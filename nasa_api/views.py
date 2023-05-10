from django.shortcuts import render
import requests
from django.http import JsonResponse

def index(request):                                             
    # view which ask api for latitude and longitude and rander index.html
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)                                    #Przetestować czy url daje odpowiedz
    data = response.json()                                              #sprawdzić czy zmienna data jest w json
    
    latitude = data['iss_position']['latitude']                         #sprawdzić czy zmienne zwracają prządany rodzaj danych
    longitude = data['iss_position']['longitude']
    
    context = {                                                  #make context dictionary with all my data                   
        'latitude':latitude,
        'longitude':longitude
             }
    return render(request, 'nasa_api_templates/index.html', context=context)

def iss_ask(request):                                             #Make a request to the API to get the ISS position data
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    data = response.json()
    
    latitude = data['iss_position']['latitude']                    # Extract latitude and longitude from the response
    longitude = data['iss_position']['longitude']
    minus_sign1 = latitude[0]
    minus_sign2 = longitude[0]
    
    letter1 = None                                                 #Determine if latitude and longitude are in the northern/southern or eastern/western 
    if minus_sign1 == "-":
        letter1 = "S"
    else:
        letter1 = "N"

    letter2 = None
    if minus_sign2 == "-":
        letter2 = "W"
    else:
        letter2 = "E"
    
    context = {                                                     #make context dictionary with all my data
        'latitude':latitude,
        'longitude':longitude, 
        'letter1':letter1,
        'letter2':letter2
              }
    return JsonResponse(context, content_type='application/json')    # Return the context as a JSON response


def nasa_photo(request):
    #Make a request to the API to get data
    key = 'cFKcJgtVk819w8bOr5iM5UJv07wsrR0vPamoy0fx'        
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        'api_key':key
                }
    response = requests.get(url, params=params)
    data = response.json()
    
    if "copyright" in data:                                   #checking if "copyright" exist in "data" if not make it None
        copyright = data["copyright"]
    else:
        copyright = "None"
    
    explanation = data["explanation"]
    hdurl = data["hdurl"]
    title = data["title"]
    
    my_context = {                                          #make context dictionary with all my data
        'copyright':copyright,
        'explanation':explanation, 
        'hdurl':hdurl, 
        'title':title
                 }
    return render(request, 'nasa_api_templates/nasa_photo.html', context=my_context)


def fullhd(request):                                        
    #Make a request to the API to get data
    key = 'cFKcJgtVk819w8bOr5iM5UJv07wsrR0vPamoy0fx'        
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        'api_key':key
                }
    response = requests.get(url, params=params)
    data = response.json()
    
    hdurl = data["hdurl"]                                   # getting photo in full hd
   
    my_context = {
        'hdurl': hdurl, 
                }
    return render(request, 'nasa_api_templates/fullhd.html', context=my_context)

