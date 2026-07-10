from decimal import Decimal, InvalidOperation

from System.config import DECIMAL_ARRAY_VALID_TYPE


#region validators

def can_string_array_be_decimaled(
    *,
    string_array: list[str] | tuple[str, ․․․],
    decimal_array_valid_type: tuple = DECIMAL_ARRAY_VALID_TYPE,
) -> bool:

    """Checks whether all strings in the given array can be Decimal() numbers. 

    This function uses **fail-fast pattern**. 
    It means that if one single string can not be a Decimal() - **array is rejected** and function returns False!

    **Args**:

        **string_array**: **A list or tuple** that can be filled by difference data types, not only strings. 
        **decimal_array_valid_type**: **A tuple with types of arrays** that function supports: **list and tuple**. 

    **Returns**:
        
        **A boolean variable** that indicates whether the array can be completely decimaled or not.

    **Examples**:

        This function can be used **to make sure user wrote a numbers, not words**. 

        >>> can_string_array_be_decimaled(string_array=["3.14", "1.41", "2.72"])
        True

        >>> can_string_array_be_decimaled(string_array=[])
        False

        >>> string_array={"Okay, empty list isn't valid. JUST DECIMAL PI RIGHT HERE ->": 3.14}
        False

        >>> can_string_array_be_decimaled(string_array=["3.14", "DECIMAL IT! DON'T YOU SEE?!!!", "WAIT! WHY FUNCTION RET..."])
        False

        >>> can_string_array_be_decimaled(string_array=["I AM RAGING!!! I LEAVE THIS JOB!!!! WHAT THE HE..."])
        False
    """

    string_array_is_empty: bool = not string_array
    string_array_is_not_valid_type: bool = not isinstance(string_array, decimal_array_valid_type)

    string_array_is_not_valid: bool = any([string_array_is_not_valid_type, string_array_is_empty])

    if string_array_is_not_valid:
        return False

    result: bool = True

    for string in string_array:
        try:
            Decimal(string)
        except (TypeError, InvalidOperation):
            return False

    return result

#endregion
