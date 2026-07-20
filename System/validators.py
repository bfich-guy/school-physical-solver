from decimal import Decimal

from System.config import SystemConstants


#region Higher-order validators

def is_list_valid(
    *,
    list_object: list,
) -> bool:

    list_is_valld: bool = True

    validator_functions_list: list[Callable] = [

        is_list_structure_valid,
        can_list_be_turned_to_decimal_list,
        
    ]

    for validator_function in validator_functions_list:
        list_is_not_valld: bool = not validator_function(list_object=list_object)

        if list_is_not_valld:
            return False

    return list_is_valld


def is_matrix_valid(
    *,
    list_matrix: list[list],
) -> bool:

    matrix_is_valld: bool = True
    
    validator_functions_list: list[Callable] = [

        is_matrix_structure_valid,
        do_sublists_in_matrix_have_same_length,
        can_matrix_be_turned_to_decimal_matrix,
        
    ]

    for validator_function in validator_functions_list:
        matrix_is_not_valld: bool = not validator_function(list_matrix=list_matrix)

        if matrix_is_not_valld:
            return False

    return matrix_is_valld

#endregion


#region List validators

def is_list_structure_valid(
    *,
    list_object: list,
) -> bool:

    list_object_is_a_list: bool = isinstance(list_matrix, list)
    list_object_is_not_empty: bool = len(list_matrix) > 0

    list_structure_is_valid: bool = all([list_matrix_is_a_list, list_matrix_is_not_empty])
    return list_structure_is_valid


def can_list_be_turned_to_decimal_list(
    *,
    list_object: list,
) -> bool:

    list_can_be_turned_to_decimal_list: Decimal = True

    for element in list_object:
        try:
            Decimal(element)
        except (TypeError, InvalidOperation, IndexError):
            return False

    return list_can_be_turned_to_decimal_list

#endregion


#region Matrix validators

def is_matrix_structure_valid(
    *,
    list_matrix: list[list],
) -> bool:

    matrix_structure_is_valid: bool = True

    list_matrix_is_a_list: bool = isinstance(list_matrix, list)
    list_matrix_is_not_empty: bool = len(list_matrix) > 0

    main_list_is_not_valid: bool = not all([list_matrix_is_a_list, list_matrix_is_not_empty])
    
    if main_list_is_not_valid:
        return False

    for list_object in list_matrix:
        list_object_is_not_a_list: bool = not isinstance(list_object, list)

        if list_object_is_not_a_list:
            return False

    return matrix_structure_is_valid


def do_sublists_in_matrix_have_same_length(
    *,
    list_matrix: list[list],
) -> bool:

    sublists_in_matrix_have_same_length: bool = True

    first_list: list = list_matrix[0]
    etalon_length: int = len(first_list)

    for list_object in list_matrix[1:]:

        list_object_length: int = len(list_object)
        lenghts_are_mismatched: bool = list_object_length != etalon_length

        if lenghts_are_mismatched:
            return False

    return sublists_in_matrix_have_same_length


def can_matrix_be_turned_to_decimal_matrix(
    *,
    list_matrix: list[list],
) -> bool:

    matrix_can_be_turned_to_decimal_matrix: bool = True

    for list_object in list_matrix:
        for element in list_object:
            try:
                Decimal(element)
            except (TypeError, InvalidOperation, IndexError):
                return False

    return matrix_can_be_turned_to_decimal_matrix

#endregion


#region String validators

def is_string_length_in_limit(
    *,
    string: str,
    string_length_limit: int = SystemConstants.MAX_INPUT_LENGTH.value,
) -> bool:

    string_is_not_a_string_at_all: bool = not isinstance(string, str)

    if string_is_not_a_string_at_all:
        return False
    
    string_length: int = len(string)
    string_length_is_in_limit: bool = string_length <= string_length_limit
    return string_length_is_in_limit

#endregion
