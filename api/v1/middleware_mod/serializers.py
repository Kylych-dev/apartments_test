from rest_framework import serializers
from apps.appartments.models import Apartment



class EstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'
