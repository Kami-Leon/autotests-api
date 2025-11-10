import allure

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExercisesRequestSchema, CreateExercisesResponseSchema, \
    ExerciseSchema, GetExerciseResponseSchema, UpdateExercisesRequestSchema, UpdateExercisesResponseSchema, \
    GetExercisesResponseSchema
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_internal_error_response
from tools.logger import get_logger

logger = get_logger("EXERCISES_ASSERTION") # Добавляем логирование


@allure.step("Check exercise")
def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные упражнения соответствуют ожидаемым.

    :param actual: Фактические данные упражнения.
    :param expected: Ожидаемые данные упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check exercise") # Добавляем логирование

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


@allure.step("Check get exercise response")
def assert_get_exercise_response(
        get_exercise_response: GetExerciseResponseSchema,
        create_exercise_response: CreateExercisesResponseSchema
):
    """
    Проверяет, что ответ на получение упражнения соответствует ответу на его создание.

    :param get_exercise_response: Ответ API при запросе упражнения.
    :param create_exercise_response: Ответ API при создании упражнения.
    :raises AssertionError: Если данные заданий не совпадают.
    """
    logger.info("Check get exercise response") # Добавляем логирование

    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)


@allure.step("Check get exercises response")
def assert_get_exercises_response(
        get_exercises_response: GetExercisesResponseSchema,
        create_exercise_responses: list[CreateExercisesResponseSchema]
):
    """
    Проверяет, что ответ на получение списка упражнений соответствует ответам на их создание.

    :param get_exercises_response: Ответ API при запросе списка упражнений.
    :param create_exercise_responses: Список API ответов при создании упражнений.
    :raises AssertionError: Если данные упражнений не совпадают.
    """
    logger.info("Check get exercises response") # Добавляем логирование

    for index, create_exercise_response in enumerate(create_exercise_responses):
        assert_exercise(get_exercises_response.exercises[index], create_exercise_response.exercise)


@allure.step("Check create exercise response")
def assert_create_exercise_response(
        request: CreateExercisesRequestSchema,
        response: CreateExercisesResponseSchema
):
    """
    Проверяет, что ответ на создание упражнения соответствует данным из запроса.

    :param request: Исходный запрос на создание упражнения.
    :param response: Ответ API создания упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check create exercise response") # Добавляем логирование

    assert_equal(request.title, response.exercise.title, "title")
    assert_equal(request.course_id, response.exercise.course_id, "course_id")
    assert_equal(request.max_score, response.exercise.max_score, "max_score")
    assert_equal(request.min_score, response.exercise.min_score, "min_score")
    assert_equal(request.order_index, response.exercise.order_index, "order_index")
    assert_equal(request.description, response.exercise.description, "description")
    assert_equal(request.estimated_time, response.exercise.estimated_time, "estimated_time")


@allure.step("Check update exercise response")
def assert_update_exercise_response(
        request: UpdateExercisesRequestSchema,
        response: UpdateExercisesResponseSchema
):
    """
    Проверяет, что ответ на обновление упражнения соответствует данным из запроса.

    :param request: Исходный запрос на обновление упражнения.
    :param response: Ответ API с обновленными данными упражнениями.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check update exercise response") # Добавляем логирование

    assert_equal(request.title, response.exercise.title, "title")
    assert_equal(request.max_score, response.exercise.max_score, "max_score")
    assert_equal(request.min_score, response.exercise.min_score, "min_score")
    assert_equal(request.order_index, response.exercise.order_index, "order_index")
    assert_equal(request.description, response.exercise.description, "description")
    assert_equal(request.estimated_time, response.exercise.estimated_time, "estimated_time")


@allure.step("Check exercise not found response")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, что запрос получения задания содержит внутреннюю ошибку.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "Exercise not found"
    """
    logger.info("Check exercise not found response") # Добавляем логирование

    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual, expected)
