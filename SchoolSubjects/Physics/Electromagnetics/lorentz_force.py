from decimal import Decimal


#region Lorentz force

def get_lorentz_force_by_electric_charge_and_particle_velocity_and_magnetic_induction(
    *,
    electric_charge: Decimal,
    particle_velocity: Decimal,
    magnetic_induction: Decimal,
) -> Decimal:

    lorentz_force: Decimal = electric_charge * particle_velocity * magnetic_induction
    return lorentz_force

#endregion
