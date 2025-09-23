from pydantic import BaseModel
'''
1. Используйте суффикс Schema, чтобы избежать конфликтов.
2. Давайте понятные названия моделям, отражающие их смысл.
3. Разделяйте краткие и полные версии моделей (ShortUserSchema, ExtendedUserSchema).
4. Не привязывайтесь к API-методу в названии модели, используйте CreateAccountRequestSchema, GetAccountResponseSchema.
5. Разбивайте модели по файлам (accounts/schema.py, users/schema.py).
6. Модели отвечают только за валидацию, а не за логику API-запросов.
7. Используйте наследование, чтобы избегать дублирования кода.
'''

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True  # Значение по умолчанию


user = User(id="123", name="Alice", email="alice@example.com")
print(user)  # 123 (автоматически преобразован в int)
print('-' * 80)


class Address(BaseModel):
    city: str
    zip_code: str


class User_1(BaseModel):
    id: int
    name: str
    address: Address  # Вложенная модель


user = User_1(id=1, name="Alice", address={"city": "New York", "zip_code": "10001"})
print(user.address.city)  # "New York"
print('-' * 80)
print(user.model_dump_json())  # Выводит JSON-строку
print('-' * 80)

from pydantic import BaseModel


class CardSchema(BaseModel):
    id: str
    pin: str
    cvv: str
    type: str
    status: str
    account_id: str
    card_number: str
    card_holder: str
    expiry_date: str
    payment_system: str


class ShortAccountSchema(BaseModel):
    id: str
    type: str


class FullAccountSchema(ShortAccountSchema):
    cards: list[CardSchema]
    status: str


class AccountSchema(BaseModel):
    id: str
    type: str
    cards: list[CardSchema]
    status: str
    balance: float


class ShortUserSchema(BaseModel):
    id: str
    email: str
    phone_number: str


class ExtendedUserSchema(ShortUserSchema):
    last_name: str
    first_name: str
    middle_name: str
