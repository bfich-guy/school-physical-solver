from decimal import Decimal


#region Electromotive force

def get_electromotive_force_by_general_voltage_and_general_current_and_electric_internal_resistance(
    *,
    electric_voltage: Decimal,
    electric_current: Decimal,
    electric_internal_resistance: Decimal,
) -> Decimal:

    electromotive_force: Decimal = electric_voltage + (electric_current * electric_internal_resistance)
    return electromotive_force

#endregion


#region Lorentz force

def get_lorentz_force_by_electric_charge_and_particle_velocity_and_magnetic_induction_and_angle_sinus(
    *,
    electric_charge: Decimal,
    particle_velocity: Decimal,
    magnetic_induction: Decimal,
    angle_sinus: Decimal,
) -> Decimal:

    lorentz_force: Decimal = electric_charge * particle_velocity * magnetic_induction * angle_sinus
    return lorentz_force

#endregion
