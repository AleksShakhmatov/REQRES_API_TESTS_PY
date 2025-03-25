import json
import requests
from allure_commons.types import Severity, AttachmentType
from jsonschema import validate
from path import path
import allure


@allure.tag("api")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "AleksSH")
@allure.feature("Создание пользователя")
@allure.story("Успешное создание пользователя")
def test_post_create_user(base_url):
    endpoint = '/api/users'
    url = base_url + endpoint
    data = {"name": "morpheus", "job": "leader"}
    schema = path('create_user.json')

    with allure.step(f"Выполнить POST запрос к {url} с данными: {data}"):
        response = requests.post(url, data=data)
        body = response.json()
        allure.attach(
            body=str(response),
            name="response",
            attachment_type=AttachmentType.TEXT
        )

    with allure.step('Проверить статус код'):
        assert response.status_code == 201, f"Ожидался статус код 201, получен {response.status_code}"

    with allure.step('Проверить значения в ответе'):
        response_json = response.json()
        assert response_json['name'] == 'morpheus', f"Ожидалось имя 'morpheus', получено {response_json['name']}"
        assert response_json['job'] == 'leader', f"Ожидалась должность 'leader', получена {response_json['job']}"
        assert response_json['id'] != '', "Поле id не должно быть пустым"
        assert response_json['createdAt'] != '', "Поле createdAt не должно быть пустым"

    with allure.step('Проверить схему ответа'):
        with open(schema) as file:
            f = file.read()
            validate(body, schema=json.loads(f))