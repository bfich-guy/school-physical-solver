from decimal import Decimal

def solve_quadratic_equation_by_discriminant(
    *,
    quadratic_coefficient: Decimal,
    linear_coefficient: Decimal,
    constant_term: Decimal,
) -> list[Decimal]:

    discriminant: Decimal = pow(linear_coefficient, 2) - 4 * quadratic_coefficient * constant_term
    discriminant_square_root: Decimal = discriminant.sqrt()

    root_1: Decimal = (-linear_coefficient - discriminant_square_root) / (2 * quadratic_coefficient)
    root_2: Decimal = (-linear_coefficient + discriminant_square_root) / (2 * quadratic_coefficient)

    root_list: list[Decimal] = [root_1, root_2]
    return root_list

