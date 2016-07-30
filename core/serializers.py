
from models import cms

from rest_framework import serializers

class cmsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cms
        fields = ('description', 'content')



