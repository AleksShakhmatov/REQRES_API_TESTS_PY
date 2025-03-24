import requests
import allure


@allure.tag('API')
@allure.feature('API')
@allure.story('Get user info')
@allure.title('Get existing user info')
@allure.link('https://reqres.in/')
def test_delete_user(base_url):
    response = requests.delete(base_url + '/api/users', params='page=2')

    with allure.step('Проверить'):
        assert response.status_code == 204
        assert response.text == ''
