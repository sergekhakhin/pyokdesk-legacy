import json

import requests

from lib.settings import api_uri
from lib.settings import token


def get_issue_info(issue_id: int) -> dict:
    r = requests.get(f'{api_uri}/issues/{issue_id}', params=token)
    try:
        decoded_r = json.loads(r.text)
        if 'errors' not in decoded_r:
            issue_info_dict = decoded_r
            return issue_info_dict
        else:
            print(f"[ ERROR ] {decoded_r['errors']}")
    except json.decoder.JSONDecodeError:
        r.raise_for_status()


def get_issue_comments(issue_id: int):
    payload = {'issue_id': issue_id}
    r = requests.get(f'{api_uri}/issues/{issue_id}/comments', json=payload, params=token)
    try:
        decoded_r = json.loads(r.text)
        if 'errors' not in decoded_r:
            comment_list = decoded_r
            return comment_list
        else:
            print(f"[ ERROR ] {decoded_r['errors']}")
    except:
        r.raise_for_status()


def get_issue_list_by_status(status: str) -> list:
    payload = {'status[]': status}
    payload.update(token)
    r = requests.get(f'{api_uri}/issues/count', params=payload)
    try:
        decoded_r = json.loads(r.text)
        if 'errors' not in decoded_r:
            issue_list = decoded_r
            return issue_list
        else:
            print(f"[ ERROR ] {decoded_r['errors']}")
    except json.decoder.JSONDecodeError:
        r.raise_for_status()


def create_issue(title: str, **kwargs) -> int:
    payload = {'title': title}
    payload.update(kwargs)
    r = requests.post(f'{api_uri}/issues', json=payload, params=token)
    try:
        decoded_r = json.loads(r.text)
        if 'errors' not in decoded_r:
            issue_id = decoded_r['id']
            print(f"[ OK ] Заявка #{issue_id} создана")
            return issue_id
        else:
            print(f"[ ERROR ] {decoded_r['errors']}")
    except json.decoder.JSONDecodeError:
        r.raise_for_status()


def change_assignee(issue_id: int, assignee_id=None, group_id=None):
    payload = {
        'assignee_id': assignee_id,
        'group_id': group_id
    }
    r = requests.patch(f'{api_uri}/issues/{issue_id}/assignees', json=payload, params=token)
    try:
        decoded_r = json.loads(r.text)
        if 'errors' not in decoded_r:
            if not decoded_r['assignee']:
                print(f"[ OK ] Заявка #{issue_id}: снят ответственный")
            else:
                assignee_name = decoded_r['assignee']['name']
                print(f"[ OK ] Заявка #{issue_id}: назначен ответственный -> {assignee_name}")
        else:
            print(f"[ ERROR ] {decoded_r['errors']}")
    except json.decoder.JSONDecodeError:
        r.raise_for_status()


def change_issue_status(issue_id: int, status_code: str, **kwargs):
    payload = {'code': status_code}
    payload.update(kwargs)
    r = requests.post(f'{api_uri}/issues/{issue_id}/statuses', json=payload, params=token)
    try:
        decoded_r = json.loads(r.text)
        if 'errors' not in decoded_r:
            issue_status = decoded_r['status']['name']
            print(f"[ OK ] Заявка #{issue_id}: статус изменён на «{issue_status}»")
        else:
            print(f"[ ERROR ] {decoded_r['errors']}")
    except json.decoder.JSONDecodeError:
        r.raise_for_status()


def add_comment(issue_id: int, comment: str, author_id: int, public=False):
    payload = {
        'content': comment,
        'author_id': author_id,
        'public': public
    }
    r = requests.post(f'{api_uri}/issues/{issue_id}/comments', json=payload, params=token)
    try:
        decoded_r = json.loads(r.text)
        if 'errors' not in decoded_r:
            print(f"[ OK ] Заявка #{issue_id}: добавлен комментарий")
        else:
            print(f"[ ERROR ] {decoded_r['errors']}")
    except json.decoder.JSONDecodeError:
        r.raise_for_status()


def add_service(issue_id: int, code: str, quantity: float, performer_id=None, **kwargs):
    payload = {
        'issue_service': {
            'code': str(code),
            'quantity': quantity,
            'performer_id': performer_id
        }
    }
    payload.update(kwargs)
    if not performer_id:  # Remove 'performer_id' if not passed.
        payload['issue_service'].pop('performer_id', None)
    r = requests.post(f'{api_uri}/issues/{issue_id}/services', json=payload, params=token)
    try:
        decoded_r = json.loads(r.text)
        if 'errors' not in decoded_r:
            print(f"[ OK ] Заявка #{issue_id}: добавлена спецификация")
        else:
            print(f"[ ERROR ] {decoded_r['errors']}")
    except json.decoder.JSONDecodeError:
        r.raise_for_status()
