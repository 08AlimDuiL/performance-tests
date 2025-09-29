from faker import Faker


fake = Faker()

print(fake.name())  # Выведет: John Doe
print(fake.address())  # Выведет: 1234 Elm St, Springfield, IL
print(fake.email())  # Выведет: j.doe@example.com
print('-' * 80)

fake = Faker('ru_RU')
print(fake.name())  # Выведет: Иван Иванов
print(fake.address())
print('-' * 80)

user_data = {
    "name": fake.name(),
    "email": fake.email(),
    "address": fake.address()
}

print(user_data)
print('-' * 80)

'''
from faker import Faker
import requests

fake = Faker()

# Генерация фейковых данных
user_data = {
    "name": fake.name(),
    "email": fake.email(),
    "age": fake.random_int(min=18, max=100)
}

# Отправка POST-запроса с фейковыми данными
response = requests.post("https://api.example.com/users", json=user_data)

# Проверка, что запрос прошел успешно
assert response.status_code == 201

'''
