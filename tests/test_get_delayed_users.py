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
def test_get_delayed_response(base_url):
    response = requests.get(base_url + '/api/users', params='delay=2')

    with allure.step('Проверить'):
        assert response.status_code == 200
        assert response.json()['page'] == 1
        assert response.json()['data'] != []
        schema = path('delayed_users.json')
        with open(schema) as file:
            f = file.read()
            validate(response.json(), schema=json.loads(f))
