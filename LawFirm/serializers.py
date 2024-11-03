from rest_framework import serializers

from User.serializers import UserSerializer
from .models import LawFirm, LawyerProfile


class LawFirmSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = LawFirm
        fields = '__all__'


class LawyerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = LawyerProfile
        fields = '__all__'

    def update(self, instance, validated_data):
        # Loop through each attribute and set it on the instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()  # Save the updated instance to the database
        return instance
