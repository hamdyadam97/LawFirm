from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Consultation
from .serializers import ConsultationSerializer


# List and Create
class ConsultationListCreateAPIView(ListCreateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer


# Retrieve, Update, and Delete
class ConsultationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
