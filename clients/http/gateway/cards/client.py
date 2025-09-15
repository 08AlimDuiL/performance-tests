import httpx
from clients.http.client import HTTPClient
from typing import TypedDict


class IssueCardsRequestDict(TypedDict):
    """
    Структура данных для создания карты (виртуальной или физической).

    :param userId: Идентификатор пользователя
    :param accountId: Идентификатор счета для привязки карты
    """
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    Предоставляет методы для работы с виртуальными и физическими картами.
    """

    def issue_virtual_card_api(self, request: IssueCardsRequestDict) -> httpx.Response:
        """
        Создание виртуальной карты через API.

        Выполняет POST-запрос к эндпоинту /api/v1/cards/issue-virtual-card
        для создания новой виртуальной карты.

        :param request: Словарь с данными для создания виртуальной карты.
                        Должен содержать обязательные поля: userId, accountId.
        :return: Ответ от сервера (объект httpx.Response) с информацией о созданной карте
                 или ошибкой валидации.
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: IssueCardsRequestDict) -> httpx.Response:
        """
        Создание физической карты через API.

        Выполняет POST-запрос к эндпоинту /api/v1/cards/issue-physical-card
        для создания новой физической карты.

        :param request: Словарь с данными для создания физической карты.
                        Должен содержать обязательные поля: userId, accountId.
        :return: Ответ от сервера (объект httpx.Response) с информацией о созданной карте
                 или ошибкой валидации.
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)