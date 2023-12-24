from rest_framework import serializers
from .models import Poro


class PoroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poro
        fields = ['name', 'UUID', 'hash_key']
