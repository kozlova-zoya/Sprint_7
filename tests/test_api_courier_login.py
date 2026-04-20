import pytest
import allure
from api.api_courier_login import CourierLogin
from conftest import register_new_courier_and_return_login_password, generate_random_string


class TestCourierLogin:

    @allure.title('Проверка возможности авторизации курьера')
    def test_courier_can_login(self):
        courier_data = register_new_courier_and_return_login_password()
        login, password, first_name = courier_data
        
        courier_login = CourierLogin()
        status_code = courier_login.get_status_code(login, password)
        
        assert status_code == 200

    @allure.title('Проверка, что для авторизации нужно передать все обязательные поля')
    @allure.description('Если какого-то поля нет, запрос возвращает ошибку 400 Bad Request с сообщением в теле ответа "Недостаточно данных для входа"')
    @pytest.mark.parametrize(
        "login,password",
        [
            ('', 'password123'), 
            ('login123', ''),      
            ('', '')               
        ]
    )
    def test_login_missing_required_fields(self, login, password):
        courier_login = CourierLogin()
        response = courier_login.login_courier(login, password)
        status_code = response.status_code
        error_message = response.json()['message']
        
        assert status_code == 400
        assert error_message == "Недостаточно данных для входа"


    @allure.title('Система возвращает ошибку 404 Not Found при неправильном вводе пароля в процессе авторизации')
    @allure.description('Создаем курьера и при авторизации указываем неправильный пароль')
    def test_login_with_wrong_password(self):

        courier_data = register_new_courier_and_return_login_password()
        login, password, first_name = courier_data
        
        courier_login = CourierLogin()
        
        response = courier_login.login_courier(login, 'wrong_password')
        status_code = response.status_code
        error_message = response.json()['message']
        
        assert status_code == 404
        assert error_message == "Учетная запись не найдена"

    @allure.title('Система возвращает ошибку 404 Not Found при неправильном вводе логина в процессе авторизации')
    @allure.description('Создаем курьера и при авторизации указываем неправильный пароль')
    def test_login_with_wrong_login(self):

        courier_data = register_new_courier_and_return_login_password()
        login, password, first_name = courier_data
        
        courier_login = CourierLogin()
        
        response = courier_login.login_courier('wrong_login', password)
        status_code = response.status_code
        error_message = response.json()['message']
        
        assert status_code == 404
        assert error_message == "Учетная запись не найдена"

    @allure.title('Авторизация под несуществующим пользователем возвращает ошибку 404 Not Found')
    def test_login_unregistered_user(self):

        courier_login = CourierLogin()
        
        login = generate_random_string(10)
        password = generate_random_string(10)
        
        response = courier_login.login_courier(login, password)
        status_code = response.status_code
        error_message = response.json()['message']
        
        assert status_code == 404
        assert error_message == "Учетная запись не найдена"


    @allure.title('Успешный запрос на авторизацию возвращает id пользователя в теле ответа')
    def test_successful_login_returns_user_id(self):
        courier_data = register_new_courier_and_return_login_password()
        login, password, first_name = courier_data
        
        courier_login = CourierLogin()
        courier_id = courier_login.get_courier_id(login, password)
        
        assert courier_id > 0



