'''
В этом задании вы самостоятельно напишете Python-скрипт, который будет взаимодействовать с двумя эндпоинтами тестового
стенда через библиотеку HTTPX. Это поможет вам закрепить знания по работе с HTTP API и понять, как последовательно
выполнять связанные запросы

Цель задания:
Реализовать скрипт, который:
1. Создаёт пользователя через эндпоинт POST /api/v1/cards сервиса http-gateway
2. Создаёт депозитный счёт для этого пользователя через эндпоинт POST /api/v1/accounts/open-deposit-account
3. Выводит в консоль:
    JSON-ответ от сервера с данными о созданном счёте
    Статус-код ответа от сервера
'''

import time
import random
from faker import Faker
import httpx

fake = Faker('ru_RU')

# Инициализируем JSON-данные, которые будем отправлять в API
payload = {
    "email": f"user.{time.time()}_{random.randint(1000, 9999)}@example.com",
    "lastName": fake.last_name(),
    "firstName": fake.first_name(),
    "middleName": fake.middle_name(),
    "phoneNumber": fake.phone_number()
}

# Выполняем POST-запрос к эндпоинту /api/v1/cards
response = httpx.post("http://localhost:8003/api/v1/users", json=payload)

user_id=None
if response.status_code == 200:
    user_id = response.json().get('user').get('id')

payload_user_id = {
    "userId": user_id
}

response = httpx.post("http://localhost:8003/api/v1/accounts/open-deposit-account", json=payload_user_id)

print(response.json())
print(response.status_code)