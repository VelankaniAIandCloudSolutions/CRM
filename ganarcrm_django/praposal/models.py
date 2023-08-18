from django.db import models
from django.contrib.auth.models import User



class Praposal(models.Model):
    
    name = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    from_date = models.DateField(blank=True)
    to_date = models.DateField(blank=True)
    created_by = models.ForeignKey(User, related_name='praposals', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name or ''
    
    
class Venue(models.Model):
    
    venues = models.CharField(max_length=255, blank=True)
    
    
    
    def __str__(self):
        return self.venues
    

class SetUp(models.Model):
    
    set_ups = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.set_ups
    
class Audio_Visual(models.Model):
    
   
    
    audio_visuals = models.CharField(max_length = 255 , blank=True)
    
    def __str__(self):
        return self.audio_visuals
    
    
class Package_Group(models.Model):
    
    FOOD = 'food'
    BEVERAGES = 'beverages'
    ALCOHOL = 'alcohol'
    
    
    CHOICES_GROUP = (
        (FOOD, 'food'),
        (BEVERAGES,'beverages'),
        (ALCOHOL, 'alcohol'),
       
    )
    
   
    name = models.CharField(max_length = 255 , choices=CHOICES_GROUP, blank=True, null=True) 
    
    def __str__(self):
        return self.name
    


    
    
    

    

class Service(models.Model):
    
    praposal = models.ForeignKey(Praposal, related_name='services', on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    
    min_attendance = models.IntegerField(blank=True, null=True)
    
    max_attendance = models.IntegerField(blank=True, null=True)
    
    rate = models.DecimalField(max_digits=10 , decimal_places=2, blank=True, null=True)
    
    
    
    venues = models.ForeignKey(Venue, related_name='services', on_delete=models.CASCADE, blank=True, null=True)
    
    venue_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    set_ups = models.ForeignKey(SetUp, related_name='services', on_delete=models.SET_NULL, blank=True, null=True)
    
    audio_visuals = models.ManyToManyField(Audio_Visual , blank=True)
    
    package_group = models.ForeignKey(Package_Group, related_name='services', on_delete=models.CASCADE, blank=True, null=True)
    
    miscellaneous_charges = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    
    
class Function(models.Model):
    
    service = models.ForeignKey(Service, related_name='functions', on_delete=models.CASCADE , blank=True, null=True)
    
    function = models.CharField(max_length = 255 , blank=True, null=True)
    

class Function_Type(models.Model):
    
    function = models.ForeignKey(Function , related_name='function_types', on_delete=models.CASCADE , blank=True, null=True)
    
    function_type = models.CharField(max_length = 255 , blank=True, null=True)
    
        
    
    
    
    
class Event(models.Model):
    
    # service = models.ForeignKey(Service, related_name='events', on_delete=models.SET_NULL , blank=True, null=True)
    
    events = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.events

class Event_Type(models.Model):
    
    event = models.ForeignKey(Event , related_name='event_types', on_delete=models.CASCADE)
    
    event_type = models.CharField(max_length = 255 , blank=True)
    
    def __str__(self):
        return self.event_type
    


     
 
    
    
class Package(models.Model):
    
    service = models.ForeignKey(Service, related_name='packages', on_delete=models.CASCADE)
    
    package_name = models.CharField(max_length=255, blank=True, null=True)
    
    package_gst = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    package_cgst_percentage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    package_cgst_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    package_sgst_percentage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    package_sgst_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    

class Choice(models.Model):
    
    package = models.ForeignKey(Package, related_name='choices', on_delete=models.CASCADE)
    
    choices = models.CharField(max_length = 255 , blank=True, null=True)
    
    choice_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    
    
   
    
class Item(models.Model):
    
    choices = models.ForeignKey(Choice , related_name='items' , on_delete=models.CASCADE)
    
    item_name = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(blank=True , null=True)
    



    
    


class Default_Package(models.Model):
    
    package_group = models.ForeignKey(Package_Group , related_name='defaults_package', on_delete=models.CASCADE)
    
    default_package_name = models.CharField(max_length=255 , blank=True)
    
    default_gst = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    default_cgst_percentage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    default_cgst_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    default_sgst_percentage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    default_sgst_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
   
    
    
    def __str__(self):
        return self.default_package_name
    

class Option(models.Model):
    
    default_package = models.ForeignKey(Default_Package, related_name='options', on_delete=models.CASCADE)
    
    option_name = models.CharField(max_length = 255 , blank=True, null=True)
    
    option_rate =  models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    option_time = models.CharField(max_length = 255 , blank=True, null=True)
    
    def __str__(self):
        return self.option_name
    

class Default_Item(models.Model):
    
    option = models.ForeignKey(Option , related_name='default_items', on_delete=models.CASCADE)
    
    default_item_name = models.CharField(max_length=255, blank=True, null=True)
    default_quantity = models.IntegerField(blank=True , null=True)
    
    
    def __str__(self):
        return self.default_item_name
    
    
    
class Room_Type(models.Model):
    
   
    
    room_types = models.CharField(max_length=255 , blank = True)
    
    def __str__(self):
        return self.room_types
    

class Meal_Plan(models.Model):
    
    meal_plans = models.CharField(max_length = 255 , blank=True)
    
    def __str__(self):
        return self.meal_plans
    
    
    

class Booking(models.Model):
    
    praposal = models.ForeignKey(Praposal , related_name='bookings', on_delete=models.CASCADE)
    
    room_types = models.ManyToManyField(Room_Type , blank=True)
    
    meal_plans = models.ManyToManyField(Meal_Plan ,blank=True)
    
    check_in_date = models.DateTimeField(blank=True ,  null=True)
    
    check_out_date = models.DateTimeField(blank=True ,  null=True)
    
    number_of_rooms = models.IntegerField(blank=True, null=True)
    
    occupancy = models.CharField(max_length = 255 , blank = True ,  null=True)
    
    
    rate = models.DecimalField(max_digits=10 , decimal_places=2, blank=True, null=True)
    
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    room_gst = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    room_cgst_percentage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    room_cgst_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    room_sgst_percentage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    room_sgst_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    
    
   
    
    def __str__(self):
        return self.praposal.name
    
    
    
class Deposite(models.Model):
    
    praposal = models.ForeignKey(Praposal , related_name='deposites', on_delete=models.CASCADE)
    
    deposite = models.CharField(max_length = 255 , blank=True)
    
    scheduled_date = models.DateField(blank=True, null=True) 
    
    amount_due = models.CharField(max_length = 255 , blank = True)
    
    
    
class Forma_Invoice(models.Model):
    
    praposal = models.ForeignKey(Praposal , related_name='forma_invoices', on_delete=models.CASCADE)
    
    total_package = models.IntegerField(blank=True)
    
    water_cleaning = models.IntegerField(blank=True)
    
    security_deposite = models.IntegerField(blank=True)
    
    grand_total = models.IntegerField(blank=True)
    
    
    
class Praposal_Invoice(models.Model):
    
    package = models.ForeignKey(Package , related_name='praposal_invoices' , on_delete=models.CASCADE, blank=True, null=True)
    
    booking = models.ForeignKey(Booking , related_name='praposal_invoices' , on_delete=models.CASCADE, blank=True, null=True)
    
    item = models.CharField(max_length=255 , blank=True, null=True)
    
    description = models.CharField(max_length=255 , blank=True, null=True)
    
    date = models.DateField(blank=True, null=True)
    
    qty = models.IntegerField(blank=True , null= True)
    
    rate = models.DecimalField(max_digits=10 , decimal_places=2, blank=True, null=True)
    
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    cgst_percentage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    cgst_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    sgst_percentage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    sgst_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    
    
    grand_total = models.DecimalField(max_digits=10 , decimal_places=2, blank=True, null=True)
    
    

        
class DigitalSignature(models.Model):
    signature_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    

    
    

    
















