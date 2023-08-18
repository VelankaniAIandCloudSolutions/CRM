from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import  get_quotes, delete_quote, delete_product, get_quote, get_inclusions, get_menu_items, get_clients , create_quotes , generate_pdf, send_reminder,accept_quotation,reject_quotation ,accepted_quotes, rejected_quotes

router = DefaultRouter()








urlpatterns = [
   
    path('',include(router.urls)),
    path('get_quotes', get_quotes, name='get_quotes'),
    path('get_quote/<int:quote_id>/',get_quote, name='get_quote'),
    path('get_inclusions', get_inclusions, name='get_inclusions'),
    path('get_menu_items',get_menu_items, name='menu_items'),
    
    
    path('create_quotes/', create_quotes, name='create_quotes'),
    
    path('quotes/<int:quote_id>/generate_pdf/', generate_pdf, name='generate_pdf'),
    
    path('quotes/<int:quote_id>/send_reminder/', send_reminder, name='send_reminder'),
    
    path('quotes/<int:quote_id>/accept_quotation/', accept_quotation, name='accept_quotation'),
    
    path('quotes/<int:quote_id>/reject_quotation/', reject_quotation, name='reject_quotation'),
    
    path('accepted_quotes', accepted_quotes, name='accepted_quotes'),
    
    path('rejected_quotes', rejected_quotes, name='rejected_quotes'),
    
   

    
    
    
    
    
    
    
    
    
    
    
    path('delete_quote/<int:quote_id>/', delete_quote, name='delete_quote'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('get_clients', get_clients, name='get_clients'),
    # path('delete_inclusions/<int:inclusions_id>/',delete_inclusions,name='delete_inclusions'),
    # path('delete_menu_items/<int:menu_items_id>/', delete_menu_items, name='delete_menu_items'),
    # path('get_quotes/<int:quote_id>/', get_quotes, name='get_quotes'),
    # path('get_quote/<int:quote_id>/', get_quote, name='get_quote')
   
   
    
]














































