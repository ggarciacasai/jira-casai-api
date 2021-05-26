import json
from json.encoder import JSONEncoder
from casai_web.models import Sprint, SprintAssigne
from casai_web.providers.abstracts.issuesProvider import IssuesProvider



class CasaiWebSprintService:
    def __init__(self, issuesProvider: IssuesProvider):
        self.issuesProvider = issuesProvider


    def sprintReview(self, sprintId: str = ''):
        sprintPendingIssues = self.issuesProvider.getPendingIssues(sprintId)
        sprintDoneIssues = self.issuesProvider.getDoneIssues(sprintId)

        asignne: dict[str, SprintAssigne] = {}
        unassinged = 'Unassigned Issues'
        asignne[unassinged] = []

        asignne = self.__assingissuesToAssigne(
            sprintPendingIssues, asignne, unassinged, False)
        asignne = self.__assingissuesToAssigne(
            sprintDoneIssues, asignne, unassinged, True)
        

        return asignne

    def __assingissuesToAssigne(self, sprint: Sprint, assignes: 'dict[str, list]', unassinged: str, idBurned: bool) -> 'dict[str, list]':
        for issue in sprint.issues:
            if (issue.fields.assignee):
                if assignes.get(issue.fields.assignee.displayName):
                    assignes[issue.fields.assignee.displayName].issues.append(
                        issue)
                    if(issue.fields.points):
                        assignes[issue.fields.assignee.displayName].burnedPoints = issue.fields.points + \
                            assignes[issue.fields.assignee.displayName].burnedPoints if idBurned  else issue.fields.points + assignes[issue.fields.assignee.displayName].pendingPoints
                else:
                    assignes[issue.fields.assignee.displayName] = SprintAssigne(
                        issue.fields.assignee.displayName)
                    assignes[issue.fields.assignee.displayName].issues.append(
                        issue)
                    if(issue.fields.points):
                        assignes[issue.fields.assignee.displayName].burnedPoints = issue.fields.points + \
                            assignes[issue.fields.assignee.displayName].burnedPoints if idBurned  else issue.fields.points + assignes[issue.fields.assignee.displayName].pendingPoints
            else:
                assignes[unassinged].append(issue)

        return assignes
