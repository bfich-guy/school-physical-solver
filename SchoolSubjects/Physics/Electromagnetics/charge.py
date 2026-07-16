from decimal import Decimal


#region Electric charge

def get_electric_charge_by_lorentz_force_and_particle_velocity_and_magnetic_induction_and_angle_sinus(
    *,
    lorentz_force: Decimal,
    particle_velocity: Decimal,
    magnetic_induction: Decimal,
    angle_sinus: Decimal = MathConstants.DEFAULT_SINUS.value,
) -> Decimal:

    electric_charge: Decimal = lorentz_force / (particle_velocity * magnetic_induction * angle_sinus)
    return electric_charge

#endregion
