from decimal import Decimal


#region Electric charge

def get_electric_charge_by_lorentz_force_and_particle_velocity_and_magnetic_induction(
    *,
    lorentz_force: Decimal,
    particle_velocity: Decimal,
    magnetic_induction: Decimal,
) -> Decimal:

    electric_charge: Decimal = lorentz_force / (particle_velocity * magnetic_induction)
    return electric_charge

#endregion
