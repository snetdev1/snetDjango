
from models import party

from rest_framework import serializers





class PartySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = party
        fields = ('name', 'location', 'description', 'start', 'length', 'active', 'user')



        #sync test