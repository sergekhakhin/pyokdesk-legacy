import os

api_uri = 'https://uvercom.okdesk.ru/api/v1'
api_token = os.getenv('OKDESK_API_KEY')
token = {'api_token': api_token}
