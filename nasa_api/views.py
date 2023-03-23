from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    key = 'cFKcJgtVk819w8bOr5iM5UJv07wsrR0vPamoy0fx'
    url_potd = "https://api.nasa.gov/planetary/apod"
    params = {
        'api_key':key
                }
    response = requests.get(url_potd, params=params)
    data = response.json()
    
    return render(request, 'nasa_api_templates/index.html',{'data':data})