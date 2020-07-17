from employees import *
from issues import *

for issue_id in get_opened_issues():
    if get_issue_info(issue_id)['title'] == "Профилактический выезд":
        employee_id = get_random_employee_id()
        if not get_issue_comments(issue_id):
            leave_comment(issue_id, 'В работе.', employee_id)
        change_assignee(issue_id, employee_id)
        add_service(issue_id, 5116, performer_id=employee_id)
        change_issue_status(issue_id, 'completed')
