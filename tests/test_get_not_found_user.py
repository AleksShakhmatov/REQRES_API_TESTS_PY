import requests
import allure


@allure.tag('API')
@allure.feature('API')
@allure.story('Get user info')
@allure.title('Get existing user info')
@allure.link('https://reqres.in/')
def test_get_not_found_user(base_url):
    response = requests.get(base_url + '/api/users/23')

    with allure.step('Проверить'):
        assert response.status_code == 404
        assert response.json() == {}
