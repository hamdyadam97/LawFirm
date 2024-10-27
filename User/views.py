from django.utils import timezone

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import UserSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils.translation import gettext_lazy as _


class UserListCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', '')
        if User.objects.filter(email__iexact=email).exists():
            return Response({'detail': 'User with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        return self.create(request, *args, **kwargs)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


# class UserPhoneNumberListCreateView(generics.ListCreateAPIView):
#     """
#     View to list all phone numbers and create a new phone number.
#     """
#     queryset = UserPhoneNumber.objects.all()
#     serializer_class = UserPhoneNumberSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         # Add custom creation logic here, if needed
#         serializer.save()


# class UserPhoneNumberDetailView(generics.RetrieveUpdateDestroyAPIView):
#     """
#     View to retrieve, update, or delete a phone number.
#     """
#     queryset = UserPhoneNumber.objects.all()
#     serializer_class = UserPhoneNumberSerializer
#     permission_classes = [IsAuthenticated]




class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer