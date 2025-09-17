from httpx import Response, QueryParams
from clients.http.client import HTTPClient
from typing import TypedDict


class GetOperationsQueryDict(TypedDict):
    """
      Структура данных для получения списка операций определенного счета.
    """
    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    """
      Структура данных для получения статистики по операциям определенного счета.
    """
    accountId: str


class MakeOperationRequestDict(TypedDict):
    """
    Базовая структура данных для операций.
    Содержит общие поля для всех типов операций.

    :param status: Статус операции
    :param amount: Сумма операции
    :param cardId: Идентификатор карты
    :param accountId: Идентификатор счета
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции комиссии.
    """
    pass


class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции пополнения.
    """
    pass


class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции кэшбэка.
    """
    pass


class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции перевода.
    """
    pass


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции покупки.
    """
    category: str


class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции оплаты по счету.
    """
    pass


class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции по снятию наличных денег.
    """
    pass


class OperationsGatewayHTTPClient(HTTPClient):

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка операций для определенного счета.
        :param query: Словарь с параметрами запроса, например: {'accountId': 'ca7d831c-3bcb-4022-a938-be6d002d59f8'}.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение статистики по операциям для определенного счета.
        :param query: Словарь с параметрами запроса, например: {'accountId': 'ca7d831c-3bcb-4022-a938-be6d002d59f8'}.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получить чек по операции по operation_id.
        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получить информацию об операции по operation_id.
        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Создание операции комиссии.
        :param request: Словарь с данными по операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Создание операции пополнения.
        :param request: Словарь с данными по операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Создание операции кэшбэка.
        :param request: Словарь с данными по операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Создание операции перевода.
        :param request: Словарь с данными по операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Создание операции покупки.
        :param request: Словарь с данными по операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Создание операции оплаты по счету.
        :param request: Словарь с данными по операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Создание операции по снятию наличных денег.
        :param request: Словарь с данными по операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)
