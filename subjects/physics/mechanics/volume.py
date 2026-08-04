from decimal import Decimal


#region General volume

def get_general_volume_by_general_mass_and_general_density(
    *,
    general_mass: Decimal,
    general_density: Decimal,
) -> Decimal:

    general_volume: Decimal = general_mass / general_density
    return general_volume

#endregion
