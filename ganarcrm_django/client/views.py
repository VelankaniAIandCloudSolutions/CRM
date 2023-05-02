from django.contrib.auth.models import User
from django.http import Http404, JsonResponse
from django.shortcuts import render
# from rest_framework.parsers import MultiPartParser, FormParser
# import os


# from django.shortcuts import get_object_or_404
# from rest_framework.decorators import api_view, parser_classes
# from rest_framework.parsers import MultiPartParser
# from rest_framework.response import Response
# from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
# from .models import Client, File
# from .serializers import FileSerializer
# from django.urls import path
from django.views.decorators.csrf import csrf_exempt





from rest_framework import viewsets, status, filters
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from lead.models import Lead
from team.models import Team

from .models import Client, Note 
from .serializers import ClientSerializer, NoteSerializer

class ClientPagination(PageNumberPagination):
    page_size = 50

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    pagination_class = ClientPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'contact_person')
    
    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()

        serializer.save(team=team, created_by=self.request.user)

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()

        return self.queryset.filter(team=team)
    
@api_view(['POST'])
def upload_file(request, client_id):
    client = Client.objects.filter(id=client_id).first()
    if not client:
        return Response({"error": "Client not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(client=client)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        client_id = self.request.GET.get('client_id')

        return self.queryset.filter(team=team).filter(client_id=client_id)

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        client_id = self.request.data['client_id']

        serializer.save(team=team, created_by=self.request.user, client_id=client_id)
        
        
# class FileViewSet(viewsets.ModelViewSet):
#     queryset = File.objects.all()
#     serializer_class = FileSerializer
#     parser_classes = [MultiPartParser, FormParser]
        
# @api_view(['POST'])
# def create_file(request, client_id):
#     client = get_object_or_404(Client, id=client_id)
#     file_obj = request.FILES['pdf']
#     if not file_obj.content_type == 'application/pdf':
#         return Response({'error': 'Invalid file type. Only PDF files are allowed.'}, status=status.HTTP_400_BAD_REQUEST)
#     File.objects.create(client=client, pdf=file_obj)
#     return Response(status=status.HTTP_201_CREATED)
        


@api_view(['POST'])
def convert_lead_to_client(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    lead_id = request.data['lead_id']

    try:
        lead = Lead.objects.filter(team=team).get(pk=lead_id)
    except Lead.DoesNotExist:
        raise Http404
    
    client = Client.objects.create(team=team, name=lead.company, contact_person=lead.contact_person, email=lead.email, phone=lead.phone, website=lead.website, created_by=request.user)

    return Response()

@api_view(['POST'])
def delete_client(request, client_id):
    team = Team.objects.filter(members__in=[request.user]).first()

    client = team.clients.filter(pk=client_id)
    client.delete()

    return Response({'message': 'The client was deleted'})




@csrf_exempt
def get_csrf_token(request):
    return JsonResponse({'csrfToken': request.csrf_token})




# @api_view(['GET'])
# def files(request, client_id):
#     try:
#         print(client_id)
#         client = Client.objects.get(pk=client_id)
#     except Client.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     client = Client.objects.filter(client_id=client_id)
#     serializer = ClientSerializer(client, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def upload(request, client_id):
#     try:
#         client = Client.objects.get(pk=client_id)
#     except Client.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     file_serializer = FileSerializer(data=request.data)
#     if file_serializer.is_valid():
#         file_serializer.save(client_id=client_id)
#         return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


