from login import token, get_post
import pytest
import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)

def test_step1(token, get_post):
    res = get_post(token)
    res_list = res.get("data")
    res_id_list = [item['id'] for item in res_list]
    assert 1234 in res_id_list, "тест не пройден"


# def test_check_post_create(creat_post):
#     result = requests.Session().get(url=data['url_post'], headers={'X-Auth-Token': token}).json()['data']
#     # print(result)
#     list_description = [i['description'] for i in result]
#     assert data['description'] in list_description, 'check_post_create FAIL'


if __name__ == '__main__':
    pytest.main(["-vv"])