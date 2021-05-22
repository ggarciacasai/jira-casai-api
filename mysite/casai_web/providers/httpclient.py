import requests
from requests.auth import HTTPBasicAuth


class HttpClient:
    def __init__(self, domain):
        self.domain = domain

    def get(self, resource, params={}):
        headers = {
            'Authorization': 'Basic ' + 'Z2lvdmFubmkuZ2FyY2lhQGNhc2FpLmNvbTpCMXhsOVd0WktZMDZROTdpZnR2TEJGRUE=',
            "Accept": "application/json"
        }
        response = requests.request(
            "GET",
            self.domain + resource,
            headers=headers,
            params=params
        )
        return response.text
