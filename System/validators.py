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

def is_string_in_length_limit(
    *,
    string_object: str,
    length_limit: int = SystemConstants.MAX_INPUT_LENGTH.value,
) -> bool:

    invalid_conditions_lambdas_list: list[Callable[[], bool]] = [
        lambda: not isinstance(string_object, str),
        lambda: len(string_object) > length_limit,
    ]

    result: bool = validate_given_object_by_conditions(
        given_object=string_object,
        invalid_conditions_lambdas_list=invalid_conditions_lambdas_list,
    )

    return result


def does_list_have_only_one_element(
    *,
    list_object: list,
) -> bool:

    invalid_conditions_lambdas_list: list[Callable[[], bool]] = [
        lambda: not isinstance(list_object, list),
        lambda: len(list_object) != 1,
    ]

    result: bool = validate_given_object_by_conditions(
        given_object=list_object,
        invalid_conditions_lambdas_list=invalid_conditions_lambdas_list,
    )
    return result

#endregion
