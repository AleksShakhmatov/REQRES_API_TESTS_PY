import requests
import allure
from allure_commons.types import Severity, AttachmentType


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "AleksSH")
@allure.feature("Удаление пользователя")
@allure.story("Успешное удаление пользователя")
def test_delete_user(base_url):
    endpoint = '/api/users'
    params = {'page': 2}
    url = base_url + endpoint

    with allure.step(f"Выполнить DELETE запрос к {url} с параметрами: {params}"):
        response = requests.delete(url, params=params)
        allure.attach(
            body=str(response.content),
            name="Response Content",
            attachment_type=AttachmentType.TEXT
        )

    with allure.step('Проверить статус код'):
        assert response.status_code == 204, f"Ожидался статус код 204, получен {response.status_code}"

    with allure.step('Проверить тело ответа'):
        assert response.text == '', "Ожидалось пустое тело ответа"
