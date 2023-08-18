from turtle import width 
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from django.http import JsonResponse, Http404, HttpResponse
from rest_framework.response import Response
from datetime import datetime,timedelta

import pdfkit
from django.template.loader import get_template
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings

# Create your views here.

# html email required stuff

from django.core.mail import send_mail
from django.http import JsonResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from datetime import datetime


from .models import   Praposal , Service , Default_Package  , Venue , SetUp , Package , Default_Item , Item , Room_Type , Booking , Deposite , Forma_Invoice , Praposal_Invoice , Package_Group , Event , Event_Type , Audio_Visual , Meal_Plan , Option , Choice , Function , Function_Type

from .serializers import ItemSerializer, PraposalSerializer , ServiceSerializer  , Default_PackageSerializer, Default_ItemSerializer , VenueSerializer ,SetUpSerializer , PackageSerializer , Room_TypeSerializer , BookingSerializer , DepositeSerializer , Forma_InvoiceSerializer , Praposal_InvoiceSerializer, Package_GroupSerializer , EventSerializer , Event_TypeSerializer , Audio_VisualsSerializer , Meal_PlanSerializer , OptionSerializer , ChoiceSerializer , FunctionSerializer, Function_TypeSerializer





@api_view(['POST'])
def create_praposal(request):
    print(request.data)
    
    from_date_str = request.data.get("from_date")
    to_date_str = request.data.get("to_date")

    praposal = Praposal.objects.create(
        name=request.data.get("name"),
        email=request.data.get("email"),
        phone=request.data.get("phone"),
        company=request.data.get("company"),
        city=request.data.get("city"),
        from_date=from_date_str,
        to_date=to_date_str,
        created_by=request.user
    )

    # Parse date strings into date objects
    # from_date = datetime.strptime(from_date_str, "%Y-%m-%d").date()
    # to_date = datetime.strptime(to_date_str, "%Y-%m-%d").date()

    # num_days = (to_date - from_date).days + 1
    # services = []
    # for i in range(num_days):
    #     date = from_date + timedelta(days=i)
    #     service = Service.objects.create(praposal=praposal,
    #                                      date=date,
    #                                      start_time = request.data.get("start_time"),
    #                                      end_time = request.data.get("end_time"),
    #                                      min_attendance = request.data.get("min_attendance"),
    #                                      max_attendance = request.data.get("max_attendance"),
    #                                      rate = request.data.get("rate"),
    #                                     )
    #     services.append(service)

    # services_queryset = Service.objects.filter(praposal=praposal)
    proposal_serializer = PraposalSerializer(praposal)
    # services_serializer = ServiceSerializer(services_queryset, many=True)

    return Response({
        'proposal': proposal_serializer.data,
        # 'services': services_serializer.data,
    })



@api_view(['GET'])
def get_praposal(request, praposal_id):
    
    
    
    praposal = Praposal.objects.filter(id=praposal_id).first()
    praposal_data = PraposalSerializer(praposal).data
    
    service = Service.objects.filter(praposal_id = praposal_id)
    service_data = ServiceSerializer(service, many=True).data
    
    data = { 'praposal': praposal_data, 'services':service_data }
    
    return Response(data)
    
    
@api_view(['GET'])
def get_proposals(request):
    
    praposal = Praposal.objects.all()
    queryset = PraposalSerializer(praposal, many=True)
    return Response(queryset.data)
    
    
@api_view(['GET'])
def get_default_packages(request):
    default_packages = Default_Package.objects.all()
    queryset = Default_PackageSerializer(default_packages, many=True)
    
    return Response(queryset.data)


@api_view(['GET'])
def get_defaults_package(request):
    package_group_id = request.GET.get('package_group_id')
    print("Received Package Group ID:", package_group_id)  # Add this print statement
    if package_group_id:
        try:
            package_group_id = int(package_group_id)  # Convert to an integer
        except ValueError:
            return Response({"error": "Invalid package_group_id"}, status=status.HTTP_400_BAD_REQUEST)

        defaults_package = Default_Package.objects.filter(package_group_id=package_group_id)
    else:
        defaults_package = Default_Package.objects.all()
    serializer = Default_PackageSerializer(defaults_package, many=True)

    return Response(serializer.data)




@api_view(['GET'])
def get_package_groups(request):
    
    package_group = Package_Group.objects.all()
    
    serializer = Package_GroupSerializer(package_group , many = True)
    
    return Response(serializer.data)

@api_view(['GET'])
def get_options(request):
    default_package_id = request.GET.get('default_package_id')
    if default_package_id:
        try:
            default_package = Default_Package.objects.get(id=default_package_id)
            options = default_package.options.all()
            serializer = OptionSerializer(options, many=True)
            print("Options Fetched Successfully:", serializer.data)  # Add this line for debugging
            return Response(serializer.data)
        except Default_Package.DoesNotExist:
            return Response([])
    else:
        return Response([])
    
    
@api_view(['GET'])
def get_default_items(request):
    option_id = request.GET.get('option_id')
    
    if option_id:
        try:
            option = Option.objects.get(id=option_id)
            defaults_item = option.default_items.all()
            serializer = Default_ItemSerializer(defaults_item, many=True)
            return Response(serializer.data)
        except Option.DoesNotExist:  # Fix the exception type here
            return Response([])
    else:
        return Response([])

    

    
    

@api_view(['GET'])
def get_events(request):
    
    events = Event.objects.all()
    
    serializer = EventSerializer(events , many = True)
    
    return Response(serializer.data)

@api_view(['GET'])
def get_event_types(request, event_id):
    try:
        event_types = Event_Type.objects.filter(event_id=event_id)
        serializer = Event_TypeSerializer(event_types, many=True)
        return Response(serializer.data)
    except Event_Type.DoesNotExist:
        return Response(status=404)
    
    
    
@api_view(['GET'])
def get_venues(request):
    
    venues = Venue.objects.all()
    
    serializer = VenueSerializer(venues , many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def get_setup(request):
    
    setups = SetUp.objects.all()
    
    queryset = SetUpSerializer(setups , many=True)
    
    return Response(queryset.data)

@api_view(['GET'])
def get_audio_visuals(request):
    
    audio_visuals = Audio_Visual.objects.all()
    
    queryset = Audio_VisualsSerializer(audio_visuals , many = True)
    
    return Response(queryset.data)


from django.db import transaction

@api_view(['POST'])
def create_services(request, praposal_id):
    print(request.data)
    print(praposal_id)
    
    sub_total = 0  # Initialize sub_total as 0
    
    services = request.data.get("services")
    
    with transaction.atomic():
        for service in services:
            print(service.get('date'))
            praposal = Praposal.objects.get(id=praposal_id)
            venues_id = service.get("venues")
            venues = Venue.objects.get(id=venues_id) if venues_id else None
          
            set_ups_id = service.get("set_ups")
            set_ups = SetUp.objects.get(id=set_ups_id) if set_ups_id else None
            
            date_object = datetime.strptime(service.get("date"), "%Y-%m-%d").date()
            
           
            min_attendance = int(service.get("min_attendance"))
            venues_amount = float(service.get("venue_amount", 0))
            miscellaneous_charges = float(service.get("miscellaneous_charges", 0))
            
            package_group_id = service.get("package_group")
            package_group = Package_Group.objects.get(pk=package_group_id)
            
            option_id = service.get("option")
            option = Option.objects.get(pk=option_id)
            
            option_rate_float = float(option.option_rate)
            
            # Calculate the amount using the choice_rate instead of rate
            amount = min_attendance * option_rate_float
            
           
            serv = Service.objects.create(
                praposal=praposal,
                date=date_object,
                start_time=service.get("start_time"),
                end_time=service.get("end_time"),
                min_attendance=min_attendance,
                max_attendance=service.get("max_attendance"),
                venues=venues,
                venue_amount=venues_amount, 
                miscellaneous_charges=miscellaneous_charges, 
                set_ups=set_ups,
                package_group=package_group, 
                rate=option_rate_float,
                # events=event,
            )
            
            



            default_package_id = service.get("default_package")
            default_package = Default_Package.objects.get(pk=default_package_id)
            
            event_id = service.get("event")
            event = Event.objects.get(pk = event_id)
            
            event_type_id = service.get("event_type")
            event_type = Event_Type.objects.get(pk = event_type_id)
            
           

            # Calculate CGST and SGST amounts for each service individually
            if default_package.default_package_name == "Venues":
                cgst_percentage = 9  # Assuming hardcoded CGST percentage of 9% for venues
                sgst_percentage = 9  # Assuming hardcoded SGST percentage of 9% for venues
            else:
                cgst_percentage = float(default_package.default_cgst_percentage)
                sgst_percentage = float(default_package.default_sgst_percentage)

            cgst_amount = (cgst_percentage / 100) * amount
            sgst_amount = (sgst_percentage / 100) * amount

            # Add the amount, cgst_amount, sgst_amount, and miscellaneous_charges to the sub_total for each service
            sub_total += amount + cgst_amount + sgst_amount + miscellaneous_charges

            package = Package.objects.create(
                service=serv,
                package_name=default_package.default_package_name,
                package_cgst_percentage=cgst_percentage,
                package_sgst_percentage=sgst_percentage
            )

            choices = Choice.objects.create(
                package=package,
                choices=option.option_name,
                choice_rate=option.option_rate,
            )
            
            function = Function.objects.create(
                service = serv,
                function = event.events
            )
            
            function_type = Function_Type.objects.create(
                function = function,
                function_type = event_type.event_type,
            )
            
           

            praposal_invoice = Praposal_Invoice.objects.create(
                package=package,
                item=default_package.default_package_name,
                date=serv.date,
                qty=min_attendance,
                rate=option_rate_float,
                amount=amount,
                cgst_percentage=cgst_percentage,
                sgst_percentage=sgst_percentage,
                cgst_amount=cgst_amount,
                sgst_amount=sgst_amount,
                grand_total=sub_total
            )

            if venues:
                # For venues, we will calculate the CGST and SGST percentages as 9% and the grand total accordingly.
                venues_cgst_amount = (9 / 100) * venues_amount
                venues_sgst_amount = (9 / 100) * venues_amount

                praposal_invoice_venues = Praposal_Invoice.objects.create(
                    package=package,
                    item=venues,
                    date=serv.date,
                    qty=1,
                    rate=venues_amount,
                    amount=venues_amount,
                    cgst_percentage=9,
                    sgst_percentage=9,
                    cgst_amount=venues_cgst_amount,
                    sgst_amount=venues_sgst_amount,
                    grand_total=sub_total + venues_cgst_amount + venues_sgst_amount
                )
                
            if miscellaneous_charges:
                # For venues, we will calculate the CGST and SGST percentages as 9% and the grand total accordingly.
                miscellaneous_cgst_amount = (9 / 100) * venues_amount
                miscellaneous_sgst_amount = (9 / 100) * venues_amount

                praposal_invoice_miscellaneous = Praposal_Invoice.objects.create(
                    package=package,
                    item= 'Miscellaneous Charges',
                    qty=1,
                    rate=miscellaneous_charges,
                    amount=miscellaneous_charges,
                    cgst_percentage=9,
                    sgst_percentage=9,
                    cgst_amount=miscellaneous_cgst_amount,
                    sgst_amount=miscellaneous_sgst_amount,
                    grand_total=sub_total + miscellaneous_cgst_amount + miscellaneous_sgst_amount
                )

            for default_item in service.get("default_item"):
                Item.objects.create(
                    choices=choices,
                    item_name=default_item.get('default_item_name'),
                    quantity=default_item.get('default_quantity')
                )

    return Response({"Service Created": "Success"})



# @api_view(['POST'])
# def create_services(request, praposal_id):
#     print(request.data)
#     print(praposal_id)
    
#     sub_total = 0  # Initialize sub_total as 0
    
#     services = request.data.get("services")
    
#     with transaction.atomic():
#         for service in services:
#             print(service.get('date'))
#             praposal = Praposal.objects.get(id=praposal_id)
#             venues_id = service.get("venues")
#             venues = Venue.objects.get(id=venues_id)
#             set_ups_id = service.get("set_ups")
#             set_ups = SetUp.objects.get(id=set_ups_id)
            
#             date_object = datetime.strptime(service.get("date"), "%Y-%m-%d").date()
            
#             # Convert min_attendance and rate to integers
#             min_attendance = int(service.get("min_attendance"))
#             rate = int(service.get("rate"))
            
#             serv = Service.objects.create(
#                 praposal=praposal,
#                 date=date_object,
#                 start_time=service.get("start_time"),
#                 end_time=service.get("end_time"),
#                 min_attendance=min_attendance,
#                 max_attendance=service.get("max_attendance"),
#                 rate=rate,
#                 venues=venues,
#                 set_ups=set_ups
#             )

#             default_package_id = service.get("default_package")
#             default_package = Default_Package.objects.get(pk=default_package_id)
            
#             # Calculate amount
#             amount = min_attendance * rate

#             # Calculate CGST and SGST amounts
#             cgst_percentage = default_package.default_cgst_percentage
#             sgst_percentage = default_package.default_sgst_percentage
            
#             # Convert cgst_percentage and sgst_percentage to integers
#             cgst_percentage = int(cgst_percentage)
#             sgst_percentage = int(sgst_percentage)

#             # Calculate CGST and SGST amounts for each service individually
#             cgst_amount = (cgst_percentage / 100) * amount
#             sgst_amount = (sgst_percentage / 100) * amount

#             # Add the amount, cgst_amount, and sgst_amount to the sub_total for each service
#             sub_total += amount

#             package = Package.objects.create(
#                 service=serv,
#                 package_name=default_package.default_package_name,
#                 package_cgst_percentage=cgst_percentage,
#                 package_sgst_percentage=sgst_percentage
#             )
            
            

#             praposal_invoice = Praposal_Invoice.objects.create(
#                 package=package,
#                 item=default_package.default_package_name,
#                 date=serv.date,
#                 qty=min_attendance,
#                 rate=rate,
#                 amount=amount,
#                 cgst_percentage=cgst_percentage,
#                 sgst_percentage=sgst_percentage,
#                 cgst_amount=cgst_amount,
#                 sgst_amount=sgst_amount,
#                 grand_total=sub_total + cgst_amount + sgst_amount
#             )

#             for default_item in service.get("default_item"):
#                 Item.objects.create(
#                     package=package,
#                     item_name=default_item.get('default_item_name'),
#                     quantity=default_item.get('default_quantity')
#                 )

#     return Response({"Service Created": "Success"})


# @api_view(['POST'])
# def create_services(request, praposal_id):
#     print(request.data)
#     print(praposal_id)
    
#     sub_total = 0  # Initialize sub_total as 0
#     cgst_amount = 0  # Initialize CGST amount as 0
#     sgst_amount = 0  # Initialize SGST amount as 0
    
#     services = request.data.get("services")
    
#     for service in services:
#         print(service.get('date'))
#         praposal = Praposal.objects.get(id=praposal_id)
#         venues_id = service.get("venues")
#         venues = Venue.objects.get(id=venues_id)
#         set_ups_id = service.get("set_ups")
#         set_ups = SetUp.objects.get(id=set_ups_id)
        
#         date_object = datetime.strptime(service.get("date"), "%Y-%m-%d").date()
#         serv = Service.objects.create(
#             praposal = praposal,
#             date = date_object,
#             start_time = service.get("start_time"),
#             end_time = service.get("end_time"),
#             min_attendance = service.get("min_attendance"),
#             max_attendance = service.get("max_attendance"),
#             rate = service.get("rate"),
#             venues = venues,
#             set_ups = set_ups
#         )

#         default_package_id = service.get("default_package")
#         default_package = Default_Package.objects.get(pk=default_package_id)
        
#         # Calculate amount
#         amount = serv.min_attendance * serv.rate

        

#         # Calculate CGST and SGST amounts
#         cgst_percentage = default_package.default_cgst_percentage
#         sgst_percentage = default_package.default_sgst_percentage

       

#         package = Package.objects.create(
#             service=serv,
#             package_name=default_package.default_package_name,
#             package_cgst_percentage=cgst_percentage,
#             package_sgst_percentage=sgst_percentage
#         )

#         praposal_invoice = Praposal_Invoice.objects.create(
#             package=package,
#             item=default_package.default_package_name,
#             date=serv.date,
#             qty=serv.min_attendance,
#             rate=serv.rate,
#             amount=amount,
#             cgst_percentage=cgst_percentage,
#             sgst_percentage=sgst_percentage,
#             cgst_amount=cgst_amount,
#             sgst_amount=sgst_amount,
            
        
#             grand_total=sub_total + cgst_amount + sgst_amount
#         )

#         for default_item in service.get("default_item"):
#             Item.objects.create(
#                 package=package,
#                 item_name=default_item.get('default_item_name'),
#                 quantity=default_item.get('default_quantity')
#             )

#     return Response({"Service Created": "Success"})

@api_view(['GET'])
def get_services(request, praposal_id):
    services = Service.objects.filter(praposal_id=praposal_id)
    service_serializer = ServiceSerializer(services, many=True)

    data = []

    for service, service_data in zip(services, service_serializer.data):
        # Check if the package_group is not None before fetching related objects
        if service.package_group:
            # Fetch the related Package_Group object for the current service using the foreign key 'package_group'
            package_group_serializer = Package_GroupSerializer(service.package_group)

            packages = Package.objects.filter(service=service)
            package_serializer = PackageSerializer(packages, many=True)

            choices = Choice.objects.filter(package__in=packages)
            choice_serializer = ChoiceSerializer(choices, many=True)

            items = Item.objects.filter(choices__in=choices)
            item_serializer = ItemSerializer(items, many=True)
            
            functions = Function.objects.filter(service = service)
            function_Serializer = FunctionSerializer(functions , many = True)
            
            function_type = Function_Type.objects.filter(function__in=functions)
            function_type_serializer = Function_TypeSerializer(function_type , many = True)

            rate = None
            if choices.exists():
                rate = choices[0].choice_rate  # Get the choice_rate of the first choice, or adjust as per your logic.

            # Add related data to the service_data dictionary
            service_data["package_groups"] = package_group_serializer.data
            service_data["packages"] = package_serializer.data
            service_data["choices"] = choice_serializer.data
            service_data["items"] = item_serializer.data
            service_data["functions"] = function_Serializer.data
            service_data["function_types"]=  function_type_serializer.data
            service_data["rate"] = rate

        data.append(service_data)

    return Response({"services": data})



# @api_view(['GET'])
# def get_services(request, praposal_id):
#     services = Service.objects.filter(praposal_id=praposal_id)
#     service_serializer = ServiceSerializer(services, many=True)

#     data = []

#     for service, service_data in zip(services, service_serializer.data):
#         # Check if the package_group is not None before fetching related objects
#         if service.package_group:
#             # Fetch the related Package_Group object for the current service using the foreign key 'package_group'
#             package_group_serializer = Package_GroupSerializer(service.package_group)

#             packages = Package.objects.filter(service=service)
#             package_serializer = PackageSerializer(packages, many=True)

#             choices = Choice.objects.filter(package__in=packages)
#             choice_serializer = ChoiceSerializer(choices, many=True)

#             items = Item.objects.filter(choices__in=choices)
#             item_serializer = ItemSerializer(items, many=True)
            
#             functions = Function.objects.filter(service = service)
#             function_Serializer = FunctionSerializer(functions , many = True)
            
#             function_type = Function_Type.objects.filter(function__in=functions)
#             function_type_serializer = Function_TypeSerializer(function_type , many = True)

#             rate = None
#             if choices.exists():
#                 rate = choices[0].choice_rate  # Get the choice_rate of the first choice, or adjust as per your logic.

#             # Add related data to the service_data dictionary
#             service_data["package_groups"] = package_group_serializer.data
#             service_data["packages"] = package_serializer.data
#             service_data["choices"] = choice_serializer.data
#             service_data["items"] = item_serializer.data
#             service_data["functions"] = function_Serializer.data
#             service_data["function_types"]=  function_type_serializer.data
#             service_data["rate"] = rate

#         data.append(service_data)

#     return Response({"services": data})


@api_view(['GET'])
def get_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    serializer = ServiceSerializer(service)
    
    packages = Package.objects.filter(service_id=service_id)
    package_serializer = PackageSerializer(packages, many=True)
    
    functions = Function.objects.filter(service_id=service_id)
    function_serializer = FunctionSerializer(functions , many = True)
    
    function_types = Function_Type.objects.filter(function__in=functions)
    function_type_serializer = Function_TypeSerializer(function_types , many = True)
    
    data = {
        "serializer": serializer.data,
        "package_serializer": package_serializer.data,
        "current_package_name": packages.first().package_name if packages.exists() else None,
        "function_serializer":function_serializer.data,
        "function_type_serializer":function_type_serializer.data
    }
    return JsonResponse(data)


@api_view(['POST'])
def update_service(request, service_id):
    try:
        service = Service.objects.get(id=service_id)
        
        date_dict = request.data.get("date")
        date_str = date_dict.get("id")
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        service.date = date
                
        service.start_time = request.data.get("start_time")
        service.end_time = request.data.get("end_time")
        
        venue_id = request.data.get("venues")
        venue = Venue.objects.get(id=venue_id)
        service.venues = venue
        
        set_ups_id = request.data.get("set_ups")
        set_ups = SetUp.objects.get(id=set_ups_id)
        service.set_ups = set_ups
        
        service.min_attendance = request.data.get("min_attendance")
        service.max_attendance = request.data.get("max_attendance")
        
        event_id = request.data.get("event")
        event = Event.objects.get(id=event_id)
        service.event = event
        
        event_type_id = request.data.get("event_type")
        event_type = Event_Type.objects.get(id=event_type_id)
        service.event_type = event_type
        
        option_id = request.data.get("option")
        option = Option.objects.get(id=option_id)
        
        package_group_id = request.data.get("package_group")
        package_group = Package_Group.objects.get(id=package_group_id)
        service.package_group = package_group
        
        default_package_id = request.data.get("default_package")
        default_package = Default_Package.objects.get(pk=default_package_id)
        
        package, created = Package.objects.get_or_create(service=service)
        package.package_name = default_package.default_package_name
        package.save()
        
        # Clear existing choices and items associated with the package
        package.choices.all().delete()
        choice = Choice.objects.create(package=package, choices=option.option_name,  choice_rate=option.option_rate )
        
        for default_item in request.data.get("default_item"):
            item_name = default_item.get('default_item_name')
            quantity = default_item.get('default_quantity')
            
           
            Item.objects.create(choices=choice, item_name=item_name, quantity=quantity)
        
        # Update rate
        rate = request.data.get("rate")
        if rate is not None:
            package.package_rate = rate
            package.save()
        
        # Update function and function type
        function, created = Function.objects.get_or_create(service=service)
        function.function = event.events
        function.save()
        
        function_type, created = Function_Type.objects.get_or_create(function=function)
        function_type.function_type = event_type.event_type
        function_type.save()
        
        service.save()
        
        return Response({"message": "Service updated successfully"})
    except Service.DoesNotExist:
        return Response({"message": "Service not found"}, status=404)





# @api_view(['POST'])
# def update_service(request, service_id):
#     try:
#         service = Service.objects.get(id=service_id)
        
#         date_dict = request.data.get("date")
#         date_str = date_dict.get("id")
#         date = datetime.strptime(date_str, "%Y-%m-%d").date()
#         service.date = date
                
#         service.start_time = request.data.get("start_time")
#         service.end_time = request.data.get("end_time")
        
#         venue_id = request.data.get("venues")
#         venue = Venue.objects.get(id=venue_id)
#         service.venues = venue
        
#         set_ups_id = request.data.get("set_ups")
#         set_ups = SetUp.objects.get(id=set_ups_id)
#         service.set_ups = set_ups
        
#         service.min_attendance = request.data.get("min_attendance")
#         service.max_attendance = request.data.get("max_attendance")
        
#         event_id = request.data.get("event")
#         event = Event.objects.get(id=event_id)
#         service.event = event
        
#         event_type_id = request.data.get("event_type")
#         event_type = Event_Type.objects.get(id=event_type_id)
#         service.event_type = event_type
        
#         package_group_id = request.data.get("package_group")
#         package_group = Package_Group.objects.get(id=package_group_id)
#         service.package_group = package_group
        
#         default_package_id = request.data.get("default_package")
#         default_package = Default_Package.objects.get(pk=default_package_id)
        
#         package, created = Package.objects.get_or_create(service=service)
#         package.package_name = default_package.default_package_name
#         package.save()
        
#         default_items = request.data.get("default_item")
        
#         # Clear existing choices and items associated with the package
#         package.choices.all().delete()
        
#         for default_item in default_items:
#             item_id = default_item.get('id')
#             item_name = default_item.get('default_item_name')
#             quantity = default_item.get('default_quantity')
            
#             choice = Choice.objects.create(package=package)
#             Item.objects.create(choices=choice, id=item_id, item_name=item_name, quantity=quantity)
        
#         # Update rate
#         rate = request.data.get("rate")
#         if rate is not None:
#             package_choice = package.choices.first()
#             if package_choice:
#                 package_choice.choice_rate = rate
#                 package_choice.save()
        
#         # Update other fields as needed
        
#         # Update function and function type
#         function = Function.objects.get(service=service)
#         function.function = event.events
#         function.save()
        
#         function_type = Function_Type.objects.get(function=function)
#         function_type.function_type = event_type.event_type
#         function_type.save()
        
#         service.save()
        
#         return Response({"message": "Service updated successfully"})
#     except Service.DoesNotExist:
#         return Response({"message": "Service not found"}, status=404)



    # except Default_Package.DoesNotExist:
    #     return Response({"message": "Default Package not found"}, status=404)
    # except Venue.DoesNotExist:
    #     return Response({"message": "Venue not found"}, status=404)
    # except Exception as e:
    #     return Response({"message": "Failed to update service", "error": str(e)}, status=500)
    
    

@api_view(['POST'])
def delete_service(request , service_id):
    
    service = Service.objects.filter(id = service_id)
    
    service.delete()
    
    return Response( { 'message': 'The service is deleted' } )


@api_view(['GET'])
def get_booking(request , booking_id):
    
    booking = Booking.objects.get(id = booking_id)
    serializer = BookingSerializer(booking)
    
    return Response(serializer.data)


@api_view(['PUT'])
def update_booking(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
        
        original_number_of_rooms = booking.number_of_rooms
        original_rate = booking.rate
        
       
        booking.check_in_date = request.data.get('check_in_date')
        booking.check_out_date = request.data.get('check_out_date')
        
        room_type_data = request.data.get('room_types')
        room_type_id = room_type_data.get('id')
        room_type = Room_Type.objects.get(id=room_type_id)
        booking.room_types = room_type
        
        booking.number_of_rooms = request.data.get('number_of_rooms')
        booking.occupancy = request.data.get('occupancy')

        booking.save()
        
        days_nights = (booking.praposal.to_date - booking.praposal.from_date).nights + 1
        if days_nights == 0:
            days_nights = 1

        booking.amount = booking.number_of_rooms * booking.rate * days_nights
        booking.save()
        

        return Response({"message": "Booking updated successfully"})
    except Booking.DoesNotExist:
        return Response({"message": "Booking not found"}, status=404)
    
@api_view(['POST'])
def delete_booking(request , booking_id):
    
    booking = Booking.objects.get(id = booking_id)
    
    booking.delete()
    
    return Response( { 'message': 'The service is deleted' } )


@api_view(['GET'])
def get_forma_invoices(request , invoice_id):
    
    forma_invoice = Forma_Invoice.objects.get(id = invoice_id)
    
    serializer = Forma_InvoiceSerializer(forma_invoice)
    
    return Response(serializer.data)


@api_view(['PUT'])
def update_forma_invoice(request, formainvoice_id):
    try:
        forma_invoice = Forma_Invoice.objects.get(id=formainvoice_id)

        # Update grand_total if it exists in the request data
        grand_total = request.data.get('grand_total')
        if grand_total is not None:
            forma_invoice.grand_total = grand_total

        # Update other fields
        forma_invoice.total_package = request.data.get('total_package')
        forma_invoice.water_cleaning = request.data.get('water_cleaning')
        forma_invoice.security_deposite = request.data.get('security_deposite')

        forma_invoice.save()

        return Response({"message": "Pro Forma Invoice updated successfully"})
    except Forma_Invoice.DoesNotExist:
        return Response({"message": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)

    
    
@api_view(['GET'])
def get_deposite(request, praposal_id):
    
    deposites = Deposite.objects.filter(praposal_id=praposal_id)
    
    deposite_serializer = DepositeSerializer(deposites, many=True)
    
    return Response(deposite_serializer.data)


@api_view(['PUT'])
def update_deposits(request, praposal_id):
    deposits_data = request.data

    deposit_ids = [deposit_data.get('id') for deposit_data in deposits_data]

    # Delete deposits that are not present in the request data
    Deposite.objects.filter(praposal_id=praposal_id).exclude(id__in=deposit_ids).delete()

    for deposit_data in deposits_data:
        deposit_id = deposit_data.get('id')
        if deposit_id:
            deposit = Deposite.objects.get(id=deposit_id)
        else:
            deposit = Deposite()

        deposit.praposal_id = praposal_id
        deposit.deposite = deposit_data.get('deposite')
        deposit.scheduled_date = deposit_data.get('scheduled_date')
        deposit.amount_due = deposit_data.get('amount_due')
        deposit.save()

    return Response('Deposits updated successfully')



@api_view(['GET'])
def get_praposal_edit(requesst , praposal_id):
    
    praposal = Praposal.objects.get(id = praposal_id)
    
    serializer = PraposalSerializer(praposal)
    
    return Response(serializer.data)

@api_view(['PUT'])
def update_praposal(request, praposal_id):
    praposal = Praposal.objects.get(id=praposal_id)
    praposal_data = request.data
    
    praposal.name = praposal_data.get("name")
    praposal.company = praposal_data.get("company")
    praposal.phone = praposal_data.get("phone")
    praposal.email = praposal_data.get("email")
    praposal.city = praposal_data.get("city")
    praposal.from_date = praposal_data.get("from_date")
    praposal.to_date = praposal_data.get("to_date")
    
    praposal.save()
    
    return Response('Proposal Updated Successfully')





    

        
        
    








@api_view(['GET'])
def get_proposalss(request):
    
    praposal = Praposal.objects.all()
    
    serializer = PraposalSerializer(praposal)
    
    return Response(serializer.data)








def generate_service_pdf(request, praposal_id):
    praposal = get_object_or_404(Praposal, pk=praposal_id)
    services = Service.objects.filter(praposal_id=praposal_id)
    packages = Package.objects.filter(service__in=services)
    items = Item.objects.filter(package__in=packages)
    
    
    template = get_template('proposal.html')
    context = {
        'praposal': praposal,
        'services': services,
        'packages': packages,
        'items': items,
    }
    html = template.render(context)

    options = {
        'page-size': 'A4',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        
    }

    path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdf = pdfkit.from_string(html, False, options=options, configuration=config)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=praposal_{praposal_id}.pdf'

    return response











# def generate_booking_pdf(request, praposal_id):
#     praposal = get_object_or_404(Praposal, pk=praposal_id)
#     bookings = Booking.objects.filter(praposal_id=praposal_id)
#     deposites = Deposite.objects.filter(praposal_id = praposal_id)
#     forma_invoices = Forma_Invoice.objects.filter(praposal_id = praposal_id)
#     days_nights = (praposal.to_date - praposal.from_date).days + 1

#     if days_nights == 0:
#         days_nights = 1
        
#     total_rooms = 0
#     for booking in bookings:
#         total_rooms += booking.number_of_rooms
#         booking.total = booking.number_of_rooms * days_nights
        
#     services = Service.objects.filter(praposal_id=praposal_id)
#     packages = Package.objects.filter(service__in=services)
#     items = Item.objects.filter(package__in=packages)
    
    
#     template = get_template('booking.html')
#     context = {
#         'praposal': praposal,
#         'bookings': bookings,
#         'deposites': deposites,
#         'forma_invoices':forma_invoices,
#         'days_nights': days_nights,
#         'total_rooms': total_rooms,
#         'services': services,
#         'packages': packages,
#         'items': items,
#     }
#     html = template.render(context)

#     options = {
#         'page-size': 'A4',
#         'margin-top': '0mm',
#         'margin-right': '0mm',
#         'margin-bottom': '0mm',
#         'margin-left': '0mm',
        
#     }

#     path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
#     config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
#     pdf = pdfkit.from_string(html, False, options=options, configuration=config)

#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename=booking_{praposal_id}.pdf'

#     return response





@api_view(['POST'])
def send_service_reminder(request, praposal_id):
    praposal = get_object_or_404(Praposal, pk=praposal_id, created_by=request.user)
    services = Service.objects.filter(praposal_id=praposal)
    packages = Package.objects.filter(service__in=services)
    items = Item.objects.filter(package__in=packages)

    subject = 'Proposal Details'
    from_email = settings.DEFAULT_FROM_EMAIL  # Use default from_email
    to = [praposal.email]

    # Modify the email body to include a greeting and a message
    text_content = f"Hello, {praposal.name}\n\nThank you for your interest in our proposal. Please find attached the proposal details in the PDF file below. If you have any questions, feel free to contact us.\n\nBest regards,\n The Oterra"


    html_content = get_template('proposal.html').render({'praposal': praposal, 'services': services, 'packages': packages, 'items': items})

    pdf_config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    options = {
        'page-size': 'A4',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
    }
    pdf = pdfkit.from_string(html_content, False, options=options, configuration=pdf_config)

    if pdf:
        name = 'praposal_{}.pdf'.format(praposal.from_date)
        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach(name, pdf, 'application/pdf')
        msg.send()
        return Response({'success': True})
    else:
        return Response({'success': False, 'message': 'Failed to generate PDF'})
    
    

@api_view(['POST'])
def send_booking_reminder(request, praposal_id):
    praposal = get_object_or_404(Praposal, pk=praposal_id, created_by=request.user)
    bookings = Booking.objects.filter(praposal_id=praposal_id)
    deposites = Deposite.objects.filter(praposal_id = praposal_id)
    packages = Package.objects.filter(service__praposal=praposal)
    praposal_invoices = Praposal_Invoice.objects.filter(package__in=packages)
    forma_invoices = Forma_Invoice.objects.filter(praposal_id = praposal_id)
    days_nights = (praposal.to_date - praposal.from_date).days + 1

    if days_nights == 0:
        days_nights = 1
        
    total_rooms = 0
    total_booking_amount = 0
    
    for booking in bookings:
        total_rooms += booking.number_of_rooms
        booking.days_nights = (booking.check_out_date - booking.check_in_date).days + 1
        booking.total = booking.number_of_rooms * days_nights
        booking.amount = booking.number_of_rooms * booking.rate * days_nights
        booking.cgst_amount = calculateCgstAmount(booking.amount, 9)  # Assuming a fixed CGST percentage of 9%
        booking.sgst_amount = calculateSgstAmount(booking.amount, 9)  # Assuming a fixed SGST percentage of 9%
        booking.total = calculateTotal(booking.amount, 9, 9)  # Assuming a fixed CGST and SGST percentage of 9%
        booking.save()
        total_booking_amount += booking.amount
        
    services = Service.objects.filter(praposal_id=praposal)
    packages = Package.objects.filter(service__in=services)
    items = Item.objects.filter(package__in=packages)
    
    first_invoice = praposal_invoices.first()
    
    for praposal_invoice in praposal_invoices:
        praposal_invoice.cgst_amount = calculateCgstAmount(praposal_invoice.amount, praposal_invoice.cgst_percentage)
        praposal_invoice.sgst_amount = calculateSgstAmount(praposal_invoice.amount, praposal_invoice.sgst_percentage)
        praposal_invoice.total = calculateTotal(praposal_invoice.amount, praposal_invoice.cgst_percentage, praposal_invoice.sgst_percentage)
        
    # Calculate grand_total, total_cgst_amount, and total_sgst_amount
    grand_total = 0
    total_cgst_amount = 0
    total_sgst_amount = 0
    
    for praposal_invoice in praposal_invoices:
        grand_total += praposal_invoice.total
        total_cgst_amount += praposal_invoice.cgst_amount
        total_sgst_amount += praposal_invoice.sgst_amount

    for booking in bookings:
        grand_total += booking.total
        total_cgst_amount += booking.cgst_amount
        total_sgst_amount += booking.sgst_amount

    subject = 'Booking Details'
    from_email = settings.DEFAULT_FROM_EMAIL  # Use default from_email
    to = [praposal.email]

    # Modify the email body to include a greeting and a message
    text_content = f"Hello, {praposal.name}\n\nThank you for your interest in our Accomadation. Please find attached the Accomadation details in the PDF file below. If you have any questions, feel free to contact us.\n\nBest regards,\n The Oterra"


    html_content = get_template('booking.html').render({
        'praposal': praposal,
        'bookings':bookings,
        'forma_invoices':forma_invoices,
        'praposal_invoices': praposal_invoices,
        'days_nights': days_nights,
        'total_rooms': total_rooms,
        'services': services,
        'packages': packages,
        'items': items ,
        'deposites':deposites,
        'calculateCgstAmount': calculateCgstAmount,
        'calculateSgstAmount': calculateSgstAmount,
        'calculateTotal': calculateTotal,
        'calculateBookingAmount': calculateBookingAmount,
        'total_booking_amount': total_booking_amount,
        'grand_total': grand_total,
        'total_cgst_amount': total_cgst_amount,
        'total_sgst_amount': total_sgst_amount,
        'first_invoice': first_invoice,
    })

    pdf_config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    options = {
        'page-size': 'A4',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
    }
    pdf = pdfkit.from_string(html_content, False, options=options, configuration=pdf_config)

    if pdf:
        name = 'booking_{}.pdf'.format(praposal.from_date)
        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach(name, pdf, 'application/pdf')
        msg.send()
        return Response({'success': True})
    else:
        return Response({'success': False, 'message': 'Failed to generate PDF'})  
    
    
    
@api_view(['GET'])
def get_room_types(request):
    
    room_type = Room_Type.objects.all()
    
    queryset = Room_TypeSerializer(room_type, many= True)
    
    return Response(queryset.data)

@api_view(['GET'])
def get_meal_plans(request):
    
    meal_plans = Meal_Plan.objects.all()
    
    queryset = Meal_PlanSerializer(meal_plans , many = True)
    
    return Response(queryset.data)


@api_view(['POST'])
def create_booking(request, praposal_id):
    praposal = Praposal.objects.get(id=praposal_id)
    booking_data = request.data
    
    room_type_ids = booking_data.get("room_types")
    room_types = Room_Type.objects.filter(id__in=room_type_ids)
    
    meal_plan_ids = booking_data.get("meal_plans")
    meal_plans = Meal_Plan.objects.filter(id__in=meal_plan_ids)
    
    number_of_rooms = booking_data.get("number_of_rooms")
    rate = booking_data.get("rate")
    days_nights = (praposal.to_date - praposal.from_date).days + 1
    
    # if days_nights == 0:
    #     days_nights = 1
    
    amount = number_of_rooms * rate * days_nights
    
    booking = Booking.objects.create(
        praposal=praposal,
        check_in_date=booking_data.get("check_in_date"),
        check_out_date=booking_data.get("check_out_date"),
        number_of_rooms=number_of_rooms,
        occupancy=booking_data.get("occupancy"),
        rate=rate,
        amount=amount,
    )
    
    # Use .set() to set the many-to-many relationships
    booking.room_types.set(room_types)
    booking.meal_plans.set(meal_plans) 
    
    booking_serializer = BookingSerializer(booking)
    
    return Response(booking_serializer.data)







# @api_view(['POST'])
# def create_booking(request, praposal_id):
#     praposal = Praposal.objects.get(id=praposal_id)
#     booking_data = request.data
    
#     room_type_id = booking_data.get("room_types")
#     room_type = Room_Type.objects.get(id=room_type_id)
    
#     number_of_rooms = booking_data.get("number_of_rooms")
#     rate = booking_data.get("rate")
#     days_nights = (praposal.to_date - praposal.from_date).days + 1
    
#     if days_nights == 0:
#         days_nights = 1
    
#     amount = number_of_rooms * rate * days_nights
    
#     booking = Booking.objects.create(
#         praposal=praposal,
#         check_in_date=booking_data.get("check_in_date"),
#         check_out_date=booking_data.get("check_out_date"),
#         room_types=room_type,
#         number_of_rooms=number_of_rooms,
#         occupancy=booking_data.get("occupancy"),
#         rate=rate,
#         amount=amount,
#     )
    
#     booking_serializer = BookingSerializer(booking)
    
#     return Response(booking_serializer.data)






@api_view(['POST'])
def create_deposites(request, praposal_id):
    print(request.data)
    print(praposal_id)
    
    praposal = Praposal.objects.get(id=praposal_id)
    
    deposite_data = request.data.get('deposite', [])
    
    for deposite_item in deposite_data:
        Deposite.objects.create(
            praposal=praposal,
            deposite=deposite_item.get('deposite'),
            scheduled_date=deposite_item.get('scheduled_date'),
            amount_due=deposite_item.get('amount_due'),
        )
    
    created_deposites = Deposite.objects.filter(praposal=praposal) 
    
    deposite_serializer = DepositeSerializer(created_deposites, many=True) 
    
    return Response(deposite_serializer.data)

@api_view(['POST'])
def submit_invoice(request):
    try:
        praposal_invoices = request.data.get('praposalInvoices')
        sub_total = Decimal(request.data.get('subTotal') or 0)
        cgst_amount = Decimal(request.data.get('cgstAmount') or 0)
        sgst_amount = Decimal(request.data.get('sgstAmount') or 0)
        grand_total = Decimal(request.data.get('grandTotal') or 0)

        # Perform the necessary operations with the data

        # Store the values in the database or perform any other required actions

        return Response({"message": "Invoice submitted successfully"})
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)



    
    




@api_view(['GET'])
def get_bookings(request , praposal_id):
    
    bookings = Booking.objects.filter(praposal_id = praposal_id)
    
    booking_serializer = BookingSerializer(bookings , many = True)
    
    return Response(booking_serializer.data)


@api_view(['GET'])
def get_deposites(request , praposal_id):
    
    deposites = Deposite.objects.filter(praposal_id = praposal_id)
    
    deposite_serializer = DepositeSerializer(deposites , many = True)
    
    return Response(deposite_serializer.data)


@api_view(['GET'])
def get_forma_invoice(request, praposal_id):
    forma_invoices = Forma_Invoice.objects.filter(praposal_id=praposal_id)
    forma_invoice_serializer = Forma_InvoiceSerializer(forma_invoices, many=True)
    return Response(forma_invoice_serializer.data)
    
    
@api_view(['DELETE'])
def delete_praposal(request, praposal_id):
    try:
        # Assuming you have a Proposal model and 'id' is the primary key
        praposal = Praposal.objects.get(id=praposal_id)
        praposal.delete()
        return JsonResponse({'message': 'Proposal deleted successfully.'})
    except Praposal.DoesNotExist:
        return JsonResponse({'error': 'Proposal not found.'}, status=404)
    

@api_view(['GET'])
def get_praposal_invoice(request, praposal_id):
    try:
        praposal = Praposal.objects.get(id=praposal_id)
        packages = Package.objects.filter(service__praposal=praposal)
        praposal_invoices = Praposal_Invoice.objects.filter(package__in=packages)
        praposal_serializer = Praposal_InvoiceSerializer(praposal_invoices, many=True)
        return Response(praposal_serializer.data)
    except Praposal.DoesNotExist:
        return Response({"error": "Praposal does not exist"}, status=status.HTTP_404_NOT_FOUND)
    

    
# def generate_booking_pdf(request, praposal_id):
#     praposal = get_object_or_404(Praposal, pk=praposal_id)
#     bookings = Booking.objects.filter(praposal_id=praposal_id)
#     deposites = Deposite.objects.filter(praposal_id=praposal_id)
#     packages = Package.objects.filter(service__praposal=praposal)
#     praposal_invoices = Praposal_Invoice.objects.filter(package__in=packages)
#     days_nights = (praposal.to_date - praposal.from_date).days + 1

#     if days_nights == 0:
#         days_nights = 1
        
#     total_rooms = 0
#     for booking in bookings:
#         total_rooms += booking.number_of_rooms
#         booking.total = booking.number_of_rooms * days_nights
#         booking.amount = calculateBookingAmount(booking)
#         booking.save()
        
#     services = Service.objects.filter(praposal_id=praposal_id)
#     packages = Package.objects.filter(service__in=services)
#     items = Item.objects.filter(package__in=packages)
    
#     first_invoice = praposal_invoices.first()

#     # Calculate sub total, CGST amount, SGST amount, and grand total
#     sub_total = calculateSubTotal(praposal_invoices, bookings)
#     cgst_amount = calculateCgstAmount(sub_total, first_invoice.cgst_percentage)
#     sgst_amount = calculateSgstAmount(sub_total, first_invoice.sgst_percentage)
#     grand_total = calculateGrandTotal(sub_total, cgst_amount, sgst_amount)

#     template = get_template('booking.html')
#     context = {
#         'praposal': praposal,
#         'bookings': bookings,
#         'deposites': deposites,
#         'praposal_invoices': praposal_invoices,
#         'days_nights': days_nights,
#         'total_rooms': total_rooms,
#         'services': services,
#         'packages': packages,
#         'items': items,
#         'sub_total': sub_total,
#         'cgst_amount': cgst_amount,
#         'sgst_amount': sgst_amount,
#         'grand_total': grand_total,
#         'first_invoice': first_invoice,
#     }
#     html = template.render(context)

#     options = {
#         'page-size': 'A4',
#         'margin-top': '0mm',
#         'margin-right': '0mm',
#         'margin-bottom': '0mm',
#         'margin-left': '0mm',
#     }

#     path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
#     config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
#     pdf = pdfkit.from_string(html, False, options=options, configuration=config)

#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename=booking_{praposal_id}.pdf'

#     return response

# from decimal import Decimal

# def calculateSubTotal(praposal_invoices, bookings):
#     sub_total = Decimal('0')

#     for praposal_invoice in praposal_invoices:
#         sub_total += praposal_invoice.amount

#     for booking in bookings:
#         sub_total += booking.amount

#     return sub_total


# def calculateCgstAmount(sub_total, cgst_percentage):
#     cgst_amount = (cgst_percentage / Decimal('100')) * sub_total
#     return cgst_amount


# def calculateSgstAmount(sub_total, sgst_percentage):
#     sgst_amount = (sgst_percentage / Decimal('100')) * sub_total
#     return sgst_amount


# def calculateGrandTotal(sub_total, cgst_amount, sgst_amount):
#     grand_total = sub_total + cgst_amount + sgst_amount
#     return grand_total


# def calculateBookingAmount(booking):
#     return booking.total * booking.rate  # Adjust the calculation based on your logic
    


from django.shortcuts import get_object_or_404, HttpResponse
from django.template.loader import get_template
import pdfkit
from decimal import Decimal

def calculateCgstAmount(amount, cgstPercentage):
    if amount is None or cgstPercentage is None:
        return 0
    cgstAmount = (amount * cgstPercentage) / 100
    return cgstAmount

def calculateSgstAmount(amount, sgstPercentage):
    if amount is None or sgstPercentage is None:
        return 0
    sgstAmount = (amount * sgstPercentage) / 100
    return sgstAmount

def calculateTotal(amount, cgstPercentage, sgstPercentage):
    if amount is None or cgstPercentage is None or sgstPercentage is None:
        return 0
    cgstAmount = calculateCgstAmount(amount, cgstPercentage)
    sgstAmount = calculateSgstAmount(amount, sgstPercentage)
    total = amount + cgstAmount + sgstAmount
    return total

def calculateBookingAmount(booking):
    # Add your logic to calculate the booking amount based on the booking details
    amount = booking.number_of_rooms * booking.rate
    return amount

def calculateGrandTotal(praposal_invoices, bookings):
    grand_total = 0
    total_cgst_amount = 0
    total_sgst_amount = 0

    # Add praposal_invoices totals
    for praposal_invoice in praposal_invoices:
        amount = praposal_invoice.amount
        cgst_amount = praposal_invoice.cgst_amount
        sgst_amount = praposal_invoice.sgst_amount
        total = praposal_invoice.total
        grand_total += total
        total_cgst_amount += cgst_amount
        total_sgst_amount += sgst_amount

    # Add bookings totals
    for booking in bookings:
        amount = booking.amount
        cgst_amount = booking.cgst_amount
        sgst_amount = booking.sgst_amount
        total = booking.total
        grand_total += total
        total_cgst_amount += cgst_amount
        total_sgst_amount += sgst_amount

    return grand_total, total_cgst_amount, total_sgst_amount



def generate_booking_pdf(request, praposal_id):
    praposal = get_object_or_404(Praposal, pk=praposal_id)
    bookings = Booking.objects.filter(praposal_id=praposal_id)
    deposites = Deposite.objects.filter(praposal_id=praposal_id)
    packages = Package.objects.filter(service__praposal=praposal)
    praposal_invoices = Praposal_Invoice.objects.filter(package__in=packages)
    days_nights = (praposal.to_date - praposal.from_date).days + 1

    if days_nights == 0:
        days_nights = 1
        
    total_rooms = 0
    total_booking_amount = 0

    for booking in bookings:
        total_rooms += booking.number_of_rooms
        booking.days_nights = (booking.check_out_date - booking.check_in_date).days + 1
        booking.total = booking.number_of_rooms * days_nights
        booking.amount = booking.number_of_rooms * booking.rate * days_nights
        booking.cgst_amount = calculateCgstAmount(booking.amount, 9)  # Assuming a fixed CGST percentage of 9%
        booking.sgst_amount = calculateSgstAmount(booking.amount, 9)  # Assuming a fixed SGST percentage of 9%
        booking.total = calculateTotal(booking.amount, 9, 9)  # Assuming a fixed CGST and SGST percentage of 9%
        booking.save()
        total_booking_amount += booking.amount


    services = Service.objects.filter(praposal_id=praposal_id)
    packages = Package.objects.filter(service__in=services)
    choices = Choice.objects.filter(package__in=packages)
    items = Item.objects.filter(choices__in=choices)
    
    functions = Function.objects.filter(service__praposal=praposal)
    function_type = Function_Type.objects.filter(function__in=functions)
    
    first_invoice = praposal_invoices.first()

    # Calculate cgst_amount, sgst_amount, and total for praposal_invoices
    for praposal_invoice in praposal_invoices:
        praposal_invoice.cgst_amount = calculateCgstAmount(praposal_invoice.amount, praposal_invoice.cgst_percentage)
        praposal_invoice.sgst_amount = calculateSgstAmount(praposal_invoice.amount, praposal_invoice.sgst_percentage)
        praposal_invoice.total = calculateTotal(praposal_invoice.amount, praposal_invoice.cgst_percentage, praposal_invoice.sgst_percentage)
        
        

    # Calculate grand_total, total_cgst_amount, and total_sgst_amount
    grand_total = 0
    total_cgst_amount = 0
    total_sgst_amount = 0

    for praposal_invoice in praposal_invoices:
        grand_total += praposal_invoice.total
        total_cgst_amount += praposal_invoice.cgst_amount
        total_sgst_amount += praposal_invoice.sgst_amount

    for booking in bookings:
        grand_total += booking.total
        total_cgst_amount += booking.cgst_amount
        total_sgst_amount += booking.sgst_amount

    
    template = get_template('booking.html')
    context = {
        'praposal': praposal,
        'bookings': bookings,
        'deposites': deposites,
        'praposal_invoices': praposal_invoices,
        'days_nights': days_nights, 
        'total_rooms': total_rooms,
        'services': services,
        'packages': packages,
        'items': items,
        'calculateCgstAmount': calculateCgstAmount,
        'calculateSgstAmount': calculateSgstAmount,
        'calculateTotal': calculateTotal,
        'calculateBookingAmount': calculateBookingAmount,
        'total_booking_amount': total_booking_amount,
        'grand_total': grand_total,
        'total_cgst_amount': total_cgst_amount,
        'total_sgst_amount': total_sgst_amount,
        'first_invoice': first_invoice,
        'function_type':function_type,
    }
    html = template.render(context)

    options = {
        'page-size': 'A4',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
    }

    path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdf = pdfkit.from_string(html, False, options=options, configuration=config)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=booking_{praposal_id}.pdf'

    return response




# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DigitalSignature

import json

@csrf_exempt
def create_signature(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            signature_data = data.get('signature_data')
            print("Received Signature Data:", signature_data)  # Debug: Check if the data is received
            if signature_data:
                DigitalSignature.objects.create(signature_data=signature_data)
                return JsonResponse({'message': 'Signature created successfully.'})
            else:
                return JsonResponse({'error': 'Signature data not provided.'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data in the request body.'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests allowed.'}, status=405)







    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    









    
    
    
    

    
    
    









    
    
            



   



































        
        













    
    
    