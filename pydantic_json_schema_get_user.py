import jsonschema

from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_user_client
from clients.users.user_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.fakers import fake

public_user_client = get_public_user_client()

create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_user_client.create_user(request=create_user_request)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_user_client = get_private_users_client(user=authentication_user)

get_user_response = private_user_client.get_user_api(user_id=create_user_response.user.id)
get_user_response_schema = GetUserResponseSchema.model_json_schema()
print(get_user_response.json())
print(get_user_response_schema)

jsonschema.validate(instance=get_user_response.json(), schema=get_user_response_schema)