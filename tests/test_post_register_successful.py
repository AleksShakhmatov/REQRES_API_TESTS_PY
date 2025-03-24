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
def test_post_register_successful(base_url):
    response = requests.post(base_url + '/api/register', data={"email": "eve.holt@reqres.in", "password": "pistol"})
    body = response.json()
    schema = path('register_successful.json')

    with allure.step('Проверить'):
        assert response.status_code == 200
        assert response.json()['id'] != ''
        assert response.json()['token'] != ''
        with open(schema) as file:
            f = file.read()
            validate(body, schema=json.loads(f))
