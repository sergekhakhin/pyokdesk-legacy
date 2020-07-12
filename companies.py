import json

import requests

from main import api_uri
from main import token


def get_company_id(search_string):
    payload = {'search_string': str(search_string)}
    r = requests.get(f'{api_uri}/companies', json=payload, params=token)
    try:
        company_id = json.loads(r.text)[0]['id']
        return company_id
    except(KeyError, IndexError):
        print(f"[ ERROR ] Не удалось определить ID компании")


def get_company_name(company_id):
    payload = {'id': int(company_id)}
    r = requests.get(f'{api_uri}/companies', json=payload, params=token)
    try:
        company_name = json.loads(r.text)['name']
        return company_name
        print(r.text)
    except(KeyError, IndexError):
        print(f"[ ERROR ] Не удалось определить название компании")
