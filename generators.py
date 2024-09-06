from faker import Faker

fake = Faker()


def generated_login():
    generated_login = fake.user_name()
    return generated_login


def generated_password():
    generated_password = fake.random_number(5)
    return generated_password


def generated_firstname():
    generated_firstname = fake.first_name()
    return generated_firstname
