import json
import requests
from jsonschema import validate
from pathlib import Path
import allure


@allure.tag('API')
@allure.feature('API')
@allure.story('Get user info')
@allure.title('Get existing user info')
@allure.link('https://reqres.in/')
def test_post_register_unsuccessful(base_url):
    endpoint = '/api/register'
    url = base_url + endpoint
    data = {"email": "sydney@fife"}
    schema = Path('register_unsuccessful.json')

    with allure.step(f"Выполнить POST запрос к {url} с данными: {data}"):
        response = requests.post(url, data=data)
        allure.attach(
            body=str(response.content),
            name="Response Content",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step('Проверить статус код'):
        assert response.status_code == 400, f"Ожидался статус код 400, получен {response.status_code}"

    with allure.step('Проверить тело ответа'):
        response_json = response.json()
        assert response_json['error'] == 'Missing password', (f"Ожидалось сообщение об ошибке 'Missing password', "
                                                              f"получено {response_json['error']}")

    with allure.step('Проверить схему ответа'):
        try:
            with open(schema, 'r') as file:
                schema_json = json.load(file)
            response_json = response.json()
            validate(response_json, schema_json)
        except Exception as e:
            allure.attach(
                body=str(e),
                name="Schema Validation Error",
                attachment_type=allure.attachment_type.TEXT
            )
