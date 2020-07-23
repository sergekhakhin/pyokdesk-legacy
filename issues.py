import json

import requests

from settings import api_uri
from settings import token


def get_issue_info(issue_id):
    payload = {'issued_id': int(issue_id)}
    r = requests.get(f'{api_uri}/issues/{issue_id}', json=payload, params=token)
    if not r.status_code == 200:
        print("[ ERROR ] " + str(json.loads(r.text)['errors']))
    else:
        return json.loads(r.text)


def get_opened_issues():
    payload = {'status[]': 'opened'}
    payload.update(token)
    r = requests.get(f'{api_uri}/issues/count', params=payload)
    if not r.status_code == 200:
        print("[ ERROR ] " + str(json.loads(r.text)['errors']))
    else:
        return json.loads(r.text)


def get_issue_comments(issue_id):
    payload = {
        'issue_id': int(issue_id)
    }
    r = requests.get(f'{api_uri}/issues/{issue_id}/comments', json=payload, params=token)
    if not r.status_code == 200:
        print("[ ERROR ] " + str(json.loads(r.text)['errors']))
    else:
        return json.loads(r.text)


def create_issue(title, **kwargs):
    payload = {
        'title': str(title)
    }
    payload.update(kwargs)
    r = requests.post(f'{api_uri}/issues', json=payload, params=token)
    if not r.status_code == 200:
        print("[ ERROR ] " + str(json.loads(r.text)['errors']))
    else:
        issue_id = json.loads(r.text)['id']
        print(f"[ OK ] Заявка #{issue_id} создана")
        return issue_id


def change_assignee(issue_id, assignee_id):
    payload = {'assignee_id': str(assignee_id)}
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
