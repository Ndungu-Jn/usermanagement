from django.urls import path
from .views import (
    UserListCreateView,
    UserDetailView,
    UserProfileView,
    ChangePasswordView,
    LoginView,
    LogoutView,
    DeleteUserView
)

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('delete-account/', DeleteUserView.as_view(), name='delete-account'),
]