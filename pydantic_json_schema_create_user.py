from clients.users.public_users_client import get_public_user_client
from tools.fakers import fake
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema
import jsonschema

public_user_client = get_public_user_client()

create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_user_client.create_user_api(create_user_request)
create_user_response_schema = CreateUserResponseSchema.model_json_schema()
print(create_user_response.json())
print(create_user_response_schema)

jsonschema.validate(instance=create_user_response.json(), schema=create_user_response_schema)
