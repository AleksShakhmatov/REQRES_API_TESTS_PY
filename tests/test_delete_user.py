import requests
import allure


def test_delete_user(base_url):
    response = requests.delete(base_url + '/api/users', params='page=2')

    with allure.step('Проверить'):
        assert response.status_code == 204
        assert response.text == ''
