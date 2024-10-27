from django.urls import path
from .views import (
    LawFirmListCreateAPIView,
    LawFirmRetrieveUpdateDestroyAPIView, LawyerProfileListCreateView, LawyerProfileRetrieveUpdateDestroyView,

)
app_name = 'LawFirm'

urlpatterns = [
    # LawFirm CRUD
    path('api/lawfirms/', LawFirmListCreateAPIView.as_view(), name='lawfirm_list_create'),
    path('api/lawfirms/<int:pk>/', LawFirmRetrieveUpdateDestroyAPIView.as_view(), name='lawfirm_detail'),
    path('lawyer-profiles/', LawyerProfileListCreateView.as_view(), name='lawyer-profile-list-create'),
    path('lawyer-profiles/<int:pk>/', LawyerProfileRetrieveUpdateDestroyView.as_view(), name='lawyer-profile-detail'),
]
