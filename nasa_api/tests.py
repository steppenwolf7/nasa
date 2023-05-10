from django.test import TestCase, Client
from django.urls import reverse
import json
import requests



class IndexViewTest(TestCase):
    def test_api(self):
        #testing status code of api
        url = "http://api.open-notify.org/iss-now.json"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_index_view(self):
        #testing staus code of index view
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
  
    def test_regex(self):    
        #testing if geographic coordinate are in right format
        url = "http://api.open-notify.org/iss-now.json"
        response = requests.get(url)
        data = json.loads(response.content)
        
        self.assertRegex(str(data['iss_position']['latitude']), r'^-?\d+\.\d+$')
        self.assertRegex(str(data['iss_position']['longitude']), r'^-?\d+\.\d+$')