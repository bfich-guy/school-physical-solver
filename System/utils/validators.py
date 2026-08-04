from decimal import Decimal

from system.config.constants import SystemConstants


#region User input validators

def is_user_input_valid_for_parsing(
    *,
    user_input: str,
    input_limit_length: int = SystemConstants.MAX_USER_INPUT_LENGTH.value,
) -> bool:

    user_input_is_not_a_string: bool = not isinstance(user_input, str)

    if user_input_is_not_a_string:
        return False
    
    user_input_length: int = len(user_input)

    user_input_length_is_too_big: bool = user_input_length > input_limit_length

    if user_input_length_is_too_big:
        return False
        
    return True

#endregion


#region Number validators

def is_decimal_number_prime(
    *,
    decimal_number: Decimal,
) -> bool:
    
    decimal_number_is_less_than_two: bool = decimal_number < Decimal("2")

    if decimal_number_is_less_than_two:
        return False

    stingified_decimal_number: str = str(decimal_number)
    integered_decimal_number: int = int(stingified_decimal_number)

    for divisor in range(2, integered_decimal_number):
        integered_decimal_number_is_divisible_integrity: bool = integered_decimal_number % divisor == 0
    
        if integered_decimal_number_is_divisible_integrity:
            return False

    return True


def is_decimal_number_integer_or_fraction(
    *,
    decimal_number: Decimal,
    checking_for: str,
) -> bool:

    try:
        decimal_number_state_map: dict[str, bool] = {
            SystemConstants.INTEGER_NUMBER.value: decimal_number % Decimal("1") == Decimal("0"),
            SystemConstants.FRACTION_NUMBER.value: decimal_number % Decimal("1") != Decimal("0"),
        }
        
        result: bool = decimal_number_state_map.get(checking_for, False)
        return result
    except TypeError:
        return False


def does_triangle_exist(
    *,
    first_side: Decimal,
    second_side: Decimal,
    third_side: Decimal,
) -> bool:

    triangle_inequality_is_broken: bool = any([
        first_side + second_side <= third_side,
        second_side + third_side <= first_side,
        third_side + first_side <= second_side,
    ])

    if triangle_inequality_is_broken:
        return False

    return True

#endregion
