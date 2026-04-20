import pytest
import allure
from api.api_create_orders import CreateOrder

class TestCreateOrder:

    @pytest.mark.parametrize('color', [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GREY'],
        None
    ])
    @allure.title('Возможность создания заказа с разными вариантами цвета')
    def test_create_order_with_different_colors(self, color):
        order = CreateOrder()
        
        status_code = order.get_status_code(
            "Naruto",
            "Uchiha",
            "Konoha, 142 apt.",
            4,
            "+7 800 355 35 35",
            5,
            "2020-06-06",
            "Saske, come back to Konoha",
            color
        )
        
        assert status_code == 201

    @allure.title('Проверка на содержании в теле ответа слова track')
    def test_response_contains_track(self):
        create_order = CreateOrder()
        
        response_body = create_order.get_response_body(
            "Naruto",
            "Uchiha",
            "Konoha, 142 apt.",
            4,
            "+7 800 355 35 35",
            5,
            "2020-06-06",
            "Saske, come back to Konoha",
            ["BLACK"]
        )
        
        assert 'track' in response_body