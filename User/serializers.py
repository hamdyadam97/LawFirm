from datetime import timezone

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class UserSerializer(serializers.ModelSerializer):
    refresh = serializers.CharField(read_only=True, source='token')
    access = serializers.CharField(read_only=True, source='token.access_token')




    def validate_password(self, data):
        validate_password(data)
        return data

    def validate_phone_number(self, value):
        phone_country_code = self.initial_data.get('phone_country_code')
        if phone_country_code == 'EG' and not value.startswith('+20'):
            raise serializers.ValidationError(_('Phone number must start with +20 for Egypt'))
        if phone_country_code == 'SA' and not value.startswith('+966'):
            raise serializers.ValidationError(_('Phone number must start with +966 for Saudi Arabia'))
        return value

    def validate_dob(self, value):
        from datetime import date
        if value >= date.today():
            raise serializers.ValidationError(_('Date of birth cannot be in the future.'))
        return value

    def validate_display_name(self, value):
        if not value or len(value) < 3:
            raise serializers.ValidationError(_('Display name must be at least 3 characters long.'))
        return value

    def create(self, validated_data):

        user = User.objects.create_user(**validated_data)

        return user

    class Meta:
        model = User
        fields = ['username', 'display_name', 'email', 'dob', 'gender', 'phone_number', 'phone_country_code','refresh',
                  'access','user_type','is_email_verified','email_verification_code','date_joined','is_phone_verified',
                  'avatar','phone_country_code','bio','password']
        extra_kwargs = {
            'password': {'write_only': True},
            'dob': {'required': True},
            'gender': {'required': True},

        }


class LoginSerializer(TokenObtainPairSerializer):
    username_field = get_user_model().USERNAME_FIELD
    def validate(self, attrs):
        try:
            super().validate(attrs)
        except AuthenticationFailed:
            raise serializers.ValidationError(_("Incorrect email or password"))

        # Customize the response data with user information if desired
        return UserSerializer(instance=self.user, context=self.context).data



