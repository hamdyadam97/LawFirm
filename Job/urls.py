from django.urls import path
from .views import (

    JobPostingListCreateAPIView,
    JobPostingRetrieveUpdateDestroyAPIView
)

app_name = 'Jobs'
urlpatterns = [

    # JobPosting CRUD
    path('api/jobpostings/', JobPostingListCreateAPIView.as_view(), name='jobposting_list_create'),
    path('api/jobpostings/<int:pk>/', JobPostingRetrieveUpdateDestroyAPIView.as_view(), name='jobposting_detail'),
]
