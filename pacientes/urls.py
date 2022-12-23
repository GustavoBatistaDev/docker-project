from django.urls import path
from foods.api import api


urlpatterns = [
    path('', api.urls)
]