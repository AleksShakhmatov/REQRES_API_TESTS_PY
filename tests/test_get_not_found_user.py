import requests
import allure
from allure_commons.types import Severity, AttachmentType


@allure.tag("api")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "AleksSH")
@allure.feature("Получение пользователя")
@allure.story("Попытка получения несуществующего пользователя")
def test_get_not_found_user(base_url):
    endpoint = '/api/users/23'
    url = base_url + endpoint

    with allure.step(f"Выполнить GET запрос к {url}"):
        response = requests.get(url)
        allure.attach(
            body=str(response),
            name="response",
            attachment_type=AttachmentType.TEXT
        )

    with allure.step('Проверить статус код'):
        assert response.status_code == 404, f"Ожидался статус код 404, получен {response.status_code}"

    with allure.step('Проверить тело ответа'):
        assert response.json() == {}, "Ожидалось пустое тело ответа"
