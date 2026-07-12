from decimal import Decimal

#region Spring stiffness

def get_spring_stiffness_by_elastic_force_and_spring_elongation(
    *,
    elastic_force: Decimal,
    spring_elongation: Decimal,
) -> Decimal:

    spring_stiffness: Decimal = elastic_force / spring_elongation
    return spring_stiffness

#endregion
