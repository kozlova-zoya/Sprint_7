import requests
import allure

class CreateOrder:
    def __init__(self, base_url='https://qa-scooter.praktikum-services.ru'):
        self.base_url = base_url
        self.orders_endpoint = '/api/v1/orders'

    @allure.step('Создание заказа с заданными параметрами')
    def create_order(self, first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment, color=None):
        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment
        }
        if color is not None:
            payload["color"] = color

        response = requests.post(f'{self.base_url}{self.orders_endpoint}', json=payload)
        return response

    @allure.step('Получение статус кода при создании заказа')
    def get_status_code(self, first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment, color=None):
        response = self.create_order(first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment, color)
        return response.status_code

    @allure.step('Получение тела ответа')
    def get_response_body(self, first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment, color=None):

        response = self.create_order(first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment, color)
        return response.json()