from django.shortcuts import render
import requests
from django.http import JsonResponse

def index(request):
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    data = response.json()
    
    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']
    
 
    context = {
        'latitude':latitude,
        'longitude':longitude
             }
    return render(request, 'nasa_api_templates/index.html', context=context)

def iss_ask(request):
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    data = response.json()
    
    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']
    minus_sign1 = latitude[0]
    minus_sign2 = longitude[0]
    
    letter1 = None
    if minus_sign1 == "-":
        letter1 = "S"
    else:
        letter1 = "N"

    letter2 = None
    if minus_sign2 == "-":
        letter2 = "W"
    else:
        letter2 = "E"
    
    context = {
        'latitude':latitude,
        'longitude':longitude, 
        'letter1':letter1,
        'letter2':letter2
              }
    return JsonResponse(context, content_type='application/json')


def nasa_photo(request):
    key = 'cFKcJgtVk819w8bOr5iM5UJv07wsrR0vPamoy0fx'
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        'api_key':key
                }
    response = requests.get(url, params=params)
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
    return render(request, 'nasa_api_templates/nasa_photo.html', context=my_context)


def fullhd(request):
    key = 'cFKcJgtVk819w8bOr5iM5UJv07wsrR0vPamoy0fx'
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        'api_key':key
                }
    response = requests.get(url, params=params)
    data = response.json()
    
    hdurl = data["hdurl"]
   
    my_context = {
        'hdurl': hdurl, 
                }
    return render(request, 'nasa_api_templates/fullhd.html', context=my_context)

