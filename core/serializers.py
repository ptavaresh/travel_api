from django.contrib.auth.models import User, Group
from rest_framework import serializers

from core.models import Place



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ['url', 'country', 'state', 'city', 'description', 'latitude', 'longitude', 'estimated_date']