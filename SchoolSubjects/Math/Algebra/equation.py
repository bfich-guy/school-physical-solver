from decimal import Decimal


#region Linear equation solving

def solve_linear_equation(
    *,
    linear_coefficient: Decimal,
    constant_term: Decimal,
) -> Decimal:

    root: Decimal = -constant_term / linear_coefficient
    return root

#endregion


#region Quadratic equation solving

def solve_quadratic_equation(
    *,
    quadratic_coefficient: Decimal,
    linear_coefficient: Decimal,
    constant_term: Decimal,
) -> list[Decimal]:

    discriminant: Decimal = pow(linear_coefficient, Decimal("2")) - Decimal("4") * quadratic_coefficient * constant_term
    discriminant_square_root: Decimal = discriminant.sqrt()

    root_1: Decimal = (-linear_coefficient - discriminant_square_root) / (Decimal("2") * quadratic_coefficient)
    root_2: Decimal = (-linear_coefficient + discriminant_square_root) / (Decimal("2") * quadratic_coefficient)

    root_list: list[Decimal] = [root_1, root_2]
    return root_list


def get_sum_and_product_of_quadratic_equation_roots_by_viet_theorem(
    *,
    quadratic_coefficient: Decimal,
    linear_coefficient: Decimal,
    constant_term: Decimal,
) -> list[Decimal]:

    new_linear_coefficient: Decimal = linear_coefficient / quadratic_coefficient
    new_constant_term: Decimal = constant_term / quadratic_coefficient

    root_sum: Decimal = -new_linear_coefficient
    root_product: Decimal = new_constant_term

    viet_theorem_list: list[Decimal] = [root_sum, root_product]
    return viet_theorem_list

#endregion
