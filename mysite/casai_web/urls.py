from casai_web.views import casaiWebSprint
from django.urls import path
from .views.casaiWebSprintReport import CasaiWebSprintReport

urlpatterns = [
    path('', casaiWebSprint.index),
    path('board/', casaiWebSprint.getBoards),
    path('board/<str:projectId>/sprint', casaiWebSprint.getSprints),
    path('board/<str:projectId>/sprint/<str:sprintId>/chart', casaiWebSprint.getSprintReport),
    path('sprint/<str:sprintId>/report', CasaiWebSprintReport.as_view()),
]
