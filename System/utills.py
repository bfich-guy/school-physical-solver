from decimal import Decimal

from System.config import SystemConstants, ErrorTypes, ErrorMessages, TextCharacters


#region System utils

def create_error_object_and_get_its_message(
    *,
    error_type: str = ErrorTypes.UNKNOWN_ERROR.value,
    error_message: str = ErrorMessages.UNKNOWN_ERROR.value,
) -> str:

    error_object: Error = Error(error_type=error_type, error_message=error_message)
    error_object_data: tuple[str, str] = error_object.show()
    error_object_message: str = error_object_data[1]
    return error_object_message


def clean_trailing_zeros_from_decimal_number(
    *,
    raw_decimal_number: Decimal,
    decimal_format_mode: str = SystemConstants.DECIMAL_FORMAT_MODE.value,
) -> Decimal:
    
    cleaned_decimal_number: Decimal = Decimal(format(raw_decimal_number.normalize(), decimal_format_mode))
    return cleaned_decimal_number

#endregion


#region Calculating utils

def compare_two_numbers_and_get_result(
    *,
    number_1: Decimal,
    comparing_mark: str,
    number_2: Decimal,
) -> bool:

    comparation_dict: dict[str, Callable[[], bool]] = {
        "<": lambda: number_1 < number_2,
        "<=": lambda: number_1 <= number_2,
        "==": lambda: number_1 == number_2,
        ">=": lambda: number_1 >= number_2,
        ">": lambda: number_1 > number_2,
        "!=": lambda: number_1 != number_2,
    }

    comparator_function: Callable[[], bool] = comparation_dict[comparing_mark]
    result: bool = comparator_function()
    return result


def get_delta_value_of_two_numbers(
    *,
    end_value: Decimal,
    start_value: Decimal,
) -> Decimal:

    delta_value: Decimal = end_value - start_value
    return delta_value

#endregion


#region String utils

def get_decimal_numbers_list_from_raw_string(
    *, 
    raw_string: str,
    valid_characters: str = SystemConstants.VALID_DIGIT_CHARACTERS.value,
    number_divider_character: str = TextCharacters.DOT.value,
) -> list[Decimal]:

    raw_string_does_not_have_valid_characters_at_all: bool = not any(character.isdigit() for character in raw_string)

    if raw_string_does_not_have_valid_characters_at_all:
        return []

    valid_character_index_list: list[int] = []

    for index, character in enumerate(raw_string):
        chracter_is_valid: bool = character in valid_characters

        if chracter_is_valid:
            valid_character_index_list.append(index)

    valid_characther_index_matrix: list[list[int]] = []
    number_character_index_list: list[int] = []
    raw_string_length: int = len(raw_string)

    for cursor_index in range(raw_string_length + 1):
        valid_character_index_exists: bool = cursor_index in valid_character_index_list

        if valid_character_index_exists:
            number_character_index_list.append(cursor_index)
        else:
            number_character_index_list_is_empty: bool = not number_character_index_list

            if number_character_index_list_is_empty:
                continue
            else:
                valid_characther_index_matrix.append(number_character_index_list)
                number_character_index_list: list[int] = []

    valid_character_matrix: list[list[str]] = []
    valid_character_list: list[str] = []

    for valid_character_index_list in valid_characther_index_matrix:
        for valid_character_index in valid_character_index_list:
            valid_character: str = raw_string[valid_character_index]
            valid_character_list.append(valid_character)

        valid_character_matrix.append(valid_character_list)
        valid_character_list: list[str] = []

    raw_number_list: list[str] = []

    for valid_character_list in valid_character_matrix:
        raw_number: str = "".join(valid_character_list)
        raw_number_list.append(raw_number)
    
    cleaned_number_list: list[list[str]] = []
    number_element_list: list[str] = []

    for raw_number in raw_number_list:
        raw_number_character_list: list[str] = raw_number.split(number_divider_character)
        cleaned_number_character_list: list[str] = []

        for number_element in raw_number_character_list:
            number_element_is_empty: bool = not number_element

            if number_element_is_empty:
                continue
            else:
                cleaned_number_character_list.append(number_element)

        cleaned_number: str = number_divider_character.join(cleaned_number_character_list)
        cleaned_number_list.append(cleaned_number)

    decimal_number_list: list[str] = []

    for cleaned_number in cleaned_number_list:
        try:
            decimal_number: Decimal = Decimal(cleaned_number)
            decimal_number_list.append(decimal_number)
        except InvalidOperation:
            continue

    return decimal_number_list

#endregion
