from django.urls import path, include
from .views import TextApi

urlpatterns = [
    path('', TextApi),
]