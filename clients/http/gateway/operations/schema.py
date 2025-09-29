from pydantic import BaseModel, Field, ConfigDict, HttpUrl
from enum import StrEnum


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationSchema(BaseModel):
    """
      Структура ответа с информацией об операции.
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class GetOperationsResponseSchema(BaseModel):
    operations: list[OperationSchema]


class OperationReceiptSchema(BaseModel):
    """
    Структура ответа с информацией о документе.
    """
    url: HttpUrl = Field(..., min_length=1, max_length=2083)
    document: str


class GetOperationReceiptResponseSchema(BaseModel):
    """
    Описание структуры ответа с информацией о документе.
    """
    receipt: OperationReceiptSchema


class OperationsSummarySchema(BaseModel):
    """
      Структура ответа с суммарной информацией.
    """
    model_config = ConfigDict(populate_by_name=True)

    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class GetOperationsQuerySchema(BaseModel):
    """
      Структура данных для получения списка операций определенного счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа получения списка операций определенного счета.
    """
    operation: OperationSchema


class GetOperationsSummaryQuerySchema(BaseModel):
    """
      Структура данных для получения статистики по операциям определенного счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationsSummaryResponseSchema(BaseModel):
    """
   Описание структуры ответа получения суммарных данных.
    """
    summary: OperationsSummarySchema


class MakeOperationRequestSchema(BaseModel):
    """
    Базовая структура данных для операций.
    Содержит общие поля для всех типов операций.

    :param status: Статус операции
    :param amount: Сумма операции
    :param cardId: Идентификатор карты
    :param accountId: Идентификатор счета
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus
    amount: float
    cardId: str
    account_id: str = Field(alias="accountId")


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции комиссии.
    """
    pass


class MakeFeeOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции пополнения.
    """
    pass


class MakeTopUpOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции кэшбэка.
    """
    pass


class MakeCashbackOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции перевода.
    """
    pass


class MakeTransferOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции покупки.
    """
    category: str


class MakePurchaseOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции оплаты по счету.
    """
    pass


class MakeBillPaymentOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции по снятию наличных денег.
    """
    pass


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    operation: OperationSchema
