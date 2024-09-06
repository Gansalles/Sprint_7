import generators


class Data:
    DATA_FOR_REG = [{
        'password': generators.generated_password(), 'firstname': generators.generated_firstname()
    }, {'login': generators.generated_login(), 'firstname': generators.generated_firstname()}]

    UNREG_COURIER_DATA = {"login": generators.generated_login(), "password": generators.generated_password()}


class OrderData:
    ORDER_DATA = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }

    COLORS = [['BLACK'], ['GREY'], (['BLACK'], ['GREY']), ['']]
