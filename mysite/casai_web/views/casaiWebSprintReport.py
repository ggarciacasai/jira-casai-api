from casai_web.providers.casaiWebProvider import CasaiWebProvider
from casai_web.providers.httpclient import HttpClient
from django.http import HttpResponse
from django.views import View


class CasaiWebSprintReport(View):
    jiraProvider = CasaiWebProvider(HttpClient(
        'https://casai-tech.atlassian.net/rest/api/3'))

    def get(self, request, sprintId=''):
        response = self.jiraProvider.sprintReview(sprintId)
        return HttpResponse(response)
