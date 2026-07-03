from decimal import Decimal, InvalidOperation

from config import DECIMAL_FORMAT_MODE, DECIMAL_ARRAY_VALID_TYPE

def get_decimal_array_from_string_array(*, 
                                        string_array: list[str] | tuple[str, ...],
                                        array_valid_type: tuple = DECIMAL_ARRAY_VALID_TYPE,
                                        format_mode: str = DECIMAL_FORMAT_MODE
                                        ) -> list[Decimal] | None:
    
    """Transforms a collection of strings into high-precision Decimal objects.

    This validator performs atomic validation on input data packages. It follows
    **the "fail-fast pattern**: if at least one element fails to convert, **the 
    entire batch is rejected** to prevent downstream calculations from processing
    corrupted data.

    **Args**:
    -
        **string_array**: **A list or tuple** containing numbers represented as strings. **Must be non-empty!**

    **Returns**:
    -
        **A list of validated Decimal objects** if all elements were converted 
        successfully. Returns **None** if the input type is invalid, empty, or 
        contains any non-convertible strings. Trailing zeros in decimals are already **cleaned**. 

    **Raises**:
    -
        **No exceptions are raised**; all TypeError and InvalidOperation errors 
        are caught internally to safeguard the pipeline runtime.
    """
    
    string_array_is_invalid_type: bool = not isinstance(string_array, array_valid_type)
    string_array_is_empty: bool = not string_array

    string_array_is_invalid: bool = any([string_array_is_invalid_type, string_array_is_empty])

    if string_array_is_invalid:
        return None
    
    decimal_array: list[Decimal] = []
    
    for element in string_array:
        try:
            decimal_number: Decimal = Decimal(element)
            cleaned_decimal_number: Decimal = Decimal(format(decimal_number.normalize(), format_mode))
            decimal_array.append(cleaned_decimal_number)
        except (TypeError, InvalidOperation):
            return None

    return decimal_array

