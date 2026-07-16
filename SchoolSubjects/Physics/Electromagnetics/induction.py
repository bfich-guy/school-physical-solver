from decimal import Decimal


#region Magnetic induction

def get_magnetic_induction_by_lorentz_force_and_electric_charge_and_particle_velocity_and_angle_sinus(
    *,
    lorentz_force: Decimal,
    electric_charge: Decimal,
    particle_velocity: Decimal,
    angle_sinus: Decimal = MathConstants.DEFAULT_SINUS.value,
) -> Decimal:

    magnetic_induction: Decimal = lorentz_force / (electric_charge * particle_velocity * angle_sinus)
    return magnetic_induction

#endregion
