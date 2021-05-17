from casai_web.providers.httpclient import HttpClient
from django.http import HttpResponse
from django.views import View


class Index(View):
    def get(self, request):
        # <view logic>
        client = HttpClient('https://casai-tech.atlassian.net/rest/api/3')
        # response = client.get('/dashboard', {
        #     'Authorization': 'Basic ' + 'Z2lvdmFubmkuZ2FyY2lhQGNhc2FpLmNvbTpCMXhsOVd0WktZMDZROTdpZnR2TEJGRUE=',
        #     'Accept': 'application/json',
        # })
        response = client.get('/dashboard')
        return HttpResponse(response)
