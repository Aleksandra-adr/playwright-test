import allure
import requests
from requests.auth import HTTPBasicAuth

@allure.feature("Basic Auth API")
@allure.story("Проверка авторизации через HTTP")
@allure.title("Успешная авторизация с валидными данными")
@allure.severity(allure.severity_level.CRITICAL)

def test_basic_auth_api():
    url = "https://the-internet.herokuapp.com/basic_auth"

    with allure.step("Отправка Get - запроса с валидным логином/паролем"):
        response = requests.get(url, auth=HTTPBasicAuth('admin', "admin"))

    with allure.step("Проверка статус кода - 200"):
        assert response.status_code == 200

    with allure.step('Проверка наличия текста "Congratulations" в ответа'):
        assert "Congratulations" in response.text


@allure.feature("Basic Auth API")
@allure.story("Отрицательная проверка")
@allure.title("Негативная авторизация с неверными учетными данными")

def test_basic_auth_api_failure():
    url = "https://the-internet.herokuapp.com/basic_auth"

    with allure.step("Отправка Get- запроса с неверным паролем"):
        response = requests.get(url, auth=HTTPBasicAuth('admin', 'qwerty'))

    with allure.step("Проверка статус кода - 401"):
        assert response.status_code == 401


