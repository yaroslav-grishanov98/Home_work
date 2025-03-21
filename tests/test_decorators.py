import pytest

from src.decorators import log


def test_my_function_success():
    """Тестирует успешное выполнение функции с логированием."""
    logs = []

    @log(logs)
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)

    assert result == 3
    assert "my_function ok" in logs


def test_my_function_error():
    """Тестирует функцию, которая вызывает ошибку, с логированием."""
    logs = []

    @log(logs)
    def faulty_function(x):
        return 1 / x

    with pytest.raises(ZeroDivisionError):
        faulty_function(0)

    assert "faulty_function error: ZeroDivisionError. Inputs: (0,), {}" in logs