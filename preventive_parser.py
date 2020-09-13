from lib.employees import get_random_employee_id
from lib.issues import *

for issue_id in get_issue_list_by_status('opened'):
    if get_issue_info(issue_id)['title'] == "Профилактический выезд":
        employee_id = get_random_employee_id()
        if not get_issue_comments(issue_id):
            add_comment(issue_id, 'В работе.', employee_id, public=True)
        change_assignee(issue_id, employee_id)
        add_service(issue_id, '5116', 1, performer_id=employee_id)
        change_issue_status(issue_id, 'completed')
