from decimal import Decimal

from System.config import PhysicsConstants


#region Resultive force

def get_resultant_force_by_general_mass_and_general_acceleration(
    *,
    general_mass: Decimal,
    general_acceleration: Decimal = PhysicsConstants.GRAVITATIONAL_ACCELERATION.value,
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


#region Normal force

def get_normal_force_by_friction_force_and_friction_coefficient(
    *,
    friction_force: Decimal,
    friction_coefficient: Decimal,
) -> Decimal:

    normal_force: Decimal = friction_force / friction_coefficient
    return normal_force

#endregion


#region Friction force

def get_friction_force_by_friction_coefficient_and_normal_force(
    *,
    friction_coefficient: Decimal,
    normal_force: Decimal,
) -> Decimal:

    friction_force: Decimal = friction_coefficient * normal_force
    return friction_force

#endregion
