from decimal import Decimal


#region Spring elongation

def get_spring_elongation_by_elastic_force_and_spring_stiffness(
    *,
    elastic_force: Decimal,
    spring_stiffness: Decimal,
) -> Decimal:

    spring_elongation: Decimal = elastic_force / spring_stiffness
    return spring_elongation

#endregion
