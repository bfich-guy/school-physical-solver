from decimal import Decimal, InvalidOperation

from System.config import SystemConstants


#region List validators

def is_list_structure_valid(
    *,
    list_object: list,
) -> bool:

    lambda_pipeline_list: list[Callable[[], bool]] = [
        lambda: not isinstance(list_object, list),
        lambda: not list_object,
    ]

    for lambda_function in lambda_pipeline_list:
        list_object_is_not_valid: bool = lambda_function()

        if list_object_is_not_valid:
            return False

    return True


def can_string_list_object_list_be_turned_to_decimal_number_list(
    *,
    list_object: list[str],
) -> bool:

    for element in list_object:
        try:
            Decimal(element)
        except (TypeError, InvalidOperation):
            return False

    return True

#endregion


#region Matrix validators

def is_matrix_structure_valid(
    *,
    matrix_object: list[list], 
) -> bool:

    lambda_pipeline_list: list[Callable[[], bool]] = [
        lambda: not isinstance(matrix_object, list),
        lambda: not matrix_object,
    ]

    for lambda_function in lambda_pipeline_list:
        matrix_object_is_not_valid: bool = lambda_function()

        if matrix_object_is_not_valid:
            return False

    for list_object in matrix_object:
        list_object_is_not_a_list: bool = not isinstance(list_object, list)

        if list_object_is_not_a_list:
            return False

    return True


def are_sublists_in_matrix_have_same_length(
    *,
    list_object: list[list],
) -> bool:

    try:
        first_list: list = list_object[0]
        etalon_length: int = len(first_list)

        for list_object in list_object:
            list_object_length: int = len(list_object)
            lengths_are_mismatched: bool = list_object_length != etalon_length

            if lengths_are_mismatched:
                return False
    except (IndexError, TypeError):
        return False

    return True

#endregion


#region String validators

def is_string_length_in_limit(
    *,
    string_object: str,
    string_length_limit: int = SystemConstants.MAX_INPUT_LENGTH.value,
) -> bool:

    string_object_is_not_a_string_at_all: bool = not isinstance(string_object, str)

    if string_object_is_not_a_string_at_all:
        return False
    
    string_object_length: int = len(string_object)
    string_object_length_is_in_limit: bool = string_object_length <= string_length_limit
    return string_object_length_is_in_limit

#endregion
