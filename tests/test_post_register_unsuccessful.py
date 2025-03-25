import json
import requests
from allure_commons.types import Severity
from jsonschema import validate
from path import path
import allure


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "AleksSH")
@allure.feature("Регистрация пользователя")
@allure.story("Неуспешная регистрация пользователя")
def test_post_register_unsuccessful(base_url):
    endpoint = '/api/register'
    url = base_url + endpoint
    data = {"email": "sydney@fife"}
    schema = path('register_unsuccessful.json')

    with allure.step(f"Выполнить POST запрос к {url} с данными: {data}"):
        response = requests.post(url, data=data)
        body = response.json()
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
        with open(schema) as file:
            f = file.read()
            validate(body, schema=json.loads(f))
