'''
Что должен делать скрипт:
    1. Создать пользователя. Выполнить POST-запрос на эндпоинт: POST /api/v1/users → Получить userId из ответа.
    2. Создать кредитный счёт для пользователя. Выполнить POST-запрос на эндпоинт:
        POST /api/v1/accounts/open-credit-card-account → Получить accountId и cardId из ответа
        (кредитный счёт создаётся с картой).
    Совершить операцию покупки (purchase). Выполнить POST-запрос: POST /api/v1/operations/make-purchase-operation.
        Передать следующие параметры в теле запроса:
            status: "IN_PROGRESS"
            amount: 77.99
            category: "taxi"
            cardId: (из ответа на шаге 2)
            accountId: (из ответа на шаге 2)
        → Получить operationId из ответа.
    Получить чек по операции. Выполнить GET-запрос:
        GET /api/v1/operations/operation-receipt/{operation_id}
        → Распечатать JSON-ответ с данными чека в консоль.
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

# 1. Выполняем POST-запрос к эндпоинту /api/v1/users
response = httpx.post("http://localhost:8003/api/v1/users", json=payload)

user_id = None
if response.status_code == 200:
    user_id = response.json().get('user').get('id')

payload_open_credit_card_account = {
    "userId": user_id
}
# 2. Выполняем POST-запрос на эндпоинт /api/v1/accounts/open-credit-card-account
response = (httpx.post
    (
    "http://localhost:8003/api/v1/accounts/open-credit-card-account",
    json=payload_open_credit_card_account
))

account_id = None
card_id = None

if response.status_code == 200:
    # Парсим JSON-ответ ОДИН раз
    data = response.json()

    # Извлекаем account_id
    account_id = data.get('account', {}).get('id')  # Используем {} для защиты, если 'account' нет

    # Извлекаем card_id
    # 1. Обращаемся к списку 'cards' внутри 'account'
    # 2. Берем ПЕРВЫЙ элемент этого списка [0]
    # 3. Из этого элемента (словаря) получаем 'id'
    cards_list = data.get('account', {}).get('cards', [])  # Получаем список карт или пустой список, если его нет

    if cards_list:  # Если список не пустой
        card_id = cards_list[0].get('id')  # Берем id первой карты в списке
    else:
        card_id = None  # Если карт нет, устанавливаем card_id в None

# 3 Выполняем POST-запрос к эндпоинту /api/v1/operations/make-purchase-operation

payload_make_purchase_operation = {
    "status": "IN_PROGRESS",
    "amount": 77.99,
    "cardId": card_id,
    "accountId": account_id,
    "category": "taxi"
}

response = (httpx.post
    (
    "http://localhost:8003/api/v1/operations/make-purchase-operation",
    json=payload_make_purchase_operation
))

operation_id = None
if response.status_code == 200:
    operation_id = response.json().get('operation', {}).get('id')

# 4 Выполняем GET-запрос с ендпоинтом /api/v1/operations/operation-receipt/{operation_id}
response = (httpx.get
    (
    "http://localhost:8003/api/v1/operations/operation-receipt/" + str(operation_id),
))

print(response.json())