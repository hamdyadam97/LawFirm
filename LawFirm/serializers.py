from rest_framework import serializers
from .models import LawFirm, LawyerProfile


class LawFirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = LawFirm
        fields = '__all__'


class LawyerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LawyerProfile
        fields = '__all__'
