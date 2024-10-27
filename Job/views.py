from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Job
from .serializers import JobPostingSerializer

# List and Create
class JobPostingListCreateAPIView(ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobPostingSerializer

# Retrieve, Update, and Delete

class JobPostingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobPostingSerializer
