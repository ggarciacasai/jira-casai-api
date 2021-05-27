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

        asignnee: 'dict[str, SprintAssigne]' = {}

        asignnee = self.__assingissuesToAssigne(
            sprintPendingIssues, asignnee,  False)
        asignnee = self.__assingissuesToAssigne(
            sprintDoneIssues, asignnee,  True)

        response = {
            'assignee': []
        }

        for asigneeKey in asignnee.keys():
            response['assignee'].append(asignnee[asigneeKey])

        return response

    def __assingissuesToAssigne(self, sprint: Sprint, asignnees: 'dict[str, list]', idBurned: bool) -> 'dict[str, list]':
        unassinged = 'Unassigned Issues'
        for issue in sprint.issues:
            if (issue.fields.assignee):
                if asignnees.get(issue.fields.assignee.displayName) == None:
                    asignnees[issue.fields.assignee.displayName] = SprintAssigne(
                        issue.fields.assignee.displayName)

                asignnees[issue.fields.assignee.displayName].issues.append(
                    issue)

                if(issue.fields.points):
                    asignnees[issue.fields.assignee.displayName].burnedPoints = issue.fields.points + \
                        asignnees[issue.fields.assignee.displayName].burnedPoints if idBurned else issue.fields.points + \
                        asignnees[issue.fields.assignee.displayName].pendingPoints

            else:
                if asignnees.get(unassinged) == None:
                    asignnees[unassinged] = SprintAssigne(unassinged)

                asignnees[unassinged].issues.append(issue)
                if(issue.fields.points):
                    asignnees[unassinged].burnedPoints = issue.fields.points + \
                        asignnees[unassinged].burnedPoints if idBurned else issue.fields.points + \
                        asignnees[unassinged].pendingPoints

        return asignnees
