from collections import namedtuple
from django.db import models
from collections.abc import Sequence
from typing import TypeVar

TModel = TypeVar('TModel')
Any = TypeVar('Any')


def mapListToModelList(arrEl: Sequence[Any], Model: TModel) -> list[TModel]:
    response = list(map(lambda el: Model(el), arrEl))
    return response


# Create your models here.
class Sprint(object):
    def __init__(self, args: dict[str, Any] = {}) -> None:
        self.total = args['total']
        self.issues: list[Issue] = mapListToModelList(args['issues'], Issue)
        # self.issues = list(map(lambda el: mapTo(el, Issue), kwargs['issues']))


class Issue(object):
    def __init__(self, args: dict[str, Any] = {}) -> None:
        self.key = args['key']
        self.fields = IssueField(args['fields'])


class IssueField(object):
    def __init__(self, args: dict[str, Any] = {}) -> None:
        self.assignee = Asignee(args['assignee']) if args['assignee'] else None
        self.summary: str = args['summary']
        self.issuetype: str = args['issuetype']['name'] if args['issuetype'] else None
        self.labels: Sequence[str] = args['labels']
        self.points: float = args['customfield_10036']
        self.priority: str = args['priority']['name'] if args['priority'] else None
        self.timespent: int = args['timespent']
        self.timeoriginalestimate: int = args['timeoriginalestimate']
        self.sprints = mapListToModelList(
            args['customfield_10020'], SprintType)
        self.timeestimate: int = args['timeestimate']
        self.status: str = args['status']['name'] if args['status'] else None


class Asignee(object):
    def __init__(self, args: dict[str, Any] = {}) -> None:
        self.displayName = args['displayName']
        self.accountId = args['accountId']


class SprintType(object):
    def __init__(self, args: dict[str, Any] = {}) -> None:
        self.name = args['name']
        self.id = args['id']

class SprintAssigne(object):
    def __init__(self, name: str) -> None:
        self.name = name
        self.issues: list(Issue) = []
        self.burnedPoints = 0
        self.pendingPoints = 0
