from lib.classes import Issue
from lib.employees import get_random_employee_id
from lib.issues import *

comment = "В работе."
preventive_service = '5116'

for issue in [Issue(issue_id) for issue_id in get_issue_list_by_status('opened')]:
    if issue.title == "Профилактический выезд":
        employee_id = get_random_employee_id()
        if not issue.comments['count']:
            issue.add_comment(comment, employee_id, public=True)
        issue.change_assignee(assignee_id=employee_id)
        issue.add_service(preventive_service, 1, performer_id=employee_id)
        issue.complete()
