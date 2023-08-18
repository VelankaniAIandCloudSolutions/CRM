from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

from team.models import Team

from .models import Lead , Notes

from .serializers import LeadSerializer , NotesSerializer


class LeadPagination(PageNumberPagination):
    page_size = 8

class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    pagination_class = LeadPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('company', 'contact_person')
    
    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()

        serializer.save(team=team, created_by=self.request.user)
    
    def perform_update(self, serializer):
        obj = self.get_object()

        member_id = self.request.data['assigned_to']

        if member_id:
            user = User.objects.get(pk=member_id)
            serializer.save(assigned_to=user)
        else:
            serializer.save()

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()

        return self.queryset.filter(team=team)

@api_view(['POST'])
def delete_lead(request, lead_id):
    team = Team.objects.filter(members__in=[request.user]).first()

    lead = team.leads.filter(pk=lead_id)
    lead.delete()

    return Response({'message': 'The lead was deleted'})

@api_view(['GET'])
def leads_new(request):
    leads_new = Lead.objects.filter(status='new')
    print(leads_new) # for debugging purposes only
    serializer = LeadSerializer(leads_new, many=True)
    print(serializer.data) # for debugging purposes only
    return Response(serializer.data)

class NotesViewSet(viewsets.ModelViewSet):
    serializer_class = NotesSerializer
    queryset = Notes.objects.all()

    def get_queryset(self):
        team = Team.objects.filter(members=self.request.user).first()
        lead_id = self.request.GET.get('lead_id')
        if team:
            return self.queryset.filter(team=team, lead_id=lead_id)
        return self.queryset.none()

    def perform_create(self, serializer):
        team = Team.objects.filter(members=self.request.user).first()
        lead_id = self.request.data.get('lead_id')
        serializer.save(team=team, created_by=self.request.user, lead_id=lead_id)










