from decimal import Decimal


#region Conductor length

def get_conductor_length_by_general_resistance_and_cross_sectional_area_and_electric_resistivity(
    *,
    general_resistance: Decimal,
    cross_sectional_area: Decimal,
    electric_resistivity: Decimal,
) -> Decimal:

    conductor_length: Decimal = (general_resistance * cross_sectional_area) / electric_resistivity
    return conductor_length


def get_conductor_length_by_ampere_force_and_magnetic_induction_and_electric_current_and_angle_sinus(
    *,
    ampere_force: Decimal,
    magnetic_induction: Decimal,
    electric_current: Decimal,
    angle_sinus: Decimal,
) -> Decimal:
    
    conductor_length: Decimal = ampere_force / (magnetic_induction * electric_current * angle_sinus)
    return conductor_length

#endregion
