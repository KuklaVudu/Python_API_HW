import pytest
import yaml
import requests


with open('config.yaml') as f:
    conf = yaml.safe_load(f)

url = conf['url']
url1 = conf['url1']


@pytest.fixture()
def login():
    obj_data = requests.post(url=url, data={'username': 'ElenaIvan', 'password': 'b0f5c4418d'})
    token = obj_data.json()['token']
    return token


@pytest.fixture()
def post():
    obj_data = requests.post(url=url1, headers={"X-Auth-Token": conf['token']},data={
        'username': 'ElenaIvan',
        'password': 'b0f5c4418d',
        'title': 'newTitle',
        'description': 'Hello',
        'content': 'Heppy'})
    return obj_data.json()['description']