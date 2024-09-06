import allure
from scooter_api import ScooterApi
import response_message


class TestGetListOrders:
    @allure.title('Получение списка заказов :/api/v1/orders')
    def test_get_list_orders(self):
        response = ScooterApi.get_orders()
        assert response.status_code == 200 and response_message.SUCCESSFUL_GET_ORDER_LIST in response.json()
