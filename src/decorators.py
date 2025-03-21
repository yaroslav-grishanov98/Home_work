def log(log_list=None):
    """Декоратор для логирования успешного выполнения функции и обработки ошибок."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            """Обернутая функция, которая выполняет логирование."""
            log_message = ""
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                if log_list is not None:
                    log_list.append(log_message)
                return result
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if log_list is not None:
                    log_list.append(log_message)
                raise
        return wrapper
    return decorator





