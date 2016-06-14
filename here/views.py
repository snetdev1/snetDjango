from django.shortcuts import render
from rest_framework import viewsets
from serializers import PartySerializer
from models import *

# Create your views here.
class PartyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = party.objects.all()
    serializer_class = PartySerializer