import requests
import allure
import json
from jsonschema import validate
from pathlib import Path


def test_update_user(base_url):
    endpoint = '/api/users/2'
    url = base_url + endpoint
    data = {"name": "morpheus", "job": "zion resident"}
    schema = Path('update_user.json')

    with allure.step(f"Выполнить PUT запрос к {url} с данными: {data}"):
        response = requests.put(url, data=data)
        allure.attach(
            body=str(response.content),
            name="Response Content",
            attachment_type=allure.attachment_type.TEXT
        )
    with allure.step('Проверить статус код'):
        assert response.status_code == 200, f"Ожидался статус код 200, получен {response.status_code}"

    with allure.step('Проверить значения в ответе'):
        response_json = response.json()
        assert response_json[
                   'job'] == 'zion resident', f"Ожидалась должность 'zion resident', получена {response_json['job']}"
        assert response_json['updatedAt'] != '', "Поле updatedAt не должно быть пустым"

    with allure.step('Проверить схему ответа'):
        try:
            with open(schema, 'r') as file:
                schema_json = json.load(file)
            validate(response_json, schema_json)
        except Exception as e:
            allure.attach(
                body=str(e),
                name="Schema Validation",
                attachment_type=allure.attachment_type.TEXT
            )
