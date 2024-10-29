from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import LawFirm, LawyerProfile
from .serializers import LawFirmSerializer, LawyerProfileSerializer


# List and Create
class LawFirmListCreateAPIView(ListAPIView):
    queryset = LawFirm.objects.all()
    serializer_class = LawFirmSerializer

# Retrieve, Update, and Delete
class LawFirmRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = LawFirmSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        profile = get_object_or_404(LawFirm, user=self.request.user)
        return profile



class LawyerProfileListCreateView(ListAPIView):
    queryset = LawyerProfile.objects.all()
    serializer_class = LawyerProfileSerializer
    permission_classes = [IsAuthenticated]


class LawyerProfileRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    serializer_class = LawyerProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):

        profile = get_object_or_404(LawyerProfile, user=self.request.user)
        return profile