from http import HTTPStatus
import pytest
import allure
from allure_commons.types import Severity

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExercisesRequestSchema, CreateExercisesResponseSchema, \
    GetExerciseResponseSchema, UpdateExercisesRequestSchema, UpdateExercisesResponseSchema, GetExercisesQuerySchema, \
    GetExercisesResponseSchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.allure.epics import AllureEpic
from tools.assertions.allure.features import AllureFeature
from tools.assertions.allure.stories import AllureStory
from tools.assertions.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_found_response, assert_get_exercises_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(AllureTag.EXERCISES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.EXERCISES)
class TestExercises:

    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create exercise")
    @allure.severity(Severity.BLOCKER)
    def test_create_exercise(self, exercises_client: ExercisesClient, function_course: CourseFixture):
        request = CreateExercisesRequestSchema(course_id=function_course.response.course.id)
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExercisesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Get exercise")
    @allure.severity(Severity.BLOCKER)
    def test_get_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture,
            function_course: CourseFixture
    ):
        response = exercises_client.get_exercise_api(function_exercise.response.exercise.id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(response_data, function_exercise.response)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.title("Update exercise")
    @allure.severity(Severity.CRITICAL)
    def test_update_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture
    ):
        request = UpdateExercisesRequestSchema()
        response = exercises_client.update_exercise_api(function_exercise.response.exercise.id, request)
        response_data = UpdateExercisesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.title("Delete exercise")
    @allure.severity(Severity.CRITICAL)
    def test_delete_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture
    ):
        delete_exercise_response = exercises_client.delete_exercise_api(function_exercise.response.exercise.id)
        assert_status_code(delete_exercise_response.status_code, HTTPStatus.OK)

        get_exercise_response = exercises_client.get_exercise_api(function_exercise.response.exercise.id)
        get_exercise_response_data = InternalErrorResponseSchema.model_validate_json(get_exercise_response.text)

        assert_status_code(get_exercise_response.status_code, HTTPStatus.NOT_FOUND)
        assert_exercise_not_found_response(get_exercise_response_data)

        validate_json_schema(get_exercise_response.json(), get_exercise_response_data.model_json_schema())

    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.title("Get exercises")
    @allure.severity(Severity.BLOCKER)
    def test_get_exercises(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture,
            function_course: CourseFixture
    ):
        request = GetExercisesQuerySchema(course_id=function_course.response.course.id)
        response = exercises_client.get_exercises_api(request)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercises_response(response_data, [function_exercise.response])

        validate_json_schema(response.json(), response_data.model_json_schema())
