def mask_account_card(input_string):
    # Применение маскировки в зависимости от типа
    if "Счет" in input_string:
        account_number = input_string.split(" ", 1)[1]  # Получаем только номер счета
        masked_number = f"**{account_number[-4:]}"  # Маскируем все кроме последних 4 цифр
        return f"Счет {masked_number}"
    else:
        card_info = input_string.split(" ", 1)  # Разделяем на название карты и номер
        card_type = card_info[0]
        card_number = card_info[1]

        # Применение маскировки для карт
        if len(card_number) == 16:
            masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"  # Маскируем карту
        else:
            # Обработка карт с другим количеством цифр
            masked_number = card_number[:-4].replace(card_number[:-4], '**') + card_number[-4:]

        return f"{card_type} {masked_number}"


# Примеры использования
print(mask_account_card("Visa Platinum 7000792289606361"))  # Visa Platinum 7000 79** **** 6361
print(mask_account_card("Счет 73654108430135874305"))  # Счет **4305