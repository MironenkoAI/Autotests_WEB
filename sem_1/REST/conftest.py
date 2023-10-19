import pytest
import yaml
import requests

with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def token():
    responce = requests.post(url=data.get("url_login"), 
                         data={"username": data.get("username"), "password": data.get("password")})
    if responce.status_code == 200:
        return responce.json()['token']

@pytest.fixture()    
def get_post(token):
    responce = requests.post(url=data.get("url_post"), 
                             headers={"X-Auth-Token": token}, 
                             params={"owner": "notMe"})
    return responce.json()

@pytest.fixture()
def creat_post():
    res = requests.Session().post(url=data['url_post'], 
                                  headers={'X-Auth-Token': token},
                                  params={'title': data['title'], 
                                          'description': data['description'], 
                                          'content': data['content']})
    if res.status_code == 200:
        return "Пост успешно создан"