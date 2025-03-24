import json
import requests
from jsonschema import validate
from path import path
import allure


@allure.tag('API')
@allure.feature('API')
@allure.story('Get user info')
@allure.title('Get existing user info')
@allure.link('https://reqres.in/')
def test_update_user(base_url):
    response = requests.post = requests.put(base_url + '/api/users/2', data={"name": "morpheus", "job": "zion resident"})
    body = response.json()
    schema = path('update_user.json')

    with allure.step('Проверить'):
        assert response.status_code == 200
        assert response.json()['job'] == 'zion resident'
        assert response.json()['updatedAt'] != ''
        with open(schema) as file:
            f = file.read()
            validate(body, schema=json.loads(f))
