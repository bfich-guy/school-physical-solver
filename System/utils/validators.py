from decimal import Decimal

from system.config.constants import SystemConstants


#region Number validators

def is_decimal_number_prime(
    *,
    decimal_number: Decimal,
) -> bool:
    
    decimal_number_is_less_than_two: bool = decimal_number < Decimal("2")

    if decimal_number_is_less_than_two:
        return False

    stingified_decimal_number: str = str(decimal_number)
    integered_decimal_number: int = int(stingified_decimal_number)

    for divisor in range(2, integered_decimal_number):
        integered_decimal_number_is_divisible_integrity: bool = integered_decimal_number % divisor == 0
    
        if integered_decimal_number_is_divisible_integrity:
            return False

    return True


def is_decimal_number_integer_or_fraction(
    *,
    decimal_number: Decimal,
    checking_for: str,
) -> bool:

    try:
        decimal_number_state_map: dict[str, bool] = {
            SystemConstants.INTEGER_NUMBER.value: decimal_number % Decimal("1") == Decimal("0"),
            SystemConstants.FRACTION_NUMBER.value: decimal_number % Decimal("1") != Decimal("0"),
        }
        
        result: bool = decimal_number_state_map.get(checking_for, False)
        return result
    except TypeError:
        return False


def does_triangle_exist(
    *,
    first_side: Decimal,
    second_side: Decimal,
    third_side: Decimal,
) -> bool:

    does_triangle_exist: bool = any([
        first_side + second_side > third_side,
        second_side + third_side < first_side,
        third_side + first_side > second_side,
    ])

    return does_triangle_exist


def are_vectors_collinear(
    *,
    first_vector: list[Decimal],
    second_vector: list[Decimal],
) -> bool:

    some_vector_is_dot: bool = all(coordinate == Decimal("0") for coordinate in first_vector) or all(coordinate == Decimal("0") for coordinate in second_vector)
    
    if some_vector_is_dot:
        return True

    suggest_scalar: Decimal | None = None

    for first_vector_coordinate, second_vector_coordinate in zip(first_vector, second_vector):
        both_coordinates_are_not_zeros: bool = all([
            first_vector_coordinate != Decimal("0"),
            second_vector_coordinate != Decimal("0"),
        ])

        if both_coordinates_are_not_zeros:
            suggest_scalar: Decimal | None = second_vector_coordinate / first_vector_coordinate
            break
        else:
            continue

    if not suggest_scalar:
        return False
    else:
        are_vectors_collinear: bool = all([first_vector_coordinate * suggest_scalar == second_vector_coordinate for first_vector_coordinate, second_vector_coordinate in zip(first_vector, second_vector)])
        return are_vectors_collinear

#endregion
