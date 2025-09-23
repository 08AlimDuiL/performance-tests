"""
Создать несколько Pydantic-моделей для описания запроса и ответа на эндпоинт POST /api/v1/users, который используется
для создания пользователей.
"""
from pydantic import BaseModel, EmailStr, Field
import uuid


class BaseUserSchema(BaseModel):
    """
    Базовая схема пользователя, содержащая общие поля.

    Attributes:
        email: Электронная почта пользователя
        lastName: Фамилия пользователя
        firstName: Имя пользователя
        middleName: Отчество пользователя
        phoneNumber: Номер телефона пользователя
    """
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class UserSchema(BaseUserSchema):
    """
    Схема данных пользователя, включая идентификатор.

    Attributes:
        id: Уникальный идентификатор пользователя
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))


class CreateUserRequestSchema(BaseUserSchema):
    """
    Схема запроса на создание пользователя.

    Содержит все необходимые данные для регистрации нового пользователя.
    Наследует все поля из BaseUserSchema.
    """
    pass


class CreateUserResponseSchema(BaseModel):
    """
    Схема ответа после успешного создания пользователя.

    Attributes:
        user: Объект с данными созданного пользователя
    """
    user: UserSchema
