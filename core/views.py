from django.shortcuts import render
from rest_framework import viewsets
from serializers import cmsSerializer
from models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class cmsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = cms.objects.all()
    serializer_class = cmsSerializer
