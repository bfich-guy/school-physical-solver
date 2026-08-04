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

#endregion
