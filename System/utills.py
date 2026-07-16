from decimal import Decimal

from System.config import SystemConstants, ErrorTypes, ErrorMessages, TextCharacters


#region System utils

def turn_string_list_to_decimal_list(
    *, 
    string_list: list[str],
    decimal_format_mode: str = SystemConstants.DECIMAL_FORMAT_MODE.value,
) -> list[Decimal]:

    """Returns list with only decimal numbers.
    
    This function gets the list and decimals every string there.
    It turns string into Decimal() number and cleans trailing zeros inside it. 
    Finally function returns a list filled with decimal numbers. 

    **Args**:

        **string_list**: **A list** that can be filled by different data types, not only strings. 
        **decimal_format_mode**: **A string** "f" that function format() uses for cleaning traling zeros. 

    **Returns**:

        **A list with decimal numbers** inside it. 

    **Raises**:

        **TypeError**, if string_list is not list. 
        **InvalidOperation**, if list element can't be decimaled. 

    **Examples**:

        >>> turn_string_list_to_decimal_list(string_list=["3.14", "1.41", "2.78"])
        [Decimal('3.14'), Decimal('1.41'), Decimal('2.78')]

        >>> turn_string_list_to_decimal_list(string_list={"Make this thing decimaled, please ->": "3.14"})
        Traceback (most recent call last):
        TypeError: ...

        >>> turn_string_list_to_decimal_list(string_list=("3.14", "IT IS PI! DECIMAL IT! JUST DO-O-O IT! Wait, WHY IS THE ER..."))
        Traceback (most recent call last):
        decimal.InvalidOperation: ...       

    """

    decimal_list: list[Decimal] = []

    for string in string_list:
        raw_decimal_number: Decimal = Decimal(string)
        cleaned_decimal_number: Decimal = Decimal(format(raw_decimal_number.normalize(), decimal_format_mode))
        decimal_list.append(cleaned_decimal_number)

    return decimal_list


def handle_error_and_get_error_text(
    *,
    error_type: str = ErrorTypes.UNKNOWN_ERROR.value,
    error_message: str = ErrorMessages.UNKNOWN_ERROR.value,
) -> str:

    """Returns an error text or text of the error itself is unknown.
    
    This function gets error type and message and creates an object of class Error().
    Then it calls the error object's method .show(), what returns the tuple (error_type, error_message). 
    Finally function returns error message that error object returned. 
    
    **Args**:
    
        **error_type**: **A string** that represents a type of error. 
        **error_message**: **A string** that represents a message of error. 

    **Returns**:

        **A string** which is the error message. If non-string arguments are provided, they will be implicitly converted to strings. 

    **Examples**:

        This function can be used to make error more readable for user. 

        >>> handle_error_and_get_error_text(error_type="MATH_ERROR", error_message="На ноль делить нельзя!")
        'На ноль делить нельзя!'

        >>> handle_error_and_get_error_text(error_type=3.14, error_message="NUMBER PI!")
        'NUMBER PI!'

    """

    error_object: Error = Error(error_type=error_type, error_message=error_message)
    error_data: tuple[str, str] = error_object.show()
    error_message: str = error_data[1]
    return error_message


def do_lists_have_same_length(
    *,
    list_matrix: list[list],
) -> bool:

    """Returns boolean variable that indicates wheter lists have same length or not. 

    This function gets the matrix (list with lists inside) and stores length of first sublist as an etalon length. 
    Then it compares lengths of other lists with etalon by **fail-fast pattern**. 
    That means if one single length mismatch happened, **function returns False**. 
    Finally function returns a boolean variable that indicates wheter lists have same length or not. 

    **Args**:

        **list_matrix**: **A matrix**. This is a list with sublists inside which lengths are comparing. 

    **Returns**:

        **A boolean variable** that indicates wheter lists have same length or not. 

    **Raises**:

        **IndexError**, if given matrix is empty. 
        **TypeError**, if matrix doesn't contain iterables.  

    **Examples**:

        This function can be used for comparing lengths of vectors and not let adding vectors with different sizes. 

        >>> do_lists_have_same_length(list_matrix=[[Decimal("0"), Decimal("0")], [Decimal("3"), Decimal("4")]])
        True

        >>> do_lists_have_same_length(list_matrix=[[Decimal("0"), Decimal("0"), Decimal("0")], [Decimal("3"), Decimal("4")]])
        False

        >>> do_lists_have_same_length(list_matrix=[])
        Traceback (most recent call last):
        IndexError: ...

        >>> do_lists_have_same_length(list_matrix=[Decimal("3.14"), "<- IT IS PI! COMPARE IT! WAIT, WHY IS THERE ER..."])
        Traceback (most recent call last):
        TypeError: ...
        
    """

    first_list: list = list_matrix[0]
    etalon_length: int = len(first_list)

    lists_have_same_length: bool = all(len(list_object) == etalon_length for list_object in list_matrix)
    return lists_have_same_length


def clean_trailing_zeros_from_number(
    *,
    raw_number: Decimal,
    decimal_format_mode: str = SystemConstants.DECIMAL_FORMAT_MODE.value,
) -> Decimal:

    """Returns a Decimal() number without trailing zeros.

    This function gets the Decimal() number and default format mode "f".
    Then it uses built-in function format() to clean trailing zeros. Simply, **it is wrapper** to function format(). 
    Finally function returns the Decimal() number without trailing zeros at the end. 

    **Args**:

        **number**: **A Decimal() number** that is need to clean from trailing zeros. 
        **decimal_format_mode**: **A string** that is already given and has value "f". 

    **Returns**:

        **A Decimal() number** without trailing zeros. 

    **Raises**:

        **TypeError**, if given number is not a Decimal(). 

    **Examples**:

        This function can be used to make Decimal() number more readable for user. 

        >>> clean_trailing_zeros_from_number(raw_number=Decimal("3.14000"))
        Decimal("3.14")

        >>> clean_trailing_zeros_from_number(raw_number=3.14)
        Traceback (most recent call last):
        TypeError: ...

    """
    
    cleaned_number: Decimal = Decimal(format(raw_number.normalize(), decimal_format_mode))
    return cleaned_number

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


#region Text parsing utils

def split_and_strip_string(
    *,
    raw_input_string: str,
    split_string: str = TextCharacters.COMMA.value,
    strip_string: str = TextCharacters.SPACE.value,
) -> str:

    """Returns a list with pure strings without spaces.

    This function gets the raw input string and uses built-in string methods .split() and .strip().
    At first function splits the text, then it strips substrings in list to clean it from spaces. 
    Finally function returns the list where are pure strings. 

    **Args**:

        **raw_input_string**: **A string** that should be parsed. 
        **split_string**: **A string** that is need to divide raw_input_string and has value ",".
        **strip_string**: **A string** that is need to strip substrings in list and has value " ". 

    **Returns**:

        **A list of pure substrings** without spaces. 

    **Raises**:

        **AttributeError**, if argument raw_input_string is not a string. 
    
    **Examples**:

        This function can be used for getting numbers from user for validation and further calculations.

        >>> split_and_strip_string(raw_input_string="10, 20, 30")
        ['10', '20', '30']

        >>> split_and_strip_string(raw_input_string=3.14)
        Traceback (most recent call last):
        AttributeError: ...

    """

    raw_substring_list: list[str] = raw_input_string.split(split_string)
    cleaned_text_list: list[str] = []

    for raw_string in raw_substring_list:
        cleaned_string: str = raw_string.strip(strip_string)
        cleaned_text_list.append(cleaned_string)

    return cleaned_text_list

#endregion
