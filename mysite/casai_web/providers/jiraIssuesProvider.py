
from casai_web.models import Sprint
from casai_web.providers.httpclient import HttpClient
from casai_web.providers.abstracts.issuesProvider import IssuesProvider
import json

class JiraIssuesProvider(IssuesProvider):
    def __init__(self, httpClient: HttpClient) -> None:
        super().__init__(httpClient)

    def __jiraApiRequest(self, endpoint, query, itemsField):
        startAt = 0
        items = []
        while True:

            rawResponse = self.httpClient.get(
                endpoint + '&startAt=' + str(startAt), query)
            response = json.loads(rawResponse)
            
            if 'errorMessages' in response:
                serializedResponse = Sprint(args={
                    'total': 0,
                    'issues': []
                })
                break
            items = items + response[itemsField]
            startAt = startAt + len(response[itemsField])

            if(startAt >= response['total']):
                response[itemsField] = items
                serializedResponse = Sprint(response)
                break

        return serializedResponse

    def getPendingIssues(self, sprintId: str):
        issues = self.__jiraApiRequest('/api/3/search?&expand=projects.issuetypes.fields', {
            'jql': 'project = CW AND issuetype in (standardIssueTypes(), subTaskIssueTypes()) AND status in (Done, Released) AND Sprint = ' + sprintId,
            'fields': 'summary,description,assignee,labels,priority,issuetype,status,sprint,customfield_10036,timeestimate,timeoriginalestimate,timespent,labels,customfield_10020'
        }, 'issues');
        
        return issues

    def getDoneIssues(self, sprintId: str):
        issues = self.__jiraApiRequest('/api/3/search?&expand=projects.issuetypes.fields', {
            'jql': 'project = CW AND issuetype in (standardIssueTypes(), subTaskIssueTypes()) AND status in (Blocked, "Code Review", "Design Review", "In Progress", QA, "To Do", Verification) AND Sprint = ' + sprintId,
            'fields': 'summary,description,assignee,labels,priority,issuetype,status,sprint,customfield_10036,timeestimate,timeoriginalestimate,timespent,labels,customfield_10020'
        }, 'issues');

        return issues
