from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import LeadViewSet, delete_lead, leads_new , NotesViewSet

router = DefaultRouter()
router.register('leads', LeadViewSet, basename='leads')
router.register('notess', NotesViewSet, basename='notess')




urlpatterns = [
    path('leads/delete_lead/<int:lead_id>/', delete_lead, name='delete_lead'),
    path('', include(router.urls)),
    path('leads_new/', leads_new, name='leads_new'),
]


