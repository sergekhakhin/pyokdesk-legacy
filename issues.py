import json

import requests

from main import api_uri
from main import token

create_issue_params = {
    'description': str(),
    'company_id': str(),
    'contact_id': str(),
    'agreement_id': str(),
    'assignee_id': str(),
    'group_id': str(),
    'maintenance_entity_id': str(),
    'equipment_ids': list(),
    'type': str(),
    'priority': str(),
    'deadline_at': str(),
    'custom_parameters': dict(),
    'parent_id': str(),
    'author': dict()
}


def create_issue(title, **kwargs):
    payload = {
        'title': str(title)
    }
    payload.update(kwargs)
    r = requests.post(f'{api_uri}/issues', json=payload, params=token)
    if not r.status_code == 200:
        print("[ ERROR  ] " + str(json.loads(r.text)['errors']))
    else:
        issue_id = json.loads(r.text)['id']
        print(f"[ OK ] Заявка #{issue_id} создана")
        return issue_id


def change_assignee(issue_id, assignee_id=None, group_id=None):
    payload = {
        'assignee_id': str(assignee_id),
        'group_id': str(group_id)
    }
    r = requests.patch(f'{api_uri}/issues/{issue_id}/assignees', json=payload, params=token)
    if not r.status_code == 200:
        print("[ ERROR ] " + str(json.loads(r.text)['errors']))
    else:
        try:
            assignee_name = json.loads(r.text)['assignee']['name']
            print(f"[ OK ] Заявка #{issue_id}: назначен ответственный: {assignee_name}")
        except TypeError:
            print(f"[ OK ] Заявка #{issue_id}: ответственный снят")


def change_issue_status(issue_id, status_code, **kwargs):
    payload = {'code': str(status_code)}
    payload.update(kwargs)
    r = requests.post(f'{api_uri}/issues/{issue_id}/statuses', json=payload, params=token)
    if not r.status_code == 200:
        print("[ ERROR ] " + str(json.loads(r.text)['errors']))
    else:
        issue_status = json.loads(r.text)['status']['name']
        print(f'[ OK ] Заявка #{issue_id}: статус изменён на «{issue_status}»')


def leave_comment(issue_id, comment, author_id, public=True):
    payload = {
        'content': str(comment),
        'author_id': int(author_id),
        'public': bool(public)
    }
    r = requests.post(f'{api_uri}/issues/{issue_id}/comments', json=payload, params=token)
    if not r.status_code == 200:
        print("[ ERROR ] " + str(json.loads(r.text)['errors']))
    else:
        print(f'[ OK ] Заявка #{issue_id}: добавлен комментарий')


def add_service(issue_id, code, quantity=1, performer_id=None):
    payload = {
        'issue_service': {
            'code': str(code),
            'quantity': float(quantity),
            'performer_id': int(performer_id)
        }
    }
    r = requests.post(f'{api_uri}/issues/{issue_id}/services', json=payload, params=token)
    if not r.status_code == 200:
        print("[ ERROR ] " + str(json.loads(r.text)['errors']))
    else:
        print(f'[ OK ] Заявка #{issue_id}: добавлена спецификация')
