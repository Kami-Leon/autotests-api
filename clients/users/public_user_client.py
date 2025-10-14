from httpx import Response
from typing import TypedDict

from clients.api_client import ApiClient


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUserClient(ApiClient):
    """
    Публичный клиент для работы с /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод создает нового пользователя.

        :param request: Словарь с данными нового пользователями
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("api/v1/users", json=request)
