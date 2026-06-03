from decimal import Decimal, InvalidOperation

def get_decimal_array_from_string_array(*, 
                                        string_array: list[str] | tuple[str, ...]
                                        ) -> list[Decimal] | None:
    
    """Transforms a collection of strings into high-precision Decimal objects.

    This validator performs atomic validation on input data packages. It follows
    **the "all-or-nothing" rule**: if at least one element fails to convert, **the 
    entire batch is rejected** to prevent downstream calculations from processing
    corrupted data.

    **Args**:
    -
        **string_array**: **A list or tuple** containing numbers represented as strings. **Must be non-empty!**

    **Returns**:
    -
        **A list of validated Decimal objects** if all elements were converted 
        successfully. Returns **None** if the input type is invalid, empty, or 
        contains any non-convertible strings.

    **Raises**:
    -
        **No exceptions are raised**; all TypeError and InvalidOperation errors 
        are caught internally to safeguard the pipeline runtime.
    """
    
    string_array_is_invalid_type: bool = not isinstance(string_array, (list, tuple))
    string_array_is_empty: bool = not string_array

    string_array_is_invalid: bool = any([string_array_is_invalid_type, string_array_is_empty])

    if string_array_is_invalid:
        return None
    
    string_array_length: int = len(string_array)
    result_array: list[Decimal] = []
    
    for element in string_array:
        try:
            decimal_number: Decimal = Decimal(element)
            result_array.append(decimal_number)
        except (TypeError, InvalidOperation):
            continue

    result_array_length: int = len(result_array)
    string_and_result_arrays_lengths_are_mismatched: bool = string_array_length != result_array_length

    if string_and_result_arrays_lengths_are_mismatched:
        return None
    
    return result_array

