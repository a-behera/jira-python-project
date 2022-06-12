from jira import JIRA

# initializing jira server
jira = JIRA(server='https://webdevsite.atlassian.net/',
            basic_auth=('ankitbehera997@gmail.com', 'Op8rDov34iBfSeG4U8PdA474'))

# code to create a new issue || create_issue
issue_dict = {
    'project': {'id': 10000},
    'summary': 'issue number 7 for testing',
    'description': 'Look into this one',
    'issuetype': {'name': 'Bug'},
    'assignee': {'name': 'Ankit'},
}
new_issue = jira.create_issue(fields=issue_dict)

#code for fetching latest created ticket
latest_issue = jira.search_issues('created >  StartOfDay()', maxResults=1) # > StartOfDay
print(f"'https://webdevsite.atlassian.net/browse/{latest_issue[0]}'")




# print(latest_issue[0])
# issue = jira.issue('WEB-3')
# print(issue.fields.project.key)
# print(issue.fields.issuetype.name)
# print(issue.fields.reporter.displayName)
