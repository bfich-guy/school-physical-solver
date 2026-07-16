from decimal import Decimal

from System.config import SystemConstants


#region System validators

def can_iterable_object_be_turned_to_decimal_list(
    *,
    iterable_object: list[str] | tuple[str] | dict[str, str],
    decimal_iterable_object_valid_type: tuple = SystemConstants.DECIMAL_ITERABLE_OBJECT_VALID_TYPE.value,
) -> bool:

    """Checks whether all strings in the given iterable object can be Decimal() numbers. 

    This function uses **fail fast and early exit patterns**. 
    That means if argument iterable_object is not an iterable object at all or one single string can not be a Decimal(), **function returns False**. 
    Finally it returns a boolean variable that indicates whether the iterable object can be completely decimaled or not. 

    **Args**:

        **iterable_object**: **An iterable object** that can be filled by difference data types, not only strings. 
        **decimal_iterable_object_valid_type**: **A tuple with types of iterable objects** that function supports: **list, tuple**. 

    **Returns**:
        
        **A boolean variable** that indicates whether the iterable object can be completely decimaled or not. 

    **Examples**:

        This function can be used **to make sure user wrote a numbers, not words**. 

        >>> can_iterable_object_be_turned_to_decimal_list(iterable_object=["3.14", "1.41", "2.72"])
        True

        >>> can_iterable_object_be_turned_to_decimal_list(iterable_object=())
        False

        >>> can_iterable_object_be_turned_to_decimal_list(iterable_object={"JUST DECIMAL PI RIGHT HERE ->": "3.14"})
        False

        >>> can_iterable_object_be_turned_to_decimal_list(iterable_object=["3.14", "WAIT! WHY FUNCTION RET..."])
        False

    """

    iterable_object_is_empty: bool = not iterable_object
    iterable_object_is_not_iterable_object: bool = not isinstance(iterable_object, decimal_iterable_object_valid_type)

    iterable_object_is_not_valid: bool = any([iterable_object_is_empty, iterable_object_is_not_iterable_object])

    if iterable_object_is_not_valid:
        return False

    iterable_object_can_be_turned_to_decimal_list: bool = True

    for string in iterable_object:
        try:
            Decimal(string)
        except (TypeError, InvalidOperation):
            return False

    return iterable_object_can_be_turned_to_decimal_list

#endregion
