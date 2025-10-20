import httpx
import uuid
from pydantic import BaseModel, Field, EmailStr, HttpUrl

from tools.fakers import get_random_email


class UserSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    user: UserSchema


CreateUserRequest = CreateUserRequestSchema(
    email=get_random_email(),
    password="password",
    lastName="Bond",
    firstName="Zara",
    middleName="Alice",
)

base_url = "http://localhost:8000"
response = httpx.post(f"{base_url}/api/v1/users", json=CreateUserRequest.model_dump(by_alias=True))

validated_response = CreateUserResponseSchema.model_validate(response.json())

print(validated_response)
print(validated_response.json())
print(validated_response.model_dump())
print(validated_response.model_dump_json())
