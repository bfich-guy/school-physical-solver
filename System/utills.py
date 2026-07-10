from decimal import Decimal

#region Calculating utils

def compare_two_numbers(
    *,
    number_1: Decimal,
    comparing_mark: str,
    number_2: Decimal,
) -> bool:

    """Returns boolean variable of comparing Decimal() numbers.
    
    This function gets two Decimal() numbers and comparing mark as a string. 
    It compares that numbers in lambda functions inside an comparing map (dictionary). 
    Finally function returns a boolean variable of this mathematician expression.
    
    **Args**:

        **number_1**: A first number of class Decimal().
        **comparing_mark**: A comparing mark. Function supports marks **<, <=, ==, >=, >, !=**.
        **number_2**: A second number of class Decimal().
    
    **Returns**:
    
        **A boolean variable** of mathematician expression number_1 comparing_mark number_2.
        If function can't compare numbers (Comparing mark is not a string, for example), functions returns **False**. 

    **Raises**:

        **TypeError**, if numbers are not Decimal() type.  

    **Examples**:

        This function can be used for **comparing discriminant to zero for solving quadratic equations**. 

        >>> compare_two_numbers(number_1=Decimal("100"), comparing_mark=">=", number_2=Decimal("0"))
        True

        >>> compare_two_numbers(number_1=Decimal("-100"), comparing_mark=">=", number_2=Decimal("0"))
        False
        
        >>> compare_two_numbers(number_1=Decimal("67"), comparing_mark="SIX SEVEN", number_2=Decimal("67"))
        False
    """

    comparation_dict: dict[str, callable] = {
        "<": lambda: number_1 < number_2,
        "<=": lambda: number_1 <= number_2,
        "==": lambda: number_1 == number_2,
        ">=": lambda: number_1 >= number_2,
        ">": lambda: number_1 > number_2,
        "!=": lambda: number_1 != number_2,
    }

    comparator_function: callable | None = comparation_dict.get(comparing_mark, None)
    comparator_function_is_none: bool = comparator_function is None

    if comparator_function_is_none:
        return False
    
    result: bool = comparator_function()
    return result

#endregion


#region System utils

#TODO: write function turn_string_array_to_decimal_array(*, string_array: list[str] | tuple[str, ․․․]) -> list[Decimal]:

#endregion
