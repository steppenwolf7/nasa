from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'nasa_api_templates/index.html')