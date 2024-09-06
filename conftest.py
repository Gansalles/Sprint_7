import pytest
import requests

import generators
import urls


@pytest.fixture
def creat_courier():
    login = generators.generated_login()
    password = generators.generated_password()
    firstname = generators.generated_firstname()
    created_courier_body = {'login': login, 'password': password, 'firstname': firstname}
    login_courier_body = {'login': login, 'password': password}
    requests.post(f'{urls.BASE_URL}{urls.REGISTRATION_ENDPOINT}', json=created_courier_body)
    login_courier = requests.post(f'{urls.BASE_URL}{urls.LOGIN_ENDPOINT}', json=login_courier_body)
    yield [created_courier_body, login_courier_body, login, password]
    requests.delete(f'{urls.BASE_URL}{urls.DELETE_COURIER_ENDPOINT}{login_courier.json()["id"]}')


@pytest.fixture
def data_courier():
    login = generators.generated_login()
    password = generators.generated_password()
    firstname = generators.generated_firstname()
    created_courier_body = {'login': login, 'password': password, 'firstname': firstname}
    login_courier_body = {'login': login, 'password': password}
    yield [created_courier_body, login_courier_body]
    login_courier = requests.post(f'{urls.BASE_URL}{urls.LOGIN_ENDPOINT}', json=login_courier_body)
    requests.delete(f'{urls.BASE_URL}{urls.DELETE_COURIER_ENDPOINT}{login_courier.json()["id"]}')
