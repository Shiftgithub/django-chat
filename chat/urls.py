from django.urls import path
from .views import *

urlpatterns = [
    path('', MessageAPIView.as_view(), name='message'),
]
