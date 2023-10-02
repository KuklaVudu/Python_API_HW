import requests
import yaml
import pytest

with open('config.yaml') as f:
    conf = yaml.safe_load(f)


def token_auth(token):
    response = requests.get(conf["url_posts"],
                            headers={"X-Auth-Token": token},
                            params={"owner": "notMe"})
    return response.json()


def test_step2(post):
    assert 'Hello' in post


if __name__ == '__main':
    pytest.main(['-vv'])