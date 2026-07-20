from decimal import Decimal

from System.config import SystemConstants, ErrorTypes, ErrorMessages, TextCharacters


#region System utils

def turn_string_list_to_decimal_list(
    *, 
    string_list: list[str],
    decimal_format_mode: str = SystemConstants.DECIMAL_FORMAT_MODE.value,
) -> list[Decimal]:

    decimal_list: list[Decimal] = []

    for string in string_list:
        raw_decimal_number: Decimal = Decimal(string)
        cleaned_decimal_number: Decimal = Decimal(format(raw_decimal_number.normalize(), decimal_format_mode))
        decimal_list.append(cleaned_decimal_number)

    return decimal_list


def handle_error_and_get_error_text(
    *,
    error_type: str = ErrorTypes.UNKNOWN_ERROR.value,
    error_message: str = ErrorMessages.UNKNOWN_ERROR.value,
) -> str:

    error_object: Error = Error(error_type=error_type, error_message=error_message)
    error_data: tuple[str, str] = error_object.show()
    error_message: str = error_data[1]
    return error_message


def clean_trailing_zeros_from_number(
    *,
    raw_number: Decimal,
    decimal_format_mode: str = SystemConstants.DECIMAL_FORMAT_MODE.value,
) -> Decimal:
    
    cleaned_number: Decimal = Decimal(format(raw_number.normalize(), decimal_format_mode))
    return cleaned_number

#endregion


#region Calculating utils

def compare_two_numbers(
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

def split_and_strip_string_by_divider(
    *,
    raw_input_string: str,
    split_string: str = TextCharacters.COMMA.value,
    strip_string: str = TextCharacters.SPACE.value,
) -> str:

    raw_substring_list: list[str] = raw_input_string.split(split_string)
    cleaned_text_list: list[str] = []

    for raw_string in raw_substring_list:
        cleaned_string: str = raw_string.strip(strip_string)
        cleaned_text_list.append(cleaned_string)

    return cleaned_text_list

#endregion
