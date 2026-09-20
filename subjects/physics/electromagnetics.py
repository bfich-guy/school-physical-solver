from decimal import Decimal


#region Electricity

def get_conductor_cross_sectional_area_by_conductor_electric_resistivity_and_conductor_length_and_electric_conductor_resistance(
    *,
    conductor_electric_resistivity: Decimal,
    conductor_length: Decimal,
    electric_conductor_resistance: Decimal,
) -> Decimal:

    conductor_cross_sectional_area: Decimal = (conductor_electric_resistivity * conductor_length) / electric_conductor_resistance
    return conductor_cross_sectional_area


def get_electric_charge_by_lorentz_force_and_particle_velocity_and_magnetic_induction_and_angle_sinus(
    *,
    lorentz_force: Decimal,
    particle_velocity: Decimal,
    magnetic_induction: Decimal,
    angle_sinus: Decimal,
) -> Decimal:

    electric_charge: Decimal = lorentz_force / (particle_velocity * magnetic_induction * angle_sinus)
    return electric_charge


def get_electric_current_by_watts_law(
    *,
    electric_power: Decimal,
    electric_voltage: Decimal,
) -> Decimal:

    electric_current: Decimal = electric_power / electric_voltage
    return electric_current


def get_electric_current_by_ohms_law(
    *,
    electric_voltage: Decimal,
    electric_resistance: Decimal,
) -> Decimal:

    electric_current: Decimal = electric_voltage / electric_resistance
    return electric_current


def get_electric_current_by_electromotive_force_and_electric_voltage_and_electric_internal_resistance(
    *,
    electromotive_force: Decimal,
    electric_voltage: Decimal,
    electric_internal_resistance: Decimal,
) -> Decimal:

    electric_current: Decimal = (electromotive_force - electric_voltage) / electric_internal_resistance
    return electric_current


def get_electric_current_by_ampere_force_and_magnetic_induction_and_conductor_length_and_angle_sinus(
    *,
    ampere_force: Decimal,
    magnetic_induction: Decimal,
    conductor_length: Decimal,
    angle_sinus: Decimal,
) -> Decimal:
    
    electric_current: Decimal = ampere_force / (magnetic_induction * conductor_length * angle_sinus)
    return electric_current


def get_electromotive_force_by_electric_voltage_and_electric_current_and_electric_internal_resistance(
    *,
    electric_voltage: Decimal,
    electric_current: Decimal,
    electric_internal_resistance: Decimal,
) -> Decimal:

    electromotive_force: Decimal = electric_voltage + (electric_current * electric_internal_resistance)
    return electromotive_force


def get_conductor_length_by_electric_conductor_resistance_and_conductor_cross_sectional_area_and_conductor_electric_resistivity(
    *,
    electric_conductor_resistance: Decimal,
    conductor_cross_sectional_area: Decimal,
    conductor_electric_resistivity: Decimal,
) -> Decimal:

    conductor_length: Decimal = (electric_conductor_resistance * conductor_cross_sectional_area) / conductor_electric_resistivity
    return conductor_length


def get_electric_power_by_watts_law(
    *,
    electric_voltage: Decimal,
    electric_current: Decimal,
) -> Decimal:

    electric_power: Decimal = electric_voltage * electric_current
    return electric_power


def get_electric_power_by_joule_lenz_law(
    *,
    joule_heat: Decimal,
    heating_duration: Decimal,
) -> Decimal:

    electric_power: Decimal = joule_heat / heating_duration
    return electric_power


def get_electric_external_resistance_by_ohms_law(
    *,
    electric_voltage: Decimal,
    electric_current: Decimal,
) -> Decimal:

    electric_external_resistance: Decimal = electric_voltage / electric_current
    return electric_external_resistance


def get_electric_conductor_resistance_by_conductor_electric_resistivity_and_conductor_length_and_conductor_cross_sectional_area(
    *,
    conductor_electric_resistivity: Decimal,
    conductor_length: Decimal,
    conductor_cross_sectional_area: Decimal,
) -> Decimal:

    electric_conductor_resistance: Decimal = (conductor_electric_resistivity * conductor_length) / conductor_cross_sectional_area
    return electric_conductor_resistance


def get_conductor_electric_resistivity_by_electric_conductor_resistance_and_conductor_cross_sectional_area_and_conductor_length(
    *,
    electric_conductor_resistance: Decimal,
    conductor_cross_sectional_area: Decimal,
    conductor_length: Decimal,
) -> Decimal:

    conductor_electric_resistivity: Decimal = (electric_conductor_resistance * conductor_cross_sectional_area) / conductor_length
    return conductor_electric_resistivity


def get_electric_internal_resistance_by_electromotive_force_and_electric_voltage_and_electric_current(
    *,
    electromotive_force: Decimal,
    electric_voltage: Decimal,
    electric_current: Decimal,
) -> Decimal:

    electric_internal_resistance: Decimal = (electromotive_force - electric_voltage) / electric_current
    return electric_internal_resistance


def get_electric_voltage_by_watts_law(
    *,
    electric_current: Decimal,
    electric_power: Decimal,
) -> Decimal:

    electric_voltage: Decimal = electric_power / electric_current
    return electric_voltage


def get_electric_voltage_by_ohms_law(
    *,
    electric_current: Decimal,
    electric_external_resistance: Decimal,
) -> Decimal:

    electric_voltage: Decimal = electric_current * electric_external_resistance
    return electric_voltage


def get_electric_voltage_by_electromotive_force_and_electric_current_and_electric_internal_resistance(
    *,
    electromotive_force: Decimal,
    electric_current: Decimal,
    electric_internal_resistance: Decimal,
) -> Decimal:

    electric_voltage: Decimal = electromotive_force - (electric_current * electric_internal_resistance)
    return electric_voltage

#endregion


#region Magnetism

def get_ampere_force_by_magnetic_induction_and_electric_current_and_conductor_length_and_angle_sinus(
    *,
    magnetic_induction: Decimal,
    electric_current: Decimal,
    conductor_length: Decimal,
    angle_sinus: Decimal,
) -> Decimal:

    ampere_force: Decimal = magnetic_induction * electric_current * conductor_length * angle_sinus
    return ampere_force


def get_lorentz_force_by_electric_charge_and_particle_velocity_and_magnetic_induction_and_angle_sinus(
    *,
    electric_charge: Decimal,
    particle_velocity: Decimal,
    magnetic_induction: Decimal,
    angle_sinus: Decimal,
) -> Decimal:

    lorentz_force: Decimal = electric_charge * particle_velocity * magnetic_induction * angle_sinus
    return lorentz_force


def get_magnetic_induction_by_ampere_force_and_electric_current_and_conductor_length_and_angle_sinus(
    *,
    ampere_force: Decimal,
    electric_current: Decimal,
    conductor_length: Decimal,
    angle_sinus: Decimal,
) -> Decimal:
    
    magnetic_induction: Decimal = ampere_force / (electric_current * conductor_length * angle_sinus)
    return magnetic_induction


def get_magnetic_induction_by_lorentz_force_and_electric_charge_and_particle_velocity_and_angle_sinus(
    *,
    lorentz_force: Decimal,
    electric_charge: Decimal,
    particle_velocity: Decimal,
    angle_sinus: Decimal,
) -> Decimal:

    magnetic_induction: Decimal = lorentz_force / (electric_charge * particle_velocity * angle_sinus)
    return magnetic_induction


def get_conductor_length_by_ampere_force_and_magnetic_induction_and_electric_current_and_angle_sinus(
    *,
    ampere_force: Decimal,
    magnetic_induction: Decimal,
    electric_current: Decimal,
    angle_sinus: Decimal,
) -> Decimal:
    
    conductor_length: Decimal = ampere_force / (magnetic_induction * electric_current * angle_sinus)
    return conductor_length


def get_angle_sinus_by_ampere_force_and_magnetic_induction_and_electric_current_and_conductor_length(
    *,
    ampere_force: Decimal,
    magnetic_induction: Decimal,
    electric_current: Decimal,
    conductor_length: Decimal,
) -> Decimal:

    angle_sinus: Decimal = ampere_force / (magnetic_induction * electric_current * conductor_length)
    return angle_sinus


def get_angle_sinus_by_lorentz_force_and_electric_charge_and_particle_velocity_and_magnetic_induction(
    *,
    lorentz_force: Decimal,
    electric_charge: Decimal,
    particle_velocity: Decimal,
    magnetic_induction: Decimal,
) -> Decimal:

    angle_sinus: Decimal = lorentz_force / (electric_charge * particle_velocity * magnetic_induction)
    return angle_sinus


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
