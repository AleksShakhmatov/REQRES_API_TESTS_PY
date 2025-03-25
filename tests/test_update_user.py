import requests
import allure
import json
from allure_commons.types import Severity, AttachmentType
from jsonschema import validate
from path import path


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "AleksSH")
@allure.feature("Обновление пользователя")
@allure.story("Успешное обновление пользователя")
def test_update_user(base_url):
    endpoint = '/api/users/2'
    url = base_url + endpoint
    data = {"name": "morpheus", "job": "zion resident"}
    schema = path('update_user.json')

    with allure.step(f"Выполнить PUT запрос к {url} с данными: {data}"):
        response = requests.put(url, data=data)
        body = response.json()
        allure.attach(
            body=str(response),
            name="response",
            attachment_type=AttachmentType.TEXT
        )
    with allure.step('Проверить статус код'):
        assert response.status_code == 200, f"Ожидался статус код 200, получен {response.status_code}"

    with allure.step('Проверить значения в ответе'):
        response_json = response.json()
        assert response_json[
                   'job'] == 'zion resident', f"Ожидалась должность 'zion resident', получена {response_json['job']}"
        assert response_json['updatedAt'] != '', "Поле updatedAt не должно быть пустым"

    with allure.step('Проверить схему ответа'):
        with open(schema) as file:
            f = file.read()
            validate(body, schema=json.loads(f))
