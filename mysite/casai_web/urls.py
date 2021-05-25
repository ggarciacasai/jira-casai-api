from casai_web.views import casaiWebSprint
from django.urls import path
from .views.casaiWebSprintReport import CasaiWebSprintReport

urlpatterns = [
    path('board/', casaiWebSprint.getBoards),
    path('board/<str:projectId>/sprint', casaiWebSprint.getSprints),
    path('sprint/<str:sprintId>/chart', casaiWebSprint.getSprintReport),

    path('sprint/<str:sprintId>/report', CasaiWebSprintReport.as_view()),
]
