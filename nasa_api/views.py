from django.shortcuts import render
#from django.http import HttpResponse
import requests

def index(request):
    key = 'cFKcJgtVk819w8bOr5iM5UJv07wsrR0vPamoy0fx'
    url_potd = "https://api.nasa.gov/planetary/apod"
    params = {
        'api_key':key
                }
    response = requests.get(url_potd, params=params)
    data = response.json()
    
    copyright = data["copyright"]
    explanation = data["explanation"]
    hdurl = data["hdurl"]
    title = data["title"]

    my_context = {
        'copyright': copyright,
        'explanation':explanation, 
        'hdurl': hdurl, 
        'title:':title
                 }
    return render(request, 'nasa_api_templates/index.html', context=my_context)


def fullhd(request):
    key = 'cFKcJgtVk819w8bOr5iM5UJv07wsrR0vPamoy0fx'
    url_potd = "https://api.nasa.gov/planetary/apod"
    params = {
        'api_key':key
                }
    response = requests.get(url_potd, params=params)
    data = response.json()
    
    hdurl = data["hdurl"]
   
    my_context = {
        'hdurl': hdurl, 
                }
    return render(request, 'nasa_api_templates/fullhd.html', context=my_context)

