from decimal import Decimal, InvalidOperation

from system.config.constants import SystemConstants


#region Text parsers

def get_decimal_numbers_from_user_input(
    *,
    user_input: str,
    valid_characters: str = SystemConstants.VALID_DIGIT_CHARACTERS.value,
) -> list[Decimal]:

    valid_characters_matrix: list[list[str]] = []
    valid_characters_list: list[str] = []

    user_input_length: int = len(user_input)

    for index, character in enumerate(user_input):
        character_is_valid: bool = character in valid_characters

        if character_is_valid:
            valid_characters_list.append(character)
            cycle_is_over: bool = index == user_input_length - 1

            if cycle_is_over:
                valid_characters_matrix.append(valid_characters_list)
                valid_characters_list: list[str] = []

        else:
            valid_characters_list_is_empty: bool = not valid_characters_list

            if valid_characters_list_is_empty:
                continue

            valid_characters_matrix.append(valid_characters_list)
            valid_characters_list: list[str] = []

    decimal_numbers_list: list[Decimal] = []

    for valid_characters_list in valid_characters_matrix:
        potential_decimal_number: str = "".join(valid_characters_list)
    
        try:
            decimal_number: Decimal = Decimal(potential_decimal_number)
            decimal_numbers_list.append(decimal_number)
        except InvalidOperation:
            continue

    return decimal_numbers_list

#endregion
