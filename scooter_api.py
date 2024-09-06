import requests

import urls


class ScooterApi:
    @staticmethod
    def registration(body):
        return requests.post(urls.BASE_URL + urls.REGISTRATION_ENDPOINT, json=body)

    @staticmethod
    def login(body):
        return requests.post(urls.BASE_URL + urls.LOGIN_ENDPOINT, json=body)

    @staticmethod
    def add_order(body):
        return requests.post(urls.BASE_URL + urls.ADD_ORDER_ENDPOINT, json=body)

    @staticmethod
    def get_orders():
        return requests.get(urls.BASE_URL + urls.GET_ORDER_ENDPOINT)

    @staticmethod
    def delete_order(body):
        return requests.put(f'{urls.BASE_URL}{urls.DELETE_ORDER_ENDPOINT}{body}')

    @staticmethod
    def get_track_id(response):
        return response.json()['track']
