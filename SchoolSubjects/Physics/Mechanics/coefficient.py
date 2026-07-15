from decimal import Decimal


#region Friction coefficient

def get_friction_coefficient_by_friction_force_and_normal_force(
    *,
    friction_force: Decimal,
    normal_force: Decimal,
) -> Decimal:

    friction_coefficient: Decimal = friction_force / normal_force
    return friction_coefficient

#endregion


#region Stiffness coefficient

def get_stiffness_coefficient_by_elastic_force_and_spring_elongation(
    *,
    elastic_force: Decimal,
    spring_elongation: Decimal,
) -> Decimal:

    stiffness_coefficient: Decimal = elastic_force / spring_elongation
    return stiffness_coefficient

#endregion
