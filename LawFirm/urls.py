from django.urls import path
from .views import (
    LawFirmListCreateAPIView,
    LawFirmRetrieveUpdateDestroyAPIView, LawyerProfileListCreateView, LawyerProfileRetrieveUpdateDestroyView,

)
app_name = 'LawFirm'

urlpatterns = [
    # LawFirm CRUD
    path('lawfirm_list_create/', LawFirmListCreateAPIView.as_view(), name='lawfirm_list_create'),
    path('lawfirm_profile/', LawFirmRetrieveUpdateDestroyAPIView.as_view(), name='lawfirm_detail'),
    path('lawyer-profile-list/', LawyerProfileListCreateView.as_view(), name='lawyer-profile-list'),
    path('lawyer-profile/', LawyerProfileRetrieveUpdateDestroyView.as_view(), name='lawyer-profile-detail'),
]
