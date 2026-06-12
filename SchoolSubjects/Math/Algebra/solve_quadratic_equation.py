from decimal import Decimal, InvalidOperation

from utils import get_decimal_array_from_string_array

def solve_quadratic_equation(*,
                             leading_coefficient: str,
                             middle_coefficient: str,
                             constant_term: str,
                             ) -> list[Decimal] | None:
    
    string_value_array: list[str] = [leading_coefficient, middle_coefficient, constant_term]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None

    try:
        decimal_leading_coefficient, decimal_middle_coefficient, decimal_constant_term = decimal_value_array
        
        discriminant: Decimal = pow(decimal_middle_coefficient, 2) - 4 * decimal_leading_coefficient * decimal_constant_term
        discriminant_square_root: Decimal = discriminant.sqrt()

        root_1: Decimal = (-decimal_middle_coefficient - discriminant_square_root) / (2 * decimal_leading_coefficient)
        root_2: Decimal = (-decimal_middle_coefficient + discriminant_square_root) / (2 * decimal_leading_coefficient)

        square_equation_solution: list[Decimal] = [root_1, root_2]
        return square_equation_solution
    except (InvalidOperation, ZeroDivisionError):
        return None
    
