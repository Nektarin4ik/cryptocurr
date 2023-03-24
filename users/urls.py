from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (LoginProfileView, UserProfileView, UserRegistrationView,
                    logout)

app_name = 'users'

urlpatterns = [
    path('<int:pk>', login_required(UserProfileView.as_view()), name='profile'),
    path('registration/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginProfileView.as_view(), name='login'),
    path('logout/', logout.as_view(), name='logout'),
                 ]