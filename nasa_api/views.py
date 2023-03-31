from django.shortcuts import render
#from django.http import HttpResponse
import requests
from django.http import JsonResponse

def index(request):
    key = 'cFKcJgtVk819w8bOr5iM5UJv07wsrR0vPamoy0fx'
    url_potd = "https://api.nasa.gov/planetary/apod"
    params = {
        'api_key':key
                }
    response = requests.get(url_potd, params=params)
    data = response.json()
    
    if "copyright" in data:
        copyright = data["copyright"]
    else:
        copyright = "None"
    explanation = data["explanation"]
    hdurl = data["hdurl"]
    title = data["title"]
    
    my_context = {
        'copyright':copyright,
        'explanation':explanation, 
        'hdurl':hdurl, 
        'title':title
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

def iss(request):
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    data1 = response.json()
    
    latitude = data1['iss_position']['latitude']
    longitude = data1['iss_position']['longitude']

    #latitude = str(latitude1)
    #longitude = str(longitude1)
    
    
    context = {
        'position':data1,
        'latitude':latitude,
        'longitude':longitude
              }
    return render(request, 'nasa_api_templates/iss.html', context=context)

def iss_ask(request):
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    data1 = response.json()
    
    latitude = data1['iss_position']['latitude']
    longitude = data1['iss_position']['longitude']

    context = {
        'position':data1,
        'latitude':latitude,
        'longitude':longitude
              }
    return JsonResponse(context, content_type='application/json')