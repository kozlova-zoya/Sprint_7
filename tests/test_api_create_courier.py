
import pytest
import allure 
from api.api_create_courier import CreateCourier
from conftest import generate_random_string


class TestCreateCourier:

    @allure.title('Успешное создание курьера') 
    @allure.description('При создании курьера со сгенерированными данными проверяется, что статус код 201,  т.е в тесте проверка уже на наличие всех данных, что говорит об успешном создании')
    def test_create_courier_success(self):

        courier = CreateCourier()
        result = courier.create_courier()
        

        assert len(result) == 3
        assert result[0] is not None
        assert result[1] is not None
        assert result[2] is not None


    @allure.title('Ошибка 409 Conflict и текст об ошибке при повторном использовании логина(при создании идентичного курьера)') 
    def test_create_two_identical_courier_returns_error_409(self):
        courier = CreateCourier()
        
        status_code, error_message = courier.create_two_identical_couriers()

        assert status_code == 409
        assert error_message == "Этот логин уже используется"


    @pytest.mark.parametrize(
    "login,password,firstName",
    [    
        ('test_login2', '', 'Test Name'),     
        ('', 'pass123', 'Test Name')          
    ]
    )
    @allure.title('Создание курьера без логина или пароля')
    def test_create_courier_missing_required_field_returns_error_400(self, login, password, firstName):
        courier = CreateCourier()
        status_code, error_message = courier.get_full_response(login, password, firstName)
        
        assert status_code == 400
        assert error_message == "Недостаточно данных для создания учетной записи"

    @allure.title('Запрос возвращает правильный код ответа при успешном создании курьера')
    def test_create_courier_returns_201_status_code(self):
        courier = CreateCourier()
    
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
  
        status_code = courier.get_status_code(login, password, first_name)
        
        assert status_code == 201

    @allure.title('Успешный запрос возвращает {"ok": True}')
    def test_create_courier_returns_ok(self):
        courier = CreateCourier()
        
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        
        response_body = courier.get_message(login, password, first_name)
    
        assert response_body == {"ok": True}