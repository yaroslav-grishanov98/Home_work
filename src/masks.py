def get_mask_card_number(card_number: str) -> str:
    """Функция, на входе которой принимает номер карты в виде числа, и возвращает XXXX XX** **** XXXX"""
    if len(card_number) != 16:
        raise ValueError('Неправильный номер карты: должен содержать 16 цифр.')
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(mask_account: str) -> str:
    """Функция, которая на вход номер счета в виде числа и возвращает маску номер **XXXX"""
    if len(mask_account) < 20:
        raise ValueError('Неправильный номер счета: должен содержать минимум 20 цифр.')
    return f"**{mask_account[-4:]}"
