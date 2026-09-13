from decimal import Decimal


#region General force

def get_general_force_by_mechanical_work_and_general_distance_and_angle_cosinus(
    *,
    mechanical_work: Decimal,
    general_distance: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    general_force: Decimal = mechanical_work / (general_distance * angle_cosinus)
    return general_force


def get_general_force_by_mechanic_pressure_and_general_area(
    *,
    mechanic_pressure: Decimal,
    general_area: Decimal,
) -> Decimal:

    general_force: Decimal = mechanic_pressure * general_area
    return general_force

#endregion


#region Resultive force

def get_resultant_force_by_general_mass_and_general_acceleration(
    *,
    general_mass: Decimal,
    general_acceleration: Decimal,
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


#region Gravitational force

def get_gravitational_force_by_potential_energy_and_lift_height(
    *,
    potential_energy: Decimal,
    lift_height: Decimal,
) -> Decimal:

    gravitational_force: Decimal = potential_energy / lift_height
    return gravitational_force

#endregion
