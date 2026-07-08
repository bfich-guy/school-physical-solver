from decimal import Decimal

#region Volume

def get_volume_by_mass_and_density(
    *,
    mass: Decimal,
    density: Decimal,
) -> Decimal:

    volume: Decimal = mass / density
    return volume

#endregion
