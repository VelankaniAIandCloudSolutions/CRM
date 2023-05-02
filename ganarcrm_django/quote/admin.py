from django.contrib import admin

# Register your models here.

from .serializers import ClientSerializer

from .models import Quote , Product , Inclusion , Menu_Item





    
    

admin.site.register(Quote)

admin.site.register(Product)

admin.site.register(Inclusion)

admin.site.register(Menu_Item)
