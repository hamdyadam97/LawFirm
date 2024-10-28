from rest_framework import serializers

from User.serializers import UserSerializer
from .models import LawFirm, LawyerProfile


class LawFirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = LawFirm
        fields = '__all__'


class LawyerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = LawyerProfile
        fields = '__all__'
