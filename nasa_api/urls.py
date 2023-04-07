from django.urls import path

from . import views

urlpatterns = [
    path('nasa_photo', views.nasa_photo, name='nasa_photo'),
    path('fullhd', views.fullhd, name='fullhd'),
    path('', views.index, name='index'),
    path('iss_ask', views.iss_ask, name='iss_ask')
]