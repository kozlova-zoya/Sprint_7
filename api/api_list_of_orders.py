import requests
import allure

class ListOfOrders:
    def __init__(self, base_url='https://qa-scooter.praktikum-services.ru'):
        self.base_url = base_url
        self.orders_endpoint = '/api/v1/orders'

    @allure.step('Получение списка заказов')
    def get_orders(self):
        response = requests.get(f'{self.base_url}{self.orders_endpoint}')
        return response.json()['orders']