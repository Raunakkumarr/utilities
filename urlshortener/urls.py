from django.urls import path
from .views import app, shorten

urlpatterns = [
    path('', app, name="urlshortner"),
]
