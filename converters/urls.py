from .views import converter
from django.urls import path

urlpatterns = [
    path('', converter, name="converters"),
]
