from decimal import Decimal

from System.config import DECIMAL_FORMAT_MODE


#region System utils

def turn_string_array_to_decimal_array(
    *, 
    string_array: list[str] | tuple[str, ...],
    decimal_format_mode: str = DECIMAL_FORMAT_MODE,
) -> list[Decimal]:

    """Returns array with only decimal numbers.
    
    This function gets the array (list or tuple) and decimals every string there.
    It cleans trailing zeros inside a decimal numbers. 
    Finally function returns an array filled with decimal numbers. 

    **Args**:

        **string_array**: **A list or tuple** that can be filled by different data types, not only strings. 
        **decimal_format_mode**: **A string** "f" that function format() uses for cleaning traling zeros. 

    **Returns**:

        **Array with decimal numbers** inside it. 

    **Raises**:

        **TypeError**, if string_array is not array. 
        **InvalidOperation**, if array element can't be decimaled. 

    **Examples**:

        >>> turn_string_array_to_decimal_array(string_array=["3.14", "1.41", "2.78"])
        [Decimal('3.14'), Decimal('1.41'), Decimal('2.78')]

        >>> turn_string_array_to_decimal_array(string_array={"Make this array decimaled, please ->": "3.14"})
        Traceback (most recent call last):
        TypeError: ...

        >>> turn_string_array_to_decimal_array(string_array=("3.14", "IT IS PI! DECIMAL IT! JUST DO-O-O IT! Wait, WHY IS THE ER..."))
        Traceback (most recent call last):
        decimal.InvalidOperation: ...       

    """

    decimal_array: list[Decimal] = []

    for string in string_array:
        raw_decimal_number: Decimal = Decimal(string)
        cleaned_decimal_number: Decimal = Decimal(format(raw_decimal_number.normalize(), decimal_format_mode))
        decimal_array.append(cleaned_decimal_number)

    return decimal_array

#endregion


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

        **KeyError**, if comparing mark doesn't exist. 
        **TypeError**, if numbers are not Decimal() type. 
        **InvalidOperation**, if string can't be decimaled. 

    **Examples**:

        This function can be used for **comparing discriminant to zero for solving quadratic equations**. 

        >>> compare_two_numbers(number_1=Decimal("100"), comparing_mark=">=", number_2=Decimal("0"))
        True

        >>> compare_two_numbers(number_1=Decimal("-100"), comparing_mark=">=", number_2=Decimal("0"))
        False
        
        >>> compare_two_numbers(number_1=Decimal("67"), comparing_mark="<=>", number_2=Decimal("67"))
        Traceback (most recent call last):
        KeyError: ...

        >>> compare_two_numbers(number_1="SQRT OF TWO", comparing_mark="<=", number_2=Decimal("3.14"))
        Traceback (most recent call last):
        TypeError: ...

        >>> compare_two_numbers(number_1=Decimal("NUMBER_PI"), comparing_mark="NOTHING COMPARES WITH PI!", number_2=Decimal("WHY IS THERE ER..."))
        Traceback (most recent call last):
        decimal.InvalidOperation: ...
    """

    comparation_dict: dict[str, Callable[[], bool]] = {
        "<": lambda: number_1 < number_2,
        "<=": lambda: number_1 <= number_2,
        "==": lambda: number_1 == number_2,
        ">=": lambda: number_1 >= number_2,
        ">": lambda: number_1 > number_2,
        "!=": lambda: number_1 != number_2,
    }

    comparator_function: Callable[[], bool] = comparation_dict[comparing_mark]
    result: bool = comparator_function()
    return result


def get_delta_value(
    *,
    end_value: Decimal,
    start_value: Decimal,
) -> Decimal:

    """Returns delta of two given values.

    This function calculates difference between end_value and start_value.
    Finally it returns this difference.

    **Args**:

        **end_value**: the end Decimal() value. 
        **start_value**: the start Decimal() value. 

    **Returns**:

        **A Decimal() value** that equals to mathematical expression end_value - start_value. 

    **Raises**:

        **TypeError**, if at least one given argument is not a Decimal(). 

    **Examples**:

        This function can be used for calculating **deltas of physics and mathemathician concepts**.
        It means that it calculates delta speed for acceleration or delta coordinates for vectors. 

        >>> get_delta_value(end_value=Decimal("3.14"), start_value=Decimal("0.14"))
        Decimal("3")

        >>> get_delta_value(end_value="NUMBER PI!!!", start_value="NO START VALUES!!!")
        Traceback (most recent call last):
        TypeError: ...
    
    """

    result: Decimal = end_value - start_value
    return result

#endregion
