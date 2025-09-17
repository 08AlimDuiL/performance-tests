from typing import Any
import httpx


class HTTPClient:
    """
    Базовый HTTP API клиент, принимающий объект httpx.Client.
    :param client: экземпляр httpx.Client для выполнения HTTP-запросов
    """

    def __init__(self, client: httpx.Client):
        self.client = client

    def post(self, url: str, json: Any | None = None) -> httpx.Response:
        """
        Выполняет POST-запрос.
        :param url: URL-адрес эндпоинта.
        :param json: Данные в формате JSON.
        :return: Объект Response с данными ответа.
        """
        return self.client.post(url=url, json=json)
