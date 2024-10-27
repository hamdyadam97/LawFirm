from rest_framework import serializers
from .models import Job


class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
