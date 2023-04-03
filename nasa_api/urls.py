from django.urls import path

from . import views

urlpatterns = [
    path('nasa_photo', views.index, name='nasa_photo'),
    path('fullhd', views.fullhd, name='fullhd'),
    path('', views.iss, name='index'),
    path('iss_ask', views.iss_ask, name='iss_ask')
]