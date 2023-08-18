

import pdfkit
from rest_framework import generics
from .models import *

from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.template.loader import get_template


from django.shortcuts import render

from team.models import Team

from client.models import Client

from .serializers import ClientSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import JsonResponse, Http404, HttpResponse


# from django.shortcuts import render
# from django.template.loader import render_to_string
# from django.core.mail import EmailMessage
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
# from django.http import JsonResponse
# import json

from django.core.mail import EmailMultiAlternatives






from .serializers import QuoteSerializer, ProductSerializer, Menu_ItemSerializer, InclusionSerializer

from .models import Quote , Product , Inclusion , Menu_Item


# html email required stuff

from django.core.mail import send_mail
from django.http import JsonResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string








@api_view(['POST'])
def create_quotes(request):
    print(request.data)
    quote = Quote.objects.create( subject = request.data.get("subject"),
                                  client_name_id =request.data.get("client_name"),
                                  quotation_owner = request.data.get("quotation_owner"),
                                  quotation_request_number = request.data.get("quotation_request_number"),
                                  quotation_status = request.data.get("quotation_status"),
                                  quotation_date = request.data.get("quotation_date"),
                                  expiry_date = request.data.get("expiry_date"),
                                  grand_total = request.data.get("grand_total"),
                                  discount = request.data.get("discount"),
                                  discount_amount = request.data.get("discount_amount"),
                                  sub_total = request.data.get("sub_total"),
                                  tax = request.data.get("tax"),
                                  tax_amount = request.data.get("tax_amount"),
                                  description = request.data.get("description"),
                                  terms_and_condition = request.data.get("terms_and_condition"),
                                  created_by = request.user
                                )
    products = request.data.get("products")
   
    for product in products:
        
       
        
       
        pro = Product.objects.create (quote = quote,
                                service_name = product.get("service_name"),
                                unit = product.get("unit"),
                                rate = product.get("rate"),
                                quantity = product.get("quantity"),
                                amount = product.get("amount"),
                                from_date = product.get("from_date"),
                                to_date = product.get("to_date"),

                                
                            )
        
     
        
        print(product.get("inclusions"))
        for inclusion in product.get("inclusions"):
            pro.inclusions.add(inclusion)
        for menu_item in product.get("menu_items"):
            pro.menu_items.add(menu_item)
        
        pro.save()   
       

       
        
    return Response({"Quote Created":"Success"})   
    
@api_view(['GET'])
def get_quotes(request):
    quote = Quote.objects.all()
    queryset = QuoteSerializer(quote, many=True)
    return Response(queryset.data)

@api_view(['DELETE'])
def delete_quote(request, quote_id):
    print(quote_id)
    quote = Quote.objects.get(id = quote_id)
    try:
        quote.delete()
    except Exception as e:
        Response("Unable to Deleter Quote!")
    return Response("Quote Deleted Sucessfully")
@api_view(['GET'])
def get_quote(request, quote_id):
    quote = Quote.objects.filter(id=quote_id).first()
    quote_data = QuoteSerializer(quote).data
    product = Product.objects.filter(quote_id=quote_id)
    product_data = ProductSerializer(product, many=True).data
    data = {'quote': quote_data, 'products': product_data}
    return Response(data)
   
    return Response(queryset.data)

@api_view(['DELETE'])
def delete_product(request, product_id):
    print(product_id)
    product = Product.objects.get(id = product_id)
    try:
        product.delete()
    except Exception as e:
        Response("Unable to Delete Product!")
    return Response("Product Delelted Sucessfully")


@api_view(['GET'])
def get_clients(request ):
    client = Client.objects.all( )
    queryset = ClientSerializer(client,many = True)
    
    return Response(queryset.data)

@api_view(['GET'])
def get_inclusions(request):
    inclusions = Inclusion.objects.get()
    queryset = InclusionSerializer(inclusions , many = True)
    
    return Response(queryset.data)

@api_view(['GET'])
def get_menu_items(request):
    menu_items = Menu_Item.objects.all()
    queryset = Menu_ItemSerializer(menu_items, many = True)
    
    return Response(queryset.data)


@api_view(['GET'])
def get_inclusions(request):
    inclusions = Inclusion.objects.all()
    queryset = InclusionSerializer(inclusions, many=True)
    return Response(queryset.data)

@api_view(['GET'])
def get_menu_items(request):
    menu_items = Menu_Item.objects.all()
    queryset = Menu_ItemSerializer(menu_items, many=True)
    return Response(queryset.data)


def generate_pdf(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    products = Product.objects.filter(quote_id=quote_id)
    template = get_template('pdf.html')
    html = template.render({'quote': quote, 'products': products})

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
    response['Content-Disposition'] = f'attachment; filename=quote_{quote_id}.pdf'
    
    return response








@api_view(['POST'])
def send_reminder(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id, created_by=request.user)
    products = Product.objects.filter(quote_id=quote_id)

    subject = 'Quotation Details'
    from_email = settings.DEFAULT_FROM_EMAIL # Use default from_email
    to = [quote.client_name.email]

    text_content = 'Your quotation number is: #' + str(quote.quotation_request_number)
    html_content = get_template('pdf.html').render({'quote': quote, 'products': products})

    pdf_config = pdfkit.configuration(wkhtmltopdf= r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    pdf = pdfkit.from_string(html_content, False, options={}, configuration=pdf_config)
    if pdf:
        name = 'quote_{}.pdf'.format(quote.quotation_request_number)
        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        msg.attach(name, pdf, 'application/pdf')
        msg.send()
        return Response({'success': True})
    else:
        return Response({'success': False, 'message': 'Failed to generate PDF'})
    
    
@api_view(["PATCH"])
def accept_quotation(request, quote_id):
    try:
        quote = Quote.objects.get(id=quote_id)
        quote.is_accepted = True
        quote.quotation_status = 'accepted'
        quote.save()
        return JsonResponse({'message': 'Quotation accepted.'})
    except quote.DoesNotExist:
        return JsonResponse({'error': 'Quotation not found.'}, status=404)
    
    
    
  
    
    
    
    
    




    
    
    
    return response

@api_view(["GET"])
def accepted_quotes(request):
    accepted_quotes = Quote.objects.filter(quotation_status='accepted')
    serializer = QuoteSerializer(accepted_quotes, many=True)
    return Response(serializer.data)

@api_view(['PATCH'])
def reject_quotation(request, quote_id):
    try:
        quote = Quote.objects.get(id = quote_id)
        quote.is_rejected = True
        quote.quotation_status = 'rejected'
        quote.save()
        return JsonResponse({ 'message': 'Quotation rejected' })
    except quote.DoesNotExist:
        return JsonResponse({'error': 'Quotation not found'}, status=404)
    
@api_view(['GET'])
def rejected_quotes(request):
    rejected_quotes = Quote.objects.filter(quotation_status = 'rejected')
    serializer = QuoteSerializer(rejected_quotes , many=True)
    return Response(serializer.data)





























    
    
    
    
    
    
    






    
        
        
         



    















# @api_view(['DELETE'])
# def delete_inclusions(request, inclusions_id):
#     print(inclusions_id)
#     inclusions = Inclusion.objects.get(id = inclusions_id)
#     try:
#         inclusions.delete()
#     except Exception as e:
#         Response("Unable to Delete Inclusion!")
#     return Response("Inclusion Delete Sucessfully")


# @api_view(['DELETE'])
# def delete_menu_items(request, menu_items_id):
#     print(menu_items_id)
#     menu_items = Menu_Item.objects.get(id = menu_items_id)
#     try:
#         menu_items.delete()
#     except Exception as e:
#         Response("Unable to Delete Menu_Items")
#     return Response("Menu_Items Deleted Sucessfully")



        


# @api_view(['POST'])
# def update_quote(requset, id):
#     quote = Quote.objects.get(id =id)
#     serializer = QuoteSerializer(instance = quote, data = requset.data)
#     if serializer.is_valid():
#         serializer.save()
#     else:
#         return HttpResponse('Some Error Occured')
#     return Response(serializer.data)


 
# @api_view(['GET'])
# def get_quotes(request, quote_id):
#     quote = Quote.objects.get(pk = quote_id)
#     products = quote.products
#     inclusions = Inclusion.objects.all()
#     menu_items = Menu_Item.objects.all()
    
    
#     quote_serializer = QuoteSerializer(quote)
#     product_serializer = ProductSerializer(products)
#     inclusion_serializer = InclusionSerializer(inclusions, many = True)
#     menu_item_serializer = Menu_ItemSerializer(menu_items, many = True)
    
#     return Response({
#         'quote': quote_serializer.data,
#         'products':product_serializer.data,
#         'inclusions':inclusion_serializer.data,
#         'menu_items': menu_item_serializer.data
#     })
    
# @api_view(['GET'])
# def get_quote_details(request, quote_id):
#     quote = Quote.objects.get(pk = quote_id)
    
    
    
    
     
 
 
 
    
    

# @api_view(['GET'])
# def get_quote(request, quote_id):
#     inclusions = Inclusions.objects.all()
    
#     inclusions_serializer = InclusionsSerializer(inclusions, many=True)
#     return Response({
#         'inclusions':inclusions_serializer.data,
        
#     })





# @csrf_exempt
# def send_quotation(request, quote_id):
    
#         try:
#             quote = Quote.objects.get(id=quote_id)
#         except Quote.DoesNotExist:
#             return JsonResponse({'success': False, 'error': 'Quotation not found.'})

#         # Fetch products for quotation from database
#         products = Product.objects.filter(quote_id = quote_id)

       

#         # Prepare email message with quotation details
#         message = f"Quotation details:\n\n ID: {quote.id}\n Name: {quote.subject}\n"

#         # Add product details to email message
#         message += "\nProducts:\n"
#         for product in products:
#             message += f"- {product.service_name}: {product.quantity} x {product.rate} = {product.amount}\n"

#         # Add inclusion details to email message
#         message += "\nInclusions:\n"
#         for inclusion in inclusions:
#             message += f"- {inclusion.name}\n"

#         # Add menu item details to email message
#         message += "\nMenu items:\n"
#         for menu_item in menu_items:
#             message += f"- {menu_item.name} ({menu_item.price})\n"

#         # Send email
#         send_mail(
#             'Quotation details',
#             message,
#             'from@example.com',
#             ['to@example.com'],
#             fail_silently=False,
#         )

#         # Return success response to frontend
#         return JsonResponse({'success': True})




# @api_view(['POST'])
# def send_reminder(request, quote_id):
#     try:
#         quote = Quote.objects.get(pk=quote_id, created_by=request.user)
#         products = Product.objects.filter(quote_id=quote_id)

#         subject = 'Quotation Details'
#         from_email = settings.DEFAULT_FROM_EMAIL # Use default from_email
#         to = ['mdadil80708@gmail.com']

#         text_content = 'Your quotation number is: #' + str(quote.quotation_request_number)
#         html_content = get_template('pdf.html').render({'quote': quote, 'products': products})

#         pdf_config = pdfkit.configuration(wkhtmltopdf= r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
#         pdf = pdfkit.from_string(html_content, False, options={}, configuration=pdf_config)
#         if pdf:
#             name = 'quote_{}.pdf'.format(quote.quotation_request_number)
#             accept_url = request.build_absolute_uri('http://localhost:8081/dashboard/quotes/:id/thankyouu')
#             reject_url = request.build_absolute_uri('/quotation-response/?id='+str(quote_id)+'&status=rejected')
#             html_content += f'<p><a href="{accept_url}">Accept Quotation</a> | <a href="{reject_url}">Reject Quotation</a></p>'
#             msg = EmailMultiAlternatives(subject, text_content, from_email, to)
#             msg.attach_alternative(html_content, "text/html")
#             msg.attach(name, pdf, 'application/pdf')
#             msg.send()
#             return Response({'success': True})
#         else:
#             return Response({'success': False, 'message': 'Failed to generate PDF'})

#     except ObjectDoesNotExist:
#         raise Http404("Quote does not exist")

#     except Exception as e:
#         return Response({'success': False, 'message': 'Error: {}'.format(str(e))})







    
    
    
    
  
