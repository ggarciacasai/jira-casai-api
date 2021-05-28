from django.http.response import HttpResponse
from django.views.generic.base import View
from casai_web.providers.httpclient import HttpClient


def __getClient():
    httpClient = HttpClient()
    return httpClient


def index(request):
    return HttpResponse('done')

def getSprintReport(request, projectId: str, sprintId: str):
    response = __getClient().get(
        '/greenhopper/1.0/rapid/charts/sprintreport?rapidViewId=' + projectId + '&sprintId=' + sprintId)
    return HttpResponse(response)


def getSprints(request, projectId: str):
    response = __getClient().get('/agile/1.0/board/' + projectId + '/sprint')
    return HttpResponse(response)


def getBoards(request):
    response = __getClient().get('/agile/1.0/board')
    return HttpResponse(response)
