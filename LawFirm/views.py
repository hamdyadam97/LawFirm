from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import LawFirm, LawyerProfile
from .serializers import LawFirmSerializer, LawyerProfileSerializer


# List and Create
class LawFirmListCreateAPIView(ListCreateAPIView):
    queryset = LawFirm.objects.all()
    serializer_class = LawFirmSerializer

# Retrieve, Update, and Delete
class LawFirmRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = LawFirm.objects.all()
    serializer_class = LawFirmSerializer



class LawyerProfileListCreateView(ListCreateAPIView):
    queryset = LawyerProfile.objects.all()
    serializer_class = LawyerProfileSerializer
    permission_classes = [IsAuthenticated]
class LawyerProfileRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = LawyerProfile.objects.all()
    serializer_class = LawyerProfileSerializer
    permission_classes = [IsAuthenticated]