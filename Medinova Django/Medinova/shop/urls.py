from django.urls import path
from .views import *

#BaseURL => #http://127.0.0.1:8000/ecom/

urlpatterns = [
    path('show/',view_showproduct),
]
