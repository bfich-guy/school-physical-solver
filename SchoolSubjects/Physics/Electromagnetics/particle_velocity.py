from decimal import Decimal


#region Particle velocity

def get_particle_velocity_by_lorentz_force_and_electric_charge_and_magnetic_induction(
    *,
    lorentz_force: Decimal,
    electric_charge: Decimal,
    magnetic_induction: Decimal,
) -> Decimal:

    particle_velocity: Decimal = lorentz_force / (electric_charge * magnetic_induction)
    return particle_velocity

#endregion
