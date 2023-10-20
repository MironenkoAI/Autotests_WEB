"token - a69630e0b98652da99efa4d995e7b2f6"
import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def token():
    responce = requests.post(url=data.get("url_login"), 
                         data={"username": data.get("username"), "password": data.get("password")})
    if responce.status_code == 200:
        return responce.json()['token']


def get_post(token):
    print(token)
    responce = requests.post(url=data.get("url_post"), 
                             headers={"X-Auth-Token": token}, 
                             params={"owner": "notMe"})
    print(responce.json())
    return responce.json()


def creat_post():
    res = requests.Session().post(url=data['url_post'], 
                                  headers={'X-Auth-Token': token},
                                  data={'title': data['title'], 
                                          'description': data['description'], 
                                          'content': data['content']})
    if res.status_code == 200:
        return "Пост успешно создан"
    

if __name__ == "__main__":
    get_post(token())