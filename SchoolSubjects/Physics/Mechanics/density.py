from decimal import Decimal

#region Density

def get_density_by_mass_and_volume(
    *,
    mass: Decimal,
    volume: Decimal,
) -> Decimal:

    density: Decimal = mass / volume
    return density

#endregion
