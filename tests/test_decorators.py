import pytest

from src.decorators import log


def test_my_function_success(capsys):
    """Тестирует успешное выполнение функции с логированием."""
    @log()
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)

    assert result == 3

    captured = capsys.readouterr()
    assert "my_function ok" in captured.out


def test_my_function_error(capsys):
    """Тестирует функцию, которая вызывает ошибку, с логированием."""
    @log()
    def faulty_function(x):
        return 1 / x

    with pytest.raises(ZeroDivisionError):
        faulty_function(0)

    captured = capsys.readouterr()
    assert "faulty_function error: ZeroDivisionError. Inputs: (0,), {}" in captured.out