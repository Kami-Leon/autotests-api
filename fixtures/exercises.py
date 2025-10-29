import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import ExercisesClient, get_exercise_client
from clients.exercises.exercises_schema import CreateExercisesRequestSchema, CreateExercisesResponseSchema
from fixtures.users import UserFixture


class ExerciseFixture(BaseModel):
    request: CreateExercisesRequestSchema
    response: CreateExercisesResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercise_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(
        exercises_client: ExercisesClient,
        function_user: UserFixture
) -> ExerciseFixture:
    request = CreateExercisesRequestSchema()
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)
