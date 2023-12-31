from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('registration/', views.RegisterView.as_view(), name='register'),
    path('coming-soon/', views.comingSoon, name='coming-soon'),
]