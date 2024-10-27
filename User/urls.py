from django.urls import path
from .views import UserListCreateView, UserDetailView,LoginView

app_name = 'User'

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('login/', LoginView.as_view(), name='login'),

]
