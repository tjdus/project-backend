from django.contrib import admin
from django.urls import path

from apps.core.views.home import HomeView

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
]
