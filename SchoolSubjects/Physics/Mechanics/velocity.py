from decimal import Decimal


#region General velocity

def get_general_velocity_by_general_distance_and_motion_duration(
    *,
    general_distance: Decimal,
    motion_duration: Decimal,
) -> Decimal:

    general_velocity: Decimal = general_distance / motion_duration
    return general_velocity

#endregion


#region Linear velocity

def get_linear_velocity_by_linear_momentum_and_object_mass(
    *,
    linear_momentum: Decimal,
    object_mass: Decimal,
) -> Decimal:

    linear_velocity: Decimal = linear_momentum / object_mass
    return linear_velocity


def get_linear_velocity_by_kinetic_energy_and_momentum(
    *,
    kinetic_energy: Decimal,
    linear_momentum: Decimal,
) -> Decimal:

    linear_velocity: Decimal = (Decimal("2") * kinetic_energy) / linear_momentum
    return linear_velocity


def get_linear_velocity_by_angular_velocity_and_radius(
    *,
    angular_velocity: Decimal,
    radius: Decimal,
) -> Decimal:

    linear_velocity: Decimal = angular_velocity * radius
    return linear_velocity

#endregion


#region Angular velocity

def get_angular_velocity_by_linear_velocity_and_radius(
    *,
    linear_velocity: Decimal,
    radius: Decimal,
) -> Decimal:

    angular_velocity: Decimal = linear_velocity / radius
    return angular_velocity

#endregion
