from decimal import Decimal

from System.config import DECIMAL_ARRAY_VALID_TYPE


#region System validators

def can_string_list_be_turned_to_decimal_list(
    *,
    string_list: list[str],
    decimal_array_valid_type: tuple = DECIMAL_ARRAY_VALID_TYPE,
) -> bool:

    """Checks whether all strings in the given list can be Decimal() numbers. 

    This function uses **fail fast and early exit patterns**. 
    That means if argument string_list is not a list at all or one single string can not be a Decimal(), **function returns False**. 
    Finally it returns a boolean variable that indicates whether the list can be completely decimaled or not. 

    **Args**:

        **string_list**: **A list** that can be filled by difference data types, not only strings. 
        **decimal_array_valid_type**: **A tuple with types of arrays** that function supports: **list**. 

    **Returns**:
        
        **A boolean variable** that indicates whether the list can be completely decimaled or not. 

    **Examples**:

        This function can be used **to make sure user wrote a numbers, not words**. 

        >>> can_string_list_be_turned_to_decimal_list(string_list=["3.14", "1.41", "2.72"])
        True

        >>> can_string_list_be_turned_to_decimal_list(string_list=[])
        False

        >>> can_string_list_be_turned_to_decimal_list(string_list={"OK, empty list isn't valid. JUST DECIMAL PI RIGHT HERE ->": 3.14})
        False

        >>> can_string_list_be_turned_to_decimal_list(string_list=["3.14", "DECIMAL IT! DON'T YOU SEE?!!!", "WAIT! WHY FUNCTION RET..."])
        False

    """

    string_list_is_empty: bool = not string_list
    string_list_is_not_list: bool = not isinstance(string_list, decimal_array_valid_type)

    string_list_is_not_valid: bool = any([string_list_is_empty, string_list_is_not_list])

    if string_list_is_not_valid:
        return False

    string_list_can_be_turned_to_decimal_list: bool = True

    for string in string_list:
        try:
            Decimal(string)
        except (TypeError, InvalidOperation):
            return False

    return string_list_can_be_turned_to_decimal_list

#endregion
