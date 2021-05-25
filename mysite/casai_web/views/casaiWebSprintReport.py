import json
from casai_web.helpers.CustomEncoder import CustomJsonEncoder
from django.http.response import JsonResponse
from casai_web.providers.jiraIssuesProvider import JiraIssuesProvider
from casai_web.providers.casaiWebProvider import CasaiWebSprintService
from casai_web.providers.httpclient import HttpClient
from django.http import HttpResponse
from django.views import View


class CasaiWebSprintReport(View):
    issuesProvider = JiraIssuesProvider(HttpClient())
    sprintService = CasaiWebSprintService(issuesProvider)

    def get(self, request, sprintId: str = ''):
        objRespose = self.sprintService.sprintReview(sprintId)

        response = json.dumps(objRespose, indent=4, cls=CustomJsonEncoder)
        return HttpResponse(response)
