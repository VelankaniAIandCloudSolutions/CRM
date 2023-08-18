from django.contrib import admin

# Register your models here.

from .models import Praposal , Service , Package, Item ,Default_Item, Default_Package , Venue ,  SetUp , Room_Type , Booking , Deposite , Forma_Invoice , Praposal_Invoice , DigitalSignature , Package_Group , Event_Type , Event , Meal_Plan , Audio_Visual , Option , Choice , Function , Function_Type

admin.site.register(Praposal)

admin.site.register(Service)

admin.site.register(Package)

admin.site.register(Item)

admin.site.register(Default_Package)

admin.site.register(Default_Item)

admin.site.register(Venue)

admin.site.register(SetUp)

admin.site.register(Room_Type)

admin.site.register(Booking)

admin.site.register(Deposite)

admin.site.register(Forma_Invoice)

admin.site.register(Praposal_Invoice)

admin.site.register(DigitalSignature)

admin.site.register(Package_Group)

admin.site.register(Event)

admin.site.register(Event_Type)

admin.site.register(Meal_Plan)

admin.site.register(Audio_Visual)

admin.site.register(Option)

admin.site.register(Choice)

admin.site.register(Function)

admin.site.register(Function_Type)