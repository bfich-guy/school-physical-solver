from decimal import Decimal

from System.config import SystemConstants


#region System validators

def can_iterable_object_be_turned_to_decimal_list(
    *,
    iterable_object: list[str],
    decimal_iterable_object_valid_type: tuple = SystemConstants.DECIMAL_ITERABLE_OBJECT_VALID_TYPE.value,
) -> bool:

    """Returns a boolean variable that indicates whether all strings in the given iterable object can be Decimal() numbers. 

    This function gets the iterable object for checking whether it can be a decimal list or not. 
    It uses a **LBYL + EAFP + Fail-Fast** patterns. That means if

    -iterable_object is not an iterable at all
    -iterable_object is empty
    -one single string can't be turned to a Decimal()

    **function returns False immediately**!

    Finally it returns a boolean variable that indicates whether the iterable object can be completely decimaled or not. 

    **Args**:

        **iterable_object**: **An iterable object** that can be filled by difference data types, not only strings. 
        **decimal_iterable_object_valid_type**: **A tuple with types of iterable objects** that function supports: **list**. 

    **Returns**:
        
        **A boolean variable** that indicates whether the iterable object can be completely decimaled or not. 

    **Examples**:

        This function can be used **to make sure user wrote a numbers, not words**. 

        >>> can_iterable_object_be_turned_to_decimal_list(iterable_object=["3.14", "1.41", "2.72"])
        True

        >>> can_iterable_object_be_turned_to_decimal_list(iterable_object=[])
        False

        >>> can_iterable_object_be_turned_to_decimal_list(iterable_object={"JUST DECIMAL PI RIGHT HERE ->": "3.14"})
        False

        >>> can_iterable_object_be_turned_to_decimal_list(iterable_object=["3.14", "WAIT! WHY FUNCTION RET..."])
        False

    """

    iterable_object_is_empty: bool = not iterable_object
    iterable_object_is_not_valid_iterable_object: bool = not isinstance(iterable_object, decimal_iterable_object_valid_type)

    iterable_object_is_not_valid_at_all: bool = any([iterable_object_is_empty, iterable_object_is_not_valid_iterable_object])

    if iterable_object_is_not_valid_at_all:
        return False

    iterable_object_can_be_turned_to_decimal_list: bool = True

    for string in iterable_object:
        try:
            Decimal(string)
        except (TypeError, InvalidOperation):
            return False

    return iterable_object_can_be_turned_to_decimal_list


def is_string_length_in_limit(
    *,
    string: str,
    string_length_limit: int = SystemConstants.MAX_INPUT_LENGTH.value,
) -> bool:

    """Returns a boolean variable that indicates whether string is too long or not.

    This function gets the string and limit of valid length (it is 32). 
    It uses a **LBYL** pattern. That means if

    -string is not a string at all

    **function returns False immediately**!

    Finally function returns the boolean variable that indicates whether string is too long or not. 

    **Args**:

        **string**: **A string** length of that should be checked. 
        **string_length_limit**: **An integer** number that is a given string length and has value 32. 
        
    **Returns**:

        **A boolean variable** that indicates whether string is too long or not. 

    **Examples**:

        This function can be used for preventing too long input from user. 

        >>> string_length_is_in_limit(string="3.14 is the number PI!")
        True

        >>> string_length_is_in_limit(string=["3.14", "<- PI! AND WHY FUNCTION RET..."])
        False

        >>> string_length_is_in_limit(string="AAAAHHHH!!!! I AM FURIOUS! WHY DOES THIS FUNCTION ALWAYS RETURN THAT ANNOYING F...")
        False

    """

    string_is_not_a_string_at_all: bool = not isinstance(string, str)

    if string_is_not_a_string_at_all:
        return False
    
    string_length: int = len(string)
    string_length_is_in_limit: bool = string_length <= string_length_limit
    return string_length_is_in_limit


def do_lists_have_same_length(
    *,
    list_matrix: list[list],
) -> bool:

    """Returns boolean variable that indicates wheter lists have same length or not. 

    This function gets the matrix (list with lists inside) and stores length of first sublist as an etalon length. 
    It uses a **LBYL + Fail-Fast** patterns. That means if

    -list_matrix is not an list at all
    -list_matrix is empty
    -sublists in list_matrix are not lists at all (function checks first list **separately** to measure etalon length)
    -one single legnth mismatch happened

    **function returns False immediately**!
    
    Finally function returns a boolean variable that indicates wheter lists have same length or not. 

    **Args**:

        **list_matrix**: **A matrix**. This is a list with sublists inside which lengths are comparing. 

    **Returns**:

        **A boolean variable** that indicates wheter lists have same length or not. 

    **Examples**:

        This function can be used for comparing lengths of vectors and not let adding vectors with different sizes. 

        >>> do_lists_have_same_length(list_matrix=[[Decimal("0"), Decimal("0")], [Decimal("3"), Decimal("4")]])
        True

        >>> do_lists_have_same_length(list_matrix=[[Decimal("1"), Decimal("2")], [Decimal("3")]])
        False

        >>> do_lists_have_same_length(list_matrix=[])
        False

        >>> do_lists_have_same_length(list_matrix="HA-HA! STRING IS ITERABLE!!! LET ME... JUST...")
        False

        >>> do_lists_have_same_length(list_matrix=["AAAAHHHH!!! FALSE! GET THIS!", "WAIT! WHY FUNCTION RET..."])
        False

        >>> do_lists_have_same_length(list_matrix=[["3.14"], "<- SEE?! A LI-I-IST! JUST RETURN TRUE! I LEAVE THIS JO-O-O-B!!!"])
        False
        
    """

    list_matrix_is_not_a_list: bool = not isinstance(list_matrix, list)
    list_matrix_is_empty: bool = not list_matrix

    list_matrix_is_not_valid_at_all: bool = any([list_matrix_is_not_a_list, list_matrix_is_empty])

    if list_matrix_is_not_valid_at_all:
        return False

    lists_have_same_length: bool = True

    first_list: list = list_matrix[0]
    first_list_is_not_a_list: bool = not isinstance(first_list, list)

    if first_list_is_not_a_list:
        return False

    etalon_length: int = len(first_list)

    for list_object in list_matrix[1:]:
        list_object_is_not_a_list: bool = not isinstance(list_object, list)

        if list_object_is_not_a_list:
            return False

        list_object_length: int = len(list_object)
        lenghts_are_mismatched: bool = list_object_length != etalon_length

        if lenghts_are_mismatched:
            return False

    return lists_have_same_length

#endregion
