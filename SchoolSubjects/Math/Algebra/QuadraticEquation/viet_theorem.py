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

