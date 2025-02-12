def mask_account_card(input_string: str) -> str:
    if "Счет" in input_string:
        account_number = input_string.split(" ", 1)[1]
        masked_number = f"**{account_number[-4:]}"
        return f"Счет {masked_number}"
    else:
        card_info = input_string.split(" ", 1)
        card_type = card_info[0]
        card_number = card_info[1].replace(' ', '')


        if len(card_number) >= 16:
            masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        else:
            masked_number = f"{'*' * (len(card_number) - 4)}{card_number[-4:]}"

        return f"{card_type} {masked_number}"

def get_mask_card_number(card_input: str) -> str:
    return mask_account_card(card_input)

def get_mask_account(account_input: str) -> str:
    return mask_account_card(account_input)


print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
