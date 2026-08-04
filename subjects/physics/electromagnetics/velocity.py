from decimal import Decimal


#region Particle velocity

def get_particle_velocity_by_lorentz_force_and_electric_charge_and_magnetic_induction_and_angle_sinus(
    *,
    lorentz_force: Decimal,
    electric_charge: Decimal,
    magnetic_induction: Decimal,
    angle_sinus: Decimal,
) -> Decimal:

    particle_velocity: Decimal = lorentz_force / (electric_charge * magnetic_induction * angle_sinus)
    return particle_velocity

#endregion
