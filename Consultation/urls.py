from django.urls import path
from .views import (

    ConsultationListCreateAPIView,
    ConsultationRetrieveUpdateDestroyAPIView,

)
app_name = 'Consultation'
urlpatterns = [



    # Consultation CRUD
    path('api/consultations/', ConsultationListCreateAPIView.as_view(), name='consultation_list_create'),
    path('api/consultations/<int:pk>/', ConsultationRetrieveUpdateDestroyAPIView.as_view(), name='consultation_detail'),


]
