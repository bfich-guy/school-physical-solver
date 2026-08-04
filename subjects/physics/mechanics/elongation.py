from decimal import Decimal


#region Spring elongation

def get_spring_elongation_by_elastic_force_and_stiffness_coefficient(
    *,
    elastic_force: Decimal,
    stiffness_coefficient: Decimal,
) -> Decimal:

    spring_elongation: Decimal = elastic_force / stiffness_coefficient
    return spring_elongation

#endregion
