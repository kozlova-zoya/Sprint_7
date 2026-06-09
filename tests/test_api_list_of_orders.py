import allure
from api.api_list_of_orders import ListOfOrders
from api.api_create_courier import CreateCourier
from api.api_create_orders import CreateOrder


class TestListOfOrders:

    @allure.title('Запрос возвращает список заказов')
    def test_get_orders_returns_list(self):

        courier = CreateCourier()
        courier.create_courier()
        
        create_order = CreateOrder()
        create_order.create_order(
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
        
        orders = ListOfOrders()
        orders_list = orders.get_orders()
        
        assert len(orders_list) > 0