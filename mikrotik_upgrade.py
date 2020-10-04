from lib.classes import Issue
from lib.issues import create_issue

company_list = [
    1,  # school1
    2,  # school2
    4,  # school4
    5,  # school5
    8,  # school9
    16,  # school20
    25,  # school22
    59,  # school42
    29,  # tech1
]
new_version = '6.47.4'
title = f"Обновить ОС RouterOS до версии {new_version} на основном маршрутизаторе"
description = "Плановое обновление ПО на маршрутизаторе."
priority = 'low'
assignee_id = author_id = performer_id = '6'
comment = "В работе."
services = {'hw_router_firmware-upgrade': 1}

created_issues = []
for company_id in company_list:
    issue_params = {
        'description': description,
        'company_id': company_id,
        'assignee_id': assignee_id,
        'priority': priority
    }
    issue_id = create_issue(title, **issue_params)
    issue = Issue(issue_id)
    created_issues.append(issue)

for issue in created_issues:
    issue.add_comment(comment, author_id=author_id, public=True)
    issue.add_services(performer_id=performer_id, **services)
    # issue.complete()
