from django.urls import path, include


from rest_framework.routers import DefaultRouter

from .views import ClientViewSet, NoteViewSet, convert_lead_to_client, delete_client,upload_file

router = DefaultRouter()
router.register('clients', ClientViewSet, basename='clients')
router.register('notes', NoteViewSet, basename='notes')
# router.register('files', FileViewSet, basename='files')

urlpatterns = [
    path('convert_lead_to_client/', convert_lead_to_client, name='convert_lead_to_client'),
    path('clients/delete_client/<int:client_id>/', delete_client, name='delete_client'),
        path('clients/<int:pk>/upload_file/', upload_file, name='upload_file'),
    
#    path('files/<int:client_id>/', files, name='files'),
   
#    path('csrf_cookie/', get_csrf_token, name='get_csrf_token'),
    
    # path('clients/<int:client_id>/files/', file),
    # path('files/upload/<int:client_id>/',upload, name='upload' ),
    path('', include(router.urls)),
]