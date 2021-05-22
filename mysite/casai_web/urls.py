from django.urls import path
from .views.casaiWebSprintReport import CasaiWebSprintReport

urlpatterns = [
    path('sprint/<str:sprintId>/', CasaiWebSprintReport.as_view()),
]
