from decimal import Decimal


#region Angle sinus

def get_angle_sinus_by_lorentz_force_and_electric_charge_and_particle_velocity_and_magnetic_induction(
    *,
    lorentz_force: Decimal,
    electric_charge: Decimal,
    particle_velocity: Decimal,
    magnetic_induction: Decimal,
) -> Decimal:

    angle_sinus: Decimal = lorentz_force / (electric_charge * particle_velocity * magnetic_induction)
    return angle_sinus


def get_angle_sinus_by_ampere_force_and_magnetic_induction_and_electric_current_and_conductor_length(
    *,
    ampere_force: Decimal,
    magnetic_induction: Decimal,
    electric_current: Decimal,
    conductor_length: Decimal,
) -> Decimal:

    angle_sinus: Decimal = ampere_force / (magnetic_induction * electric_current * conductor_length)
    return angle_sinus

#endregion
