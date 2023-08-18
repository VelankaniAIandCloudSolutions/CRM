from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import create_praposal, get_praposal ,  get_defaults_package , get_package_groups , get_default_items , get_default_packages , get_venues , get_setup , create_services , get_proposals , get_services , generate_service_pdf , generate_booking_pdf  ,send_service_reminder ,send_booking_reminder ,get_room_types , create_booking , get_bookings , create_deposites , get_deposites ,  get_forma_invoice , get_service , get_proposalss , update_service , delete_service , get_booking , update_booking , delete_booking , get_forma_invoices , update_forma_invoice , get_deposite , update_deposits , get_praposal_edit , update_praposal , delete_praposal , get_praposal_invoice , submit_invoice , create_signature , get_events , get_event_types , get_audio_visuals , get_meal_plans , get_options



router = DefaultRouter()






urlpatterns = [
   
    path('',include(router.urls)),
    
    path('create_praposal/',create_praposal, name='create_praposal' ),
    
    path('get_praposal/<int:praposal_id>/', get_praposal, name='get_praposal'),
    
    path('get_default_packages', get_default_packages, name='get_default_packages'),
    
    
    path('get_defaults_package/', get_defaults_package , name='get_defaults_package'),
    
    path('get_package_groups/' , get_package_groups , name='get_package_groups'),
    
    path('get_default_items/', get_default_items, name='get_default_items'),
   
    path('get_venues', get_venues, name='get_venues'),
   
    path('get_setup', get_setup , name='get_setup'),
   
    path('create_services/<int:praposal_id>/', create_services, name='create_services'),
    
    path('get_proposals', get_proposals, name='get_proposals'),
    
    path('get_services/<int:praposal_id>/', get_services, name='get_services'),
    
    path('get_service/<int:service_id>/' , get_service , name='get_service'),
    
    path('praposals/<int:praposal_id>/generate_service_pdf/', generate_service_pdf, name='generate_service_pdf'),
    
    path('praposals/<int:praposal_id>/generate_booking_pdf/', generate_booking_pdf, name='generate_booking_pdf'),
    
    path('praposals/<int:praposal_id>/send_service_reminder/', send_service_reminder, name='send_service_reminder'),
    
    path('praposals/<int:praposal_id>/send_booking_reminder/', send_booking_reminder, name='send_booking_reminder'),
    
    path('get_room_types', get_room_types, name='get_room_types'),
    
    path('create_booking/<int:praposal_id>/', create_booking , name='create_booking'),
    
    path('create_deposites/<int:praposal_id>/' , create_deposites , name='create_deposites'),
    
    # path('create_forma_invoice/<int:praposal_id>/' , create_forma_invoice , name='create_forma_invoice'),
    
    path('get_bookings/<int:praposal_id>/' , get_bookings , name='get_bookings'),
    
    path('get_deposites/<int:praposal_id>/' , get_deposites , name='get_deposites'),
    
    path('get_forma_invoice/<int:praposal_id>/' , get_forma_invoice , name='get_forma_invoice'),
    
    path('get_proposalss/' , get_proposalss , name='get_proposalss'),
    
    path('update_service/<int:service_id>/' , update_service , name='update_service'),
    
    path('delete_service/<int:service_id>/',  delete_service , name='delete_service'),
    
    path('get_booking/<int:booking_id>/' , get_booking , name='get_booking'),
    
    path('update_booking/<int:booking_id>/', update_booking, name='update_booking'),
    
    path('delete_booking/<int:booking_id>/' , delete_booking ,  name='delete_booking'),
    
    path('get_forma_invoices/<int:invoice_id>/' , get_forma_invoices , name='get_forma_invoices'),
    
    path('update_forma_invoice/<int:formainvoice_id>/' , update_forma_invoice , name='update_forma_invoice'),
    
    path('get_deposite/<int:praposal_id>/', get_deposite, name='get_deposite'),
    
    path('update_deposits/<int:praposal_id>/' ,  update_deposits , name='update_deposits'),
    
    path('get_praposal_edit/<int:praposal_id>/' , get_praposal_edit , name='get_praposal_edit'),
    
    path('update_praposal/<int:praposal_id>/' , update_praposal , name='update_praposal'),
    
    path('get_praposal_invoice/<int:praposal_id>/', get_praposal_invoice, name='get_praposal_invoice'),
    
    path('delete_praposal/<int:praposal_id>/' , delete_praposal , name='delete_praposal'),
    
    path('submit_invoice' , submit_invoice , name='submit_invoice'),
    
    path('create_signature/', create_signature, name='create_signature'),
    
    
    path('get_events/' , get_events , name='get_events'),
    
    path('get_event_types/<int:event_id>/' , get_event_types , name='get_event_types'),
    
    path('get_audio_visuals' , get_audio_visuals , name='get_audio_visuals'),
    
    path('get_meal_plans' , get_meal_plans  , name='get_meal_plans'),
    
    path('get_options/' , get_options , name='get_options'),




   
   
   
]















