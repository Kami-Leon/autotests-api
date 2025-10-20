from httpx import Response

from clients.api_client import ApiClient
from clients.public_http_builder import get_public_http_client
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema


class PublicUserClient(ApiClient):
    """
    Публичный клиент для работы с /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Метод создает нового пользователя.

        :param request: Словарь с данными нового пользователями
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("api/v1/users", json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_user_client() -> PublicUserClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUserClient(client=get_public_http_client())
