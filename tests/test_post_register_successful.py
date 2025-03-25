import json
import allure
import requests
from allure_commons.types import Severity, AttachmentType
from jsonschema import validate
from path import path


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "AleksSH")
@allure.feature("Регистрация пользователя")
@allure.story("Успешная регистрация пользователя")
def test_post_register_successful(base_url):
    endpoint = '/api/register'
    url = base_url + endpoint
    data = {"email": "eve.holt@reqres.in", "password": "pistol"}
    schema = path('register_successful.json')

    with allure.step(f"Выполнить POST запрос к {url} с данными: {data}"):
        response = requests.post(url, data=data)
        body = response.json()
        allure.attach(
            body=str(response.content),
            name="Response Content",
            attachment_type=AttachmentType.TEXT
        )

    with allure.step('Проверить статус код'):
        assert response.status_code == 200, f"Ожидался статус код 200, получен {response.status_code}"

    with allure.step('Проверить тело ответа'):
        response_json = response.json()
        assert response_json['id'] != '', "Поле id не должно быть пустым"
        assert response_json['token'] != '', "Поле token не должно быть пустым"

    with allure.step('Проверить схему ответа'):
        with open(schema) as file:
            f = file.read()
            validate(body, schema=json.loads(f))
