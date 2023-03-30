from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fullhd', views.fullhd, name='fullhd'),
    path('iss', views.iss, name='iss'),
    path('iss_ask', views.iss_ask, name='iss_ask')
]