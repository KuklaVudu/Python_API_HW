import pytest
import yaml
import requests


with open('config.yaml') as f:
    conf = yaml.safe_load(f)


@pytest.fixture()
def login():
    obj_data = requests.post(url=conf['url'], data={'username': 'ElenaIvan', 'password': 'b0f5c4418d'})
    token = obj_data.json()['token']
    return token


@pytest.fixture()
def post():
    obj_data = requests.post(url=conf['url1'], headers={"X-Auth-Token": conf['token']},data={
        'username': 'ElenaIvan',
        'password': 'b0f5c4418d',
        'title': 'newTitle',
        'description': 'Hello',
        'content': 'Heppy'})
    return obj_data.json()['description']