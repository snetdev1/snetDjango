from django.shortcuts import render
from rest_framework import viewsets
from serializers import PartySerializer
from models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

# Create your views here.
class PartyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = party.objects.all()
    serializer_class = PartySerializer