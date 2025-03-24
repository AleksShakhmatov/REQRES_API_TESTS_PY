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
def test_post_create_user(base_url):
    response = requests.post(base_url + '/api/users', data={"name": "morpheus", "job": "leader"})
    body = response.json()
    schema = path('create_user.json')

    with allure.step('Проверить'):
        assert response.status_code == 201
        assert response.json()['name'] == 'morpheus'
        assert response.json()['job'] == 'leader'
        assert response.json()['id'] != ''
        assert response.json()['createdAt'] != ''
        with open(schema) as file:
            f = file.read()
            validate(body, schema=json.loads(f))
