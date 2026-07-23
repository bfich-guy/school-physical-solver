from decimal import Decimal, InvalidOperation
from typing import Callable, Any

from System.config import SystemConstants


#region Core validators

def validate_given_object_by_conditions(
    given_object: Any,
    invalid_conditions_lambdas_list: list[Callable[[], bool]],
) -> bool:

    for condition_lambda in invalid_conditions_lambdas_list:
        given_object_is_not_valid: bool = condition_lambda()

        if given_object_is_not_valid:
            return False

    return True

#endregion


#region Wrapper validators

def is_string_valid_for_parsing(
    *,
    string_object: str,
    length_limit: int = SystemConstants.MAX_INPUT_STRING_LENGTH.value,
) -> bool:

    invalid_conditions_lambdas_list: list[Callable[[], bool]] = [
        lambda: not isinstance(string_object, str),
        lambda: len(string_object) > length_limit,
        lambda: not any(character.isdigit() for character in string_object)
    ]

    result: bool = validate_given_object_by_conditions(
        given_object=string_object,
        invalid_conditions_lambdas_list=invalid_conditions_lambdas_list,
    )

    return result


def is_list_valid_for_calculating(
    *,
    list_object: list,
    length_limit: int = SystemConstants.MAX_DECIMAL_LIST_LENGTH.value,
) -> bool:

    invalid_conditions_lambdas_list: list[Callable[[], bool]] = [
        lambda: not isinstance(list_object, list),
        lambda: len(list_object) != length_limit,
    ]

    result: bool = validate_given_object_by_conditions(
        given_object=list_object,
        invalid_conditions_lambdas_list=invalid_conditions_lambdas_list,
    )
    
    return result


def is_decimal_number_a_fraction(
    *,
    decimal_number: Decimal,
) -> bool:

    invalid_conditions_lambdas_list: list[Callable[[], bool]] = [
        lambda: not isinstance(decimal_number, Decimal),
        lambda: decimal_number // Decimal("1") == decimal_number,
    ]

    result: bool = validate_given_object_by_conditions(
        given_object=list_object,
        invalid_conditions_lambdas_list=invalid_conditions_lambdas_list,
    )
    
    return result


def can_decimal_number_be_prime_factorized(
    *,
    decimal_number: Decimal,
) -> bool:

    invalid_conditions_lambdas_list: list[Callable[[], bool]] = [
        lambda: not isinstance(decimal_number, Decimal),
        lambda: decimal_number < Decimal("2"),
        lambda: decimal_number // Decimal("1") != decimal_number,
    ]

    result: bool = validate_given_object_by_conditions(
        given_object=list_object,
        invalid_conditions_lambdas_list=invalid_conditions_lambdas_list,
    )
    
    return result

#endregion
