from lib.classes import Issue
from lib.issues import get_issue_list_by_status

for issue in [Issue(issue_id) for issue_id in get_issue_list_by_status(['opened', 'repair'])]:
    if issue.group_id:
        issue.change_assignee(6)
