from rest_framework import serializers

from .models import Praposal , Service , Package, Item, Default_Item, Default_Package , Venue , SetUp , Room_Type , Booking , Deposite , Forma_Invoice , Praposal_Invoice , DigitalSignature , Package_Group , Event , Event_Type , Meal_Plan , Audio_Visual , Option , Choice , Function , Function_Type


class PraposalSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Praposal
        
        read_only_fields = (
            'created_by',
        )
        
        fields = (
            'id',
            'name',
            'phone',
            'company',
            'email',
            'city',
            'from_date',
            'to_date',
        )
        
class VenueSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Venue
        
        fields = (
            'id',
            'venues',
            
            
        )
        
class SetUpSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = SetUp
        
        fields = (
            'id',
            'set_ups',
        )
        
class Audio_VisualsSerializer(serializers.ModelSerializer):
    
   
    
    class Meta : 
        
        model = Audio_Visual
        
        fields = (
            'id',          
            'audio_visuals',
        )
        
class Package_GroupSerializer(serializers.ModelSerializer):
    
    # service = ServiceSerializer()
    
    class Meta:
        
        model = Package_Group
        
        fields = (
            'id',
            # 'service',
            'name',
        )
        
        
        
class ServiceSerializer(serializers.ModelSerializer):
    
    praposal = PraposalSerializer()
    # number = NumberSerializer(),
    venues = VenueSerializer()
    set_ups = SetUpSerializer()
    package_group = Package_GroupSerializer()
    audio_visuals = Audio_VisualsSerializer(many = True)
    
    
    
    class Meta:
        
        model = Service
        
        fields = (
            'id',
            'praposal',
            'date',
            'start_time',
            'end_time',
            'min_attendance',
            'max_attendance',
            'rate',
            'venues',
            'venue_amount',
            'miscellaneous_charges',
            'set_ups',
            'audio_visuals',
            'package_group',
        )
        

class FunctionSerializer(serializers.ModelSerializer):
    
    service = ServiceSerializer()
    
    class Meta :
        
        model = Function
        
        fields = (
            
            'id',
            'service',
            'function',
        )
        
class Function_TypeSerializer(serializers.ModelSerializer):
    
    function = FunctionSerializer()
    
    class Meta :
        
        model = Function_Type
        
        fields = (
            
            'id',
            'function',
            'function_type',
        )
        
        
        
class EventSerializer(serializers.ModelSerializer):
    
    # service = ServiceSerializer()
    
    class Meta :
        
        model = Event
        
        fields = (
            'id',
            # 'service',
            'events',
        )

class Event_TypeSerializer(serializers.ModelSerializer):
    
    event = EventSerializer()
    
    class Meta :
        
        model = Event_Type
        
        fields = (
            'id',
            'event',
            'event_type',
        )
        

    
    
    
    
    
    
        
class PackageSerializer(serializers.ModelSerializer):
    
    service = ServiceSerializer()
    
    class Meta:
        
        model = Package
        
        fields = (
            'id',
            'service',
            'package_name',
            'package_gst',
            'package_cgst_percentage',
            'package_cgst_amount',
            'package_sgst_percentage',
            'package_sgst_amount',
        )
        
class ChoiceSerializer(serializers.ModelSerializer):

    package = PackageSerializer()

    class Meta:
        model = Choice  
        fields = (
            'id',
            'package',
            'choices',
            'choice_rate',
        )

    
    
        
class ItemSerializer(serializers.ModelSerializer):
    
    choices = ChoiceSerializer()
    
    class Meta:
        
        model = Item
        
        fields = (
            'id',
            'choices',
            'item_name',
            'quantity',
        )
        


        

class Default_PackageSerializer(serializers.ModelSerializer):
    
    package_group = Package_GroupSerializer()
    
    class Meta:
        
        model = Default_Package
        
        fields = (
            'id',
            'package_group',
            'default_package_name',
            'default_gst',
            'default_cgst_percentage',
            'default_cgst_amount',
            'default_sgst_percentage',
            'default_sgst_amount',
        )
        
class OptionSerializer(serializers.ModelSerializer):
    
    default_package = Default_PackageSerializer()
    
    class Meta:
        
        model = Option
        
        fields = (
            'id',
            'default_package',
            'option_name',
            'option_rate',
            'option_time',
        )
        
class Default_ItemSerializer(serializers.ModelSerializer):
    
    option = OptionSerializer()
    
    class Meta:
        
        model = Default_Item
        
        fields = (
            'id',
            'option',
            'default_item_name',
            'default_quantity',
            
        )
        
        
class Room_TypeSerializer(serializers.ModelSerializer):
    
    
    
    class Meta:
        
       
        
        model = Room_Type
        
        fields = (
            'id',
            'room_types',
        )
        
class Meal_PlanSerializer(serializers.ModelSerializer):
    
    class Meta :
        
        model = Meal_Plan
        
        fields = (
            'id',
            'meal_plans',
        )
    

class BookingSerializer(serializers.ModelSerializer):
    
    praposal = PraposalSerializer()
    
    room_types = Room_TypeSerializer(many = True)
    
    meal_plans = Meal_PlanSerializer(many = True)
    
    class Meta:
        
        model = Booking
        
        fields = (
            'id',
            'praposal',
            'room_types',
            'meal_plans',
            'check_in_date',
            'check_out_date',
            'number_of_rooms',
            'occupancy',
            'rate',
            'amount',
            'room_gst',
            'room_cgst_percentage',
            'room_cgst_amount',
            'room_sgst_percentage',
            'room_sgst_amount',
            
        )
        
        
class DepositeSerializer(serializers.ModelSerializer):
    praposal = PraposalSerializer()  
    class Meta:
        model = Deposite
        fields = (
            'id',
            'praposal',
            'deposite',
            'scheduled_date',
            'amount_due',
        )
        
        
class Forma_InvoiceSerializer(serializers.ModelSerializer):
    praposal = PraposalSerializer() 
    
    class Meta:
        model = Forma_Invoice
        fields = (
            'id',
            'praposal',
            'total_package',
            'water_cleaning',
            'security_deposite',
            'grand_total',
        )
        

class Praposal_InvoiceSerializer(serializers.ModelSerializer):
    
    package = PackageSerializer() 
    
    booking = BookingSerializer()
    
    class Meta:
        
        model = Praposal_Invoice
        
        fields = (
            
            'id',
            'package',
            'booking',
            'item',
            'description',
            'date',
            'qty',
            'rate',
            'amount',
            'sub_total',
            'cgst_percentage',
            'cgst_amount',
            'sgst_percentage',
            'sgst_amount',
            'grand_total',
        )
        

class DigitalSignatureSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = DigitalSignature
        
        fields = (
            'signature_data',
        )


    
    

        
        

        

        



