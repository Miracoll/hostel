from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('contact-us/', views.contactUs, name='contact-us'),
    path('about-us/', views.aboutUs, name='about-us'),
]