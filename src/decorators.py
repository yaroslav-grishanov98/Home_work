from functools import wraps


def log(file_name=None):
    """Декоратор для логирования успешного выполнения функции и обработки ошибок."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """Обернутая функция, которая выполняет логирование."""
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                raise
            else:
                log_message = f"{func.__name__} ok"
                return result
            finally:
                if not file_name:
                    print(log_message)
                else:
                    with open(file_name, "w", encoding="utf-8") as file:
                        file.write(log_message)

        return wrapper

    return decorator
