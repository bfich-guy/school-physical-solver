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

def get_fraction_and_mixed_number_from_decimal_number(
    *,
    cleaned_decimal_number: Decimal,
    fraction_divider: str = TextCharacters.DOT.value,
) -> list[list[str]]:
    
    cleaned_decimal_number: Decimal = clean_trailing_zeros_from_decimal_number(raw_decimal_number=cleaned_decimal_number)
    stringified_decimal_number: str = str(cleaned_decimal_number)
    decimal_number_integer_part, decimal_number_fraction_part = stringified_decimal_number.split(fraction_divider)

    period_pattern_length: int = len(decimal_number_fraction_part)
    stringified_period_pattern_length: str = str(period_pattern_length)
    decimaled_period_pattern_length: Decimal = Decimal(stringified_period_pattern_length)
    ten_to_the_power_of_decimaled_period_pattern_length: Decimal = Decimal("10") ** decimaled_period_pattern_length

    raw_multiplied_decimal_number: Decimal = cleaned_decimal_number * (ten_to_the_power_of_decimaled_period_pattern_length + Decimal("1"))
    cleaned_multiplied_decimal_number: Decimal = clean_trailing_zeros_from_decimal_number(raw_decimal_number=raw_multiplied_decimal_number)
    raw_delta_decimal_number: Decimal = cleaned_multiplied_decimal_number - cleaned_decimal_number
    cleaned_delta_decimal_number: Decimal = clean_trailing_zeros_from_decimal_number(raw_decimal_number=raw_delta_decimal_number)

    cleaned_improrer_fraction_numerator: Decimal = cleaned_delta_decimal_number
    cleaned_improrer_fraction_denominator: Decimal = ten_to_the_power_of_decimaled_period_pattern_length - Decimal("1")
    improrer_fraction_list: list[Decimal] = [cleaned_improrer_fraction_numerator, cleaned_improrer_fraction_denominator]

    raw_mixed_number_integer_part: Decimal = cleaned_improrer_fraction_numerator // cleaned_improrer_fraction_denominator
    cleaned_mixed_number_integer_part: Decimal = clean_trailing_zeros_from_decimal_number(raw_decimal_number=raw_mixed_number_integer_part)
    raw_mixed_number_fraction_part_numerator: Decimal = cleaned_improrer_fraction_numerator - (cleaned_mixed_number_integer_part * cleaned_improrer_fraction_denominator)
    cleaned_mixed_number_fraction_part_numerator: Decimal = clean_trailing_zeros_from_decimal_number(raw_decimal_number=raw_mixed_number_fraction_part_numerator)
    cleaned_mixed_number_denominator: Decimal = cleaned_improrer_fraction_denominator
    mixed_number_list: list[Decimal] = [cleaned_mixed_number_integer_part, cleaned_mixed_number_fraction_part_numerator, cleaned_mixed_number_denominator]
    
    fraction_and_mixed_number_matrix: list[list[Decimal]] = [improrer_fraction_list, mixed_number_list]
    return fraction_and_mixed_number_matrix


def get_prime_multipliers_of_decimal_number(
    *,
    raw_decimal_number: Decimal,
) -> list[Decimal]:

    cleaned_decimal_number: Decimal = clean_trailing_zeros_from_decimal_number(raw_decimal_number=raw_decimal_number)
    prime_multipliers_list: list[Decimal] = []    
    divisor: Decimal = Decimal("2")

    cleaned_decimal_number_is_not_equal_to_one: bool = cleaned_decimal_number != Decimal("1")

    while cleaned_decimal_number_is_not_equal_to_one:
        decimal_number_is_divisible_integrity_by_divisor: bool = cleaned_decimal_number % divisor == Decimal("0")

        if decimal_number_is_divisible_integrity_by_divisor:
            cleaned_decimal_number //= divisor
            prime_multipliers_list.append(divisor)
            divisor: Decimal = Decimal("2")
        else:
            divisor += Decimal("1")

        cleaned_decimal_number_is_not_equal_to_one: bool = cleaned_decimal_number != Decimal("1")
    
    return prime_multipliers_list

#endregion


#region String utils

def get_decimal_numbers_list_from_raw_string(
    *, 
    raw_string: str,
    valid_characters: str = SystemConstants.VALID_DIGIT_CHARACTERS.value,
    number_divider_character: str = TextCharacters.DOT.value,
) -> list[Decimal]:

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
            cleaned_decimal_number: Decimal = Decimal(cleaned_number)
            decimal_number_list.append(cleaned_decimal_number)
        except InvalidOperation:
            continue

    return decimal_number_list

#endregion
