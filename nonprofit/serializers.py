from rest_framework import serializers
from .models import *


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestDonationBox
        fields = ['name', 'email', 'phone', 'state', 'city', 'address', 'sub_group']


class EnvSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestEnvelope
        fields = ['name', 'email', 'phone', 'state', 'city', 'address', 'sub_group']


class ClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingDonation
        fields = ['name', 'email', 'phone', 'state', 'city', 'address', 'date','sub_group', 'time']

class BoxListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestDonationBox
        fields = ['name', 'email', 'phone', 'state', 'city', 'address', 'sub_group']


class EnvListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestEnvelope
        fields = ['name', 'email', 'phone', 'state', 'city', 'address', 'sub_group']

class ClothingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingDonation
        fields = ['name', 'email', 'phone', 'state', 'city', 'address', 'date','sub_group', 'time']




  
