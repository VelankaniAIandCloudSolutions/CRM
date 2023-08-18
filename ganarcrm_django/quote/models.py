from django.contrib.auth.models import User
from django.db import models

from client.models import Client

import decimal

from datetime import timedelta





class Quote(models.Model):
    
    NEW = 'new'
    ACCEPTED = 'accepted'
    ON_GOING = 'on_going'
    COMPLETED = 'completed'
    REJECTED = 'rejected'
    
    CHOICES_STATUS = (
        (NEW, 'new'),
        (ACCEPTED,'accepted'),
        (ON_GOING, 'on_going'),
        (COMPLETED, 'completed'),
        (REJECTED, 'rejected'),
    )
    

    
    
    client_name = models.ForeignKey(Client, related_name='quotes', on_delete=models.SET_NULL, null = True, blank = True,)
    subject = models.CharField(max_length=255, blank=True)
    
    quotation_owner = models.CharField(max_length=255, blank=True)
    quotation_request_number = models.CharField(max_length=255, blank=True)
    quotation_status = models.CharField(max_length=255, choices=CHOICES_STATUS, blank=True)
    quotation_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateField(auto_now=True)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount = models.CharField(max_length=255, blank=True , null=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2 , blank=True, null=True)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2 , blank=True, null=True)
    tax  = models.FloatField(blank=True , null=True)
    tax_amount = models.FloatField( blank=True, null=True)
    description = models.TextField(blank=True , null=True)
    terms_and_condition = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='quotes', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.subject
    
 

    
    
    
class Inclusion(models.Model):
    
   

    inclusions = models.CharField(max_length=255,  blank=True)
    
    
    def __str__(self):
        return self.inclusions
    
    
class Menu_Item(models.Model):
    
     
   
    
    
    menu_items = models.CharField(max_length=255,   blank=True)
    
    def __str__(self):
        return self.menu_items
    
    


    
class Product(models.Model):
    
   
    quote = models.ForeignKey(Quote, related_name='products', on_delete=models.SET_NULL, null = True, blank = True)
    service_name = models.CharField(max_length=255,blank=True , null=True)
    unit = models.IntegerField(blank=True, null=True) 
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.IntegerField(blank=True , null=True)
    amount = models.DecimalField(max_digits=10,decimal_places=3, blank=True, null=True)
    from_date = models.DateTimeField(auto_now_add=True)
    to_date = models.DateField(auto_now=True)
    inclusions = models.ManyToManyField(Inclusion, blank=True )
    menu_items = models.ManyToManyField(Menu_Item, blank=True)
   
    created_by = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE , null=True)
    
    def __str__(self):
        return self.service_name
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    



