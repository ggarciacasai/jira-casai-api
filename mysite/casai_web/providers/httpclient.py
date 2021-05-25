import requests
from django.conf import settings


class HttpClient:
    def __init__(self):
        self.domain = settings.APISERVICE['domain']
        self.authtoken = settings.APISERVICE['token']
        

    def get(self, resource, params={}):
        headers = {
            'Authorization': 'Basic ' + self.authtoken,
            "Accept": "application/json"
        }
        response = requests.request(
            "GET",
            self.domain + resource,
            headers=headers,
            params=params
        )
        return response.text
