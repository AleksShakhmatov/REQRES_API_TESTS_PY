import json
import requests
from allure_commons.types import Severity, AttachmentType
from jsonschema import validate
from path import path
import allure


@allure.tag("api")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "AleksSH")
@allure.feature("Получение пользователей")
@allure.story("Получение списка пользователей с задержкой")
def test_get_delayed_response(base_url):
    endpoint = '/api/users'
    params = {'delay': 2}
    url = base_url + endpoint
    schema = path('delayed_users.json')

    with allure.step(f"Выполнить GET запрос к {url} с параметрами: {params}"):
        response = requests.get(url, params=params)
        body = response.json()
        allure.attach(
            body=str(response.content),
            name="Response Content",
            attachment_type=AttachmentType.TEXT
        )

    with allure.step('Проверить статус код'):
        assert response.status_code == 200, f"Ожидался статус код 200, получен {response.status_code}"

    with allure.step('Проверить значения в ответе'):
        response_json = response.json()
        assert response_json['page'] == 1, f"Ожидалась страница 1, получено {response_json['page']}"
        assert response_json['data'] != [], "Поле data не должно быть пустым"

    with allure.step('Проверить схему ответа'):
        with open(schema) as file:
            f = file.read()
            validate(body, schema=json.loads(f))
