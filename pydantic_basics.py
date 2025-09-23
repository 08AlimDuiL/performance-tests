'''
{
  "id": "string",
  "type": "UNSPECIFIED",
  "status": "UNSPECIFIED",
  "balance": 0
}


{
  "account": {
    "id": "string",
    "type": "UNSPECIFIED",
    "cards": [
      {
        "id": "string",
        "pin": "string",
        "cvv": "string",
        "type": "UNSPECIFIED",
class CardSchema(BaseModel):
    id: str = "card-id"
    pin: str = "1234"
    cvv: str = "123"
    type: str = "PHYSICAL"
    status: str = "ACTIVE"
    account_id: str = Field(alias="accountId", default="account-id")
    card_number: str = Field(alias="cardNumber", default="123412341234234")
    card_holder: str = Field(alias="cardHolder", default="Alise Smith")
    expiry_date: date = Field(alias="expiryDate", default=date(2027, 3, 25))
    payment_system: str = Field(alias="paymentSystem", default="VISA")


# Создадим объект модели без передачи параметров
card = CardSchema()
print(card)
        "status": "UNSPECIFIED",
        "accountId": "string",
        "cardNumber": "string",
        "cardHolder": "string",
        "expiryDate": "2025-06-08",
        "paymentSystem": "UNSPECIFIED"
      }
    ],
    "status": "UNSPECIFIED",
    "balance": 0
  }
}
'''

from pydantic import BaseModel, Field, ConfigDict, EmailStr, HttpUrl, ValidationError
import json
from datetime import date
from pydantic.alias_generators import to_camel
import uuid


class AccountSchema(
    BaseModel):  # BaseModel —  это базовый класс, от которого наследуются все модели Pydantic. Он предоставляет встроенную валидацию данных, сериализацию и десериализацию.
    id: str
    type: str
    status: str
    balance: float


# Инициализируем модель AccountSchema через передачу аргументов
account_default_model = AccountSchema(
    id="account-id",
    type="CREDIT_CARD",
    status="ACTIVE",
    balance=100.57,
)
print('Account default model:', account_default_model)
print('-' * 80)

# Инициализируем модель AccountSchema через JSON
account_json = """
{
    "id": "account-id",
    "type": "CREDIT_CARD",
    "status": "ACTIVE",
    "balance": 777.11
}
"""
account_json_model = AccountSchema.model_validate_json(account_json)
print('Account JSON model:', account_json_model)
print('-' * 80)


# Добавили модель CardSchema
class CardSchema(BaseModel):
    id: str
    pin: str
    cvv: str
    type: str
    status: str
    accountId: str
    cardNumber: str
    cardHolder: str
    expiryDate: date
    paymentSystem: str


class AccountSchema(BaseModel):
    id: str
    type: str
    # Вложенный объект для списка карт привязанных к счету
    cards: list[CardSchema]
    status: str
    balance: float


# Инициализируем модель AccountSchema через передачу аргументов
account_default_model = AccountSchema(
    id="account-id",
    type="CREDIT_CARD",
    # Добавили инициализацию списка вложенных моделей CardSchema
    cards=[
        CardSchema(
            id="card-id",
            pin="1234",
            cvv="123",
            type="PHYSICAL",
            status="ACTIVE",
            accountId="account-id",
            cardNumber="1234123412341234",
            cardHolder="Alise Smith",
            expiryDate=date(2027, 3, 25),
            paymentSystem="VISA"
        )
    ],
    status="ACTIVE",
    balance=100.57,
)
print('Account default model:', account_default_model)
print('-' * 80)

# Инициализируем модель AccountSchema через распаковку словаря
account_dict = {
    "id": "account-id",
    "type": "CREDIT_CARD",
    # Добавили ключ cards
    "cards": [
        {
            "id": "card-id",
            "pin": "1234",
            "cvv": "123",
            "type": "PHYSICAL",
            "status": "ACTIVE",
            "accountId": "account-id",
            "cardNumber": "1234123412341234",
            "cardHolder": "Alise Smith",
            "expiryDate": "2027-03-25",
            "paymentSystem": "VISA"
        }
    ],
    "status": "ACTIVE",
    "balance": 777.11,
}
account_dict_model = AccountSchema(**account_dict)
print('Account dict model:', account_dict_model)
print('-' * 80)

# Инициализируем модель AccountSchema через JSON
account_json = """
{
    "id": "account-id",
    "type": "CREDIT_CARD",
    "cards": [
        {
            "id": "card-id",
            "pin": "1234",
            "cvv": "123",
            "type": "PHYSICAL",
            "status": "ACTIVE",
            "accountId": "account-id",
            "cardNumber": "1234123412341234",
            "cardHolder": "Alise Smith",
            "expiryDate": "2027-03-25",
            "paymentSystem": "VISA"
        }
    ],
    "status": "ACTIVE",
    "balance": 777.11
}
"""
account_json_model = AccountSchema.model_validate_json(account_json)
print('Account JSON model:', account_json_model)
print('-' * 80)


class CardSchema(BaseModel):
    id: str
    pin: str
    cvv: str
    type: str
    status: str
    account_id: str = Field(alias="accountId")  # Используем alias
    card_number: str = Field(alias="cardNumber")  # Используем alias
    card_holder: str = Field(alias="cardHolder")  # Используем alias
    expiry_date: date = Field(alias="expiryDate")  # Используем alias
    payment_system: str = Field(alias="paymentSystem")  # Используем alias


class AccountSchema(BaseModel):
    id: str
    type: str
    cards: list[CardSchema]
    status: str
    balance: float


class CardSchema(BaseModel):
    # Автоматическое преобразование snake_case → camelCase
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str
    pin: str
    cvv: str
    type: str
    status: str
    account_id: str
    card_number: str
    card_holder: str
    expiry_date: date
    payment_system: str


class AccountSchema(BaseModel):
    id: str
    type: str
    cards: list[CardSchema]
    status: str
    balance: float


account_data = {
    "id": "account-id",
    "type": "CREDIT_CARD",
    "cards": [
        {
            "id": "card-id",
            "pin": "1234",
            "cvv": "123",
            "type": "PHYSICAL",
            "status": "ACTIVE",
            "accountId": "account-id",
            "cardNumber": "1234123412341234",
            "cardHolder": "Alise Smith",
            "expiryDate": "2027-03-25",
            "paymentSystem": "VISA"
        }
    ],
    "status": "ACTIVE",
    "balance": 777.11,
}
account_model = AccountSchema(**account_data)
print(account_model.model_dump(by_alias=True))
print('-' * 80)


class CardSchema(BaseModel):
    id: str = "card-id"
    pin: str = "1234"
    cvv: str = "123"
    type: str = "PHYSICAL"
    status: str = "ACTIVE"
    account_id: str = Field(alias="accountId", default="account-id")
    card_number: str = Field(alias="cardNumber", default="123412341234234")
    card_holder: str = Field(alias="cardHolder", default="Alise Smith")
    expiry_date: date = Field(alias="expiryDate", default=date(2027, 3, 25))
    payment_system: str = Field(alias="paymentSystem", default="VISA")


# Создадим объект модели без передачи параметров
card = CardSchema()
print(card)
print('-' * 80)


class AccountSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    type: str = "CREDIT_CARD"
    cards: list[CardSchema] = Field(default_factory=list)
    status: str = "ACTIVE"
    balance: float = 25000


# Создадим несколько объектов модели
account1 = AccountSchema()
account2 = AccountSchema()

print(account1.id)
print(account2.id)
print('-' * 80)


class AccountSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    type: str = "CREDIT_CARD"
    cards: list[CardSchema] = []
    status: str = "ACTIVE"
    balance: float = 25000

    def get_account_name(self) -> str:
        return f"{self.status}:{self.type}"


# Добавили модель DocumentSchema
class DocumentSchema(BaseModel):
    url: HttpUrl  # Используем HttpUrl вместо str
    document: str


# Добавили модель UserSchema
class UserSchema(BaseModel):
    id: str
    email: EmailStr  # Используем EmailStr вместо str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


# -----------------------------------------------------------------------------------------------------------------------

# Добавили модель DocumentSchema
class DocumentSchema(BaseModel):
    url: HttpUrl  # Используем HttpUrl вместо str
    document: str


# Добавили модель UserSchema
class UserSchema(BaseModel):
    id: str
    email: EmailStr  # Используем EmailStr вместо str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


# Добавили модель CardSchema
class CardSchema(BaseModel):
    id: str = "card-id"
    pin: str = "1234"
    cvv: str = "123"
    type: str = "PHYSICAL"
    status: str = "ACTIVE"
    account_id: str = Field(alias="accountId", default="account-id")
    card_number: str = Field(alias="cardNumber", default="123412341234234")
    card_holder: str = Field(alias="cardHolder", default="Alise Smith")
    expiry_date: date = Field(alias="expiryDate", default=date(2027, 3, 25))
    payment_system: str = Field(alias="paymentSystem", default="VISA")


class AccountSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    type: str = "CREDIT_CARD"
    # Вложенный объект для списка карт привязанных к счету
    cards: list[CardSchema] = Field(default_factory=list)
    status: str = "ACTIVE"
    balance: float = 25000

    def get_account_name(self) -> str:
        return f"{self.status}:{self.type}"


# Инициализируем модель AccountSchema через передачу аргументов
account_default_model = AccountSchema(
    id="account-id",
    type="CREDIT_CARD",
    # Добавили инициализацию списка вложенных моделей CardSchema
    cards=[
        CardSchema(
            id="card-id",
            pin="1234",
            cvv="123",
            type="PHYSICAL",
            status="ACTIVE",
            accountId="account-id",
            cardNumber="1234123412341234",
            cardHolder="Alise Smith",
            expiryDate=date(2027, 3, 25),
            paymentSystem="VISA"
        )
    ],
    status="ACTIVE",
    balance=100.57,
)
print('Account default model:', account_default_model)

# Инициализируем модель AccountSchema через распаковку словаря
account_dict = {
    "id": "account-id",
    "type": "CREDIT_CARD",
    # Добавили ключ cards
    "cards": [
        {
            "id": "card-id",
            "pin": "1234",
            "cvv": "123",
            "type": "PHYSICAL",
            "status": "ACTIVE",
            "accountId": "account-id",
            "cardNumber": "1234123412341234",
            "cardHolder": "Alise Smith",
            "expiryDate": "2027-03-25",
            "paymentSystem": "VISA"
        }
    ],
    "status": "ACTIVE",
    "balance": 777.11,
}
account_dict_model = AccountSchema(**account_dict)
print('Account dict model:', account_dict_model)

# Инициализируем модель AccountSchema через JSON
account_json = """
{
    "id": "account-id",
    "type": "CREDIT_CARD",
    "cards": [
        {
            "id": "card-id",
            "pin": "1234",
            "cvv": "123",
            "type": "PHYSICAL",
            "status": "ACTIVE",
            "accountId": "account-id",
            "cardNumber": "1234123412341234",
            "cardHolder": "Alise Smith",
            "expiryDate": "2027-03-25",
            "paymentSystem": "VISA"
        }
    ],
    "status": "ACTIVE",
    "balance": 777.11
}
"""
account_json_model = AccountSchema.model_validate_json(account_json)
print('Account JSON model:', account_json_model)

try:
    tariff = DocumentSchema(
        url="localhost",
        document="document-data",
    )
except ValidationError as error:
    print(error)
    print(error.errors())
