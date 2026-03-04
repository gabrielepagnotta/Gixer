from rest_framework import serializers
from .models import OreInserite


class OreSerializer(serializers.ModelSerializer):
    class Meta:
        model = OreInserite
        fields = '__all__'
