from abc import ABC, abstractmethod
from casai_web.models import Sprint
from casai_web.providers.httpclient import HttpClient


class IssuesProvider(ABC):
    def __init__(self, httpClient: HttpClient) -> None:
        self.httpClient = httpClient

    @abstractmethod
    def getPendingIssues(self, sprintId: str) -> Sprint:
        pass

    @abstractmethod
    def getDoneIssues(self, sprintId: str) -> Sprint:
        pass
