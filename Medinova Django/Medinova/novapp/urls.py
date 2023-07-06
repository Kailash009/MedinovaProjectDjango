from django.urls import path
from .views import *
#Base URL ==>>>  http://127.0.0.1:8000/nov/


urlpatterns = [
    path('home/',view_home,name='home'),
    path('about/',view_about,name='about'),
    path('service/',view_service,name='service'),
    path('pricing/',view_pricing,name='pricing'),
    path('contact/',view_contact,name='contact'),
    path('email/',view_sendmail,name='email'),
]

