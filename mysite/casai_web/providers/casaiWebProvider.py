from casai_web.models import Sprint
import json


class CasaiWebProvider:
    def __init__(self, httpClient):
        self.httpClient = httpClient

    def sprintReview(self, sprintId=''):
        startAt = 0
        issues = []
        while True:
            sprintDoneIssues = self.httpClient.get('/search?&expand=projects.issuetypes.fields&startAt=' + str(startAt), {
                'jql': 'project = CW AND issuetype in (standardIssueTypes(), subTaskIssueTypes()) AND status in (Done, Released) AND Sprint = ' + sprintId,
                'fields': 'summary,description,assignee,labels,priority,issuetype,status,sprint,customfield_10036,timeestimate,timeoriginalestimate,timespent,labels,customfield_10020'
            })
            # sprintPendingIssues = self.httpClient.get('/search?&expand=projects.issuetypes.fields?limit=999', {
            #     'jql': 'project = CW AND issuetype in (standardIssueTypes(), subTaskIssueTypes()) AND status in (Blocked, "Code Review", "Design Review", "In Progress", QA, "To Do", Verification) AND Sprint = ' + sprintId,
            #     'fields': 'summary,description,assignee,labels,priority,issuetype,status,sprint,customfield_10036,timeestimate,timeoriginalestimate,timespent,labels,customfield_10020'
            # })
            response = json.loads(sprintDoneIssues)
            issues = issues + response['issues']
            startAt = startAt + len(response['issues'])

            if(startAt >= response['total']):
                break
        # y = json.loads(sprintPendingIssues)
        # sprintDone = Sprint(x)
        # sprintPending = Sprint(y)

        return issues
