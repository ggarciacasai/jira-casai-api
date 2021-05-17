# import http.client
import json
import requests
from requests.auth import HTTPBasicAuth

class HttpClient:
    def __init__(self, domain):
        self.domain = domain
        # self.connection = http.client.HTTPSConnection(self.domain)

    # def get(self, resource, headers = {}, params = {}):        
    def get(self, resource):        
        # auth = HTTPBasicAuth("giovanni.garcia@casai.com", "Z2lvdmFubmkuZ2FyY2lhQGNhc2FpLmNvbTpCMXhsOVd0WktZMDZROTdpZnR2TEJGRUE=")
        headers = {
           'Authorization': 'Basic ' + 'Z2lvdmFubmkuZ2FyY2lhQGNhc2FpLmNvbTpCMXhsOVd0WktZMDZROTdpZnR2TEJGRUE=',
           "Accept": "application/json"
        }
        # foo = {'text': 'Hello world github/linguist#1 **cool**, and #1!'}
        # json_params = json.dumps(params)
        # self.connection.request('GET', resource, None, headers)
        # response = self.connection.getresponse()
        # return response.read().decode()
        response = requests.request(
            "GET",
            self.domain + resource,
            headers=headers
        )

        # return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
        return response.text
