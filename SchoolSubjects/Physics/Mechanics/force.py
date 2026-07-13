from decimal import Decimal

from System.config import GRAVITATIONAL_ACCELERATION


#region Resultive force

def get_resultant_force_by_general_mass_and_general_acceleration(
    *,
    general_mass: Decimal,
    general_acceleration: Decimal = GRAVITATIONAL_ACCELERATION,
) -> Decimal:

    resultant_force: Decimal = general_mass * general_acceleration
    return resultant_force

#endregion


#region Elastic force

def get_elastic_force_by_spring_stiffness_and_spring_elongation(
    *,
    spring_stiffness: Decimal,
    spring_elongation: Decimal,
) -> Decimal:

    elastic_force: Decimal = spring_stiffness * spring_elongation
    return elastic_force

#endregion
