def log(filename=None):
    """Декоратор для логирования успешного выполнения функции и обработки ошибок."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            """Обернутая функция, которая выполняет логирование."""
            try:
                result = func(*args, **kwargs)
                print(f"{func.__name__} ok")  # Выводим в консоль
                return result
            except Exception as e:
                print(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")  # Выводим в консоль
                raise
        return wrapper
    return decorator

# Пример использования
@log()
def my_function(x, y):
    """Суммирует два числа."""
    return x + y




