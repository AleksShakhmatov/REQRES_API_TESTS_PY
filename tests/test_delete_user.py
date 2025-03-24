import requests
import allure
from allure_commons.types import Severity


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "AleksSH")
@allure.feature("")
@allure.story("")
def test_delete_user(base_url):
    response = requests.delete(base_url + '/api/users', params='page=2')

    with allure.step('Проверить'):
        assert response.status_code == 204
        assert response.text == ''
