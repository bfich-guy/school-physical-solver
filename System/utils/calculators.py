from decimal import Decimal, DivisionByZero, InvalidOperation
from typing import Callable, Any

from system.config.constants import Errors


#region Number calculators

def factorize_decimal_number(
    *,
    decimal_number: Decimal,
) -> list[Decimal]:

    decimal_number_is_less_than_two: bool = decimal_number < Decimal("2")

    if decimal_number_is_less_than_two:
        return [decimal_number]

    prime_multipliers_list: list[Decimal] = []    

    decimal_number_is_not_equal_to_one: bool = decimal_number != Decimal("1")
    divisor: Decimal = Decimal("2")

    while decimal_number_is_not_equal_to_one:
        decimal_number_is_divisible_integrity_by_divisor: bool = decimal_number % divisor == Decimal("0")

        if decimal_number_is_divisible_integrity_by_divisor:
            decimal_number //= divisor
            prime_multipliers_list.append(divisor)
            divisor: Decimal = Decimal("2")
        else:
            divisor += Decimal("1")

        decimal_number_is_not_equal_to_one: bool = decimal_number != Decimal("1")
    
    return prime_multipliers_list


def get_divisors_of_decimal_number(
    *,
    decimal_number: Decimal,
    one_and_minus_one_are_included: bool = False,
) -> list[Decimal]:

    decimal_number_is_zero: bool = decimal_number == Decimal("0")

    if decimal_number_is_zero:
        return []

    divisors_list: list[Decimal] = []

    opposite_decimal_number: Decimal = -decimal_number

    start_number: Decimal = min(decimal_number, opposite_decimal_number)
    end_number: Decimal = max(decimal_number, opposite_decimal_number)

    stringified_start_number: str = str(start_number)
    stringified_end_number: str = str(end_number)
    stringified_decimal_number: str = str(decimal_number)

    integered_start_number: int = int(stringified_start_number)
    integered_end_number: int = int(stringified_end_number)
    integered_decimal_number: int = int(stringified_decimal_number)

    step: int = 1

    for potential_divisor in range(integered_start_number, integered_end_number + 1, step):
        potential_divisor_is_zero: bool = potential_divisor == 0

        if potential_divisor_is_zero:
            continue

        potential_divisor_is_a_real_divisor: bool = integered_decimal_number % potential_divisor == 0 

        if potential_divisor_is_a_real_divisor:
            stringified_divisor: str = str(potential_divisor)
            decimaled_divisor: Decimal = Decimal(stringified_divisor)
            divisors_list.append(decimaled_divisor)

    if not one_and_minus_one_are_included:
        divisors_list.remove(Decimal("-1"))
        divisors_list.remove(Decimal("1"))

    return divisors_list


def calculate_value_safely(
    calculator_function: Callable,
) -> Any:

    def wrapper(*args, **kwargs) -> Any:
        try:
            value: Any = calculator_function(*args, **kwargs)
            return value
        
        except DivisionByZero:
            return Errors.ZERO_DIVISION.value
        
        except InvalidOperation:
            return Errors.NEGATIVE_ROOT.value

        except Exception as e:
            return Errors.UNKNOWN_ERROR.value

    return wrapper

#endregion
