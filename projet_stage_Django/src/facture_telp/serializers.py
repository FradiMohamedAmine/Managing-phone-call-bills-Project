from rest_framework import serializers
from .models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = client
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = service
        fields = '__all__'


class OffreSerializer(serializers.ModelSerializer):
    class Meta:
        model = offre
        fields = '__all__'


class ContratSerializer(serializers.ModelSerializer):
    class Meta:
        model = contrat
        fields = '__all__'


class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = facture
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
