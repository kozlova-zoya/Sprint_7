import requests
import allure
from conftest import register_new_courier_and_return_login_password

class CreateCourier:

    def __init__(self, base_url='https://qa-scooter.praktikum-services.ru'):
        self.base_url = base_url
        self.courier_endpoint = '/api/v1/courier'

    @allure.step('Создание курьера')
    def create_courier(self):
        return register_new_courier_and_return_login_password()

    @allure.step('Создание двух одинаковых курьеров')
    def create_two_identical_couriers(self):
        courier_data = register_new_courier_and_return_login_password()

        login, password, first_name = courier_data
        payload = {"login": login, "password": password, "firstName": first_name}
        
        response_2 = requests.post(f'{self.base_url}{self.courier_endpoint}', data=payload)

        error_message = response_2.json()['message']
        
        return response_2.status_code, error_message
    
    @allure.step('Создание курьера с заданными данными')
    def create_courier_with_data(self, login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return requests.post(f'{self.base_url}{self.courier_endpoint}', data=payload)
    
    @allure.step('Получение полного тела ответа')
    def get_full_response(self, login, password, first_name):
        response = self.create_courier_with_data(login, password, first_name)
        return response.status_code, response.json()['message']
    
    @allure.step('Получение статус кода при создании курьера')
    def get_status_code(self, login, password, first_name):
        response = self.create_courier_with_data(login, password, first_name)
        return response.status_code
    
    @allure.step('Получение сообщения при создании курьера')
    def get_message(self, login, password, first_name):
        response = self.create_courier_with_data(login, password, first_name)
        return response.json()

