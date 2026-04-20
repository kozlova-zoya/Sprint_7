import requests
import allure


class CourierLogin:

    def __init__(self, base_url='https://qa-scooter.praktikum-services.ru'):
        self.base_url = base_url
        self.login_endpoint = '/api/v1/courier/login'

    @allure.step('Авторизация курьера с заданными данными')
    def login_courier(self, login, password):
        payload = {
            "login": login,
            "password": password
        }
        return requests.post(f'{self.base_url}{self.login_endpoint}', data=payload)

    @allure.step('Получение статус кода при авторизации')
    def get_status_code(self, login, password):
        response = self.login_courier(login, password)
        return response.status_code

    @allure.step('Получение сообщения об ошибке при авторизации')
    def get_error_message(self, login, password):
        response = self.login_courier(login, password)
        return response.json()['message']

    @allure.step('Получение id пользователя при успешной авторизации')
    def get_courier_id(self, login, password):
        response = self.login_courier(login, password)
        return response.json()['id']
    

    