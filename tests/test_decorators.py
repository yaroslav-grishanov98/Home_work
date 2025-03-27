import pytest

from src.decorators import log


@log()
def successful_function(x, y):
    """Суммирует два числа."""
    return x + y


@log()
def function_with_exception(x, y):
    """Делит x на y. Генерирует ZeroDivisionError, если y равно 0."""
    return x / y


def test_successful_function(capsys):
    """Тестирует успешное выполнение функции с корректными аргументами.

    Проверяет, что результат функции равен ожидаемому значению и
    что вывод на консоль соответствует сообщению об успешном выполнении.
    """
    result = successful_function(3, 5)
    captured = capsys.readouterr()

    assert result == 8
    assert captured.out.strip() == "successful_function ok"


def test_function_with_exception(capsys):
    """Тестирует обработку исключений в функции.

    Проверяет, что при делении на ноль вызывается исключение
    ZeroDivisionError и выводит ожидаемое сообщение об ошибке.
    """
    with pytest.raises(ZeroDivisionError):
        function_with_exception(10, 0)

    captured = capsys.readouterr()
    assert "function_with_exception error: ZeroDivisionError" in captured.out