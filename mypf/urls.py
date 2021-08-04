from django.urls import path
from . import views #import views

# adding url:
urlpatterns = [

    path('', views.portfolio, name='portfolio'), #portfolio
    path('contact', views.contact, name='contact'), #contact
]