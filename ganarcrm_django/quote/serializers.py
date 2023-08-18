from rest_framework import serializers

from .models import Quote , Product , Inclusion , Menu_Item 
from client.serializers import ClientSerializer







class QuoteSerializer(serializers.ModelSerializer):
    
    client_name = ClientSerializer( many = False )
    
   
    
   
    
    class Meta:
        model = Quote
        
        read_only_fields = (
            'created_by',
        )
        
        fields = (
            'id',
            'subject',
            'client_name',
            'quotation_owner',
            'quotation_request_number',
            'quotation_status',
            'quotation_date',
            'expiry_date',
            'grand_total',
            'discount',
            'discount_amount',
            'sub_total',
            'tax',
            'tax_amount',
            'description',
            'terms_and_condition',
            
            
        )
        
        
class InclusionSerializer(serializers.ModelSerializer):
    
    
    
    
    
    
    
    class Meta:
        model = Inclusion
        
        read_only_fields = (
            'created_by',
        )
        
        
        fields = (
            'id',
            'inclusions',
        )

        
class Menu_ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu_Item
        
        fields = (
            'id',
            'menu_items',
        )
        
class ProductSerializer(serializers.ModelSerializer):
    
    quote = QuoteSerializer(many = False)
    inclusions = InclusionSerializer(many = True)   
    menu_items = Menu_ItemSerializer(many = True)  
    # from_date = serializers.DateField()
    
    class Meta:
        
        model = Product
        
        read_only_fields = (
            'created_by',
        )
        
        fields = (
            
            'id',
            'quote',
            'service_name',
            'unit',
            'rate',
            'quantity',
            'amount',
            'from_date',
            'to_date',
            'inclusions',
            'menu_items',
            
           
            
        )










