import requests
import allure
from allure_commons.types import Severity


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "AleksSH")
@allure.feature("")
@allure.story("")
def test_get_not_found_user(base_url):
    response = requests.get(base_url + '/api/users/23')

    with allure.step('Проверить'):
        assert response.status_code == 404
        assert response.json() == {}
