import allure
import pytest

import response_message

from data import Data
from scooter_api import ScooterApi


class TestNewCourier:
    @allure.title('Можно создать курьера. :/api/vi/courier')
    def test_creation_new_courier_success(self, data_courier):
        response = ScooterApi.registration(data_courier[0])
        assert response.status_code == 201 and response.json() == response_message.SUCCESSFUL_ADD_NEW_COURIER

    @allure.title('Нельзя создать двух одинаковых курьеров. :/api/vi/courier')
    def test_cannot_create_two_identical_couriers(self, creat_courier):
        response = ScooterApi.registration(creat_courier[0])
        assert response.status_code == 409 and response.json() == response_message.CANNOT_CREATE_TWO_IDENTICAL_COURIER

    @allure.title('Для создания курьера, нужно передать в ручку все обязательные поля :/api/vi/courier')
    @pytest.mark.parametrize('data', Data.DATA_FOR_REG)
    def test_mandatory_fields(self, data):
        response = ScooterApi.registration(data)
        assert response.status_code == 400 and response.json() == response_message.MANDATORY_FIELDS
