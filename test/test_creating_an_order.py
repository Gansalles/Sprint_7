import allure
import pytest

import response_message

from data import OrderData
from scooter_api import ScooterApi


class TestOrder:

    @allure.title("Тест на создание заказа с разными значениями colors :/api/v1/orders")
    @pytest.mark.parametrize('color', OrderData.COLORS)
    def test_add_order_with_different_colors(self, color):
        order_data = OrderData.ORDER_DATA
        order_data['color'] = color
        response = ScooterApi.add_order(order_data)
        assert response.status_code == 201 and response_message.SUCCESSFUL_ORDER_ADDING in response.json()
        ScooterApi.delete_order(ScooterApi.get_track_id(response))
