from django.urls import path
from .views import LoginView, RegistrationView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page="posts"), name='logout'),
]
