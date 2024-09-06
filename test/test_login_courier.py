import allure

import response_message
from data import Data

from scooter_api import ScooterApi


class TestLoginCourier:

    @allure.title('Курьер может авторизоваться, Успешный запрос возвращает id :/api/v1/courier/login')
    def test_login_successful(self, creat_courier):
        response = ScooterApi.login(creat_courier[1])
        response_message = response.json()
        assert response.status_code == 200 and 'id' in response_message

    @allure.title('Для авторизации нужно передать все обязательные поля :/api/v1/courier/login')
    def test_courier_login_with_no_password(self, creat_courier):
        login_data = {'login': creat_courier[2], 'password': ''}
        response = ScooterApi.login(login_data)
        assert (response.status_code == 400 and response.json() ==
                response_message.THERE_IS_NOT_ENOUGH_DATA_TO_LOG_IN)

    @allure.title('Cистема вернёт ошибку, если неправильно указать логин или пароль :/api/v1/courier/login')
    def test_courier_login_with_no_login(self, creat_courier):
        login_data = {'login': '', 'password': creat_courier[3]}
        response = ScooterApi.login(login_data)
        assert (response.status_code == 400 and response.json() ==
                response_message.THERE_IS_NOT_ENOUGH_DATA_TO_LOG_IN)

    @allure.title('Eсли авторизоваться под несуществующим пользователем, запрос возвращает ошибку '
                  ':/api/v1/courier/login')
    def test_log_in_under_a_non_existent_user(self):
        response_login = ScooterApi.login(Data.UNREG_COURIER_DATA)
        assert (response_login.status_code == 404 and response_login.json() ==
                response_message.THE_ACCOUNT_WAS_NOT_FOUND)
