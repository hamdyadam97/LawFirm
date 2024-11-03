from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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

    def patch(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        print(partial)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        print( serializer)
        print( request.data)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        # Save the serializer to update the object in the database
        serializer.save()

class LawFirmRetrieveAPIView(RetrieveAPIView):
    serializer_class = LawFirmSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        profile = get_object_or_404(LawFirm, user=self.request.user)
        return profile



class LawFirmRetrieveOwnerAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = LawFirmSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        profile = get_object_or_404(LawFirm, owner=self.request.user)
        return profile