from decimal import Decimal

from System.config import GRAVITATIONAL_ACCELERATION


#region General density

def get_general_density_by_general_mass_and_general_volume(
    *,
    general_mass: Decimal,
    general_volume: Decimal,
) -> Decimal:

    general_density: Decimal = general_mass / general_volume
    return general_density

#endregion

