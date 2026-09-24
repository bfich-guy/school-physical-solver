from decimal import Decimal

from system.utils.calculators import decimal_product


#region Ohms Law

def get_electric_voltage_by_ohms_law(
    *,
    electric_current: Decimal,
    electric_resistance: Decimal,
) -> Decimal:

    electric_voltage: Decimal = electric_current * electric_resistance
    return electric_voltage


def get_electric_current_by_ohms_law(
    *,
    electric_voltage: Decimal,
    electric_resistance: Decimal,
) -> Decimal:

    electric_current: Decimal = electric_voltage / electric_resistance
    return electric_current


def get_electric_resistance_by_ohms_law(
    *,
    electric_voltage: Decimal,
    electric_current: Decimal,
) -> Decimal:

    electric_resistance: Decimal = electric_voltage / electric_current
    return electric_resistance


def get_electromotive_force_by_ohms_full_law(
    *,
    electric_voltage: Decimal,
    electric_current: Decimal,
    electric_internal_resistance: Decimal,
) -> Decimal:

    electromotive_force: Decimal = electric_voltage + (electric_current * electric_internal_resistance)
    return electromotive_force


def get_electric_voltage_by_ohms_full_law(
    *,
    electromotive_force: Decimal,
    electric_current: Decimal,
    electric_internal_resistance: Decimal,
) -> Decimal:

    electric_voltage: Decimal = electromotive_force - (electric_current * electric_internal_resistance)
    return electric_voltage


def get_electric_current_by_ohms_full_law(
    *,
    electromotive_force: Decimal,
    electric_voltage: Decimal,
    electric_internal_resistance: Decimal,
) -> Decimal:

    electric_current: Decimal = (electromotive_force - electric_voltage) / electric_internal_resistance
    return electric_current


def get_electric_internal_resistance_by_ohms_full_law(
    *,
    electromotive_force: Decimal,
    electric_voltage: Decimal,
    electric_current: Decimal,
) -> Decimal:

    electric_internal_resistance: Decimal = (electromotive_force - electric_voltage) / electric_current
    return electric_internal_resistance

#endregion


#region Watts law

def get_electric_power_by_watts_law(
    *,
    electric_voltage: Decimal,
    electric_current: Decimal,
) -> Decimal:

    electric_power: Decimal = electric_voltage * electric_current
    return electric_power


def get_electric_voltage_by_watts_law(
    *,
    electric_power: Decimal,
    electric_current: Decimal,
) -> Decimal:

    electric_voltage: Decimal = electric_power / electric_current
    return electric_voltage


def get_electric_current_by_watts_law(
    *,
    electric_power: Decimal,
    electric_voltage: Decimal,
) -> Decimal:

    electric_current: Decimal = electric_power / electric_voltage
    return electric_current

#endregion


#region Joule-Lenz law

def get_joule_heat_by_joule_lenz_law(
    *,
    electric_power: Decimal,
    heating_duration: Decimal,
) -> Decimal:

    joule_heat: Decimal = electric_power * heating_duration
    return joule_heat


def get_electric_power_by_joule_lenz_law(
    *,
    joule_heat: Decimal,
    heating_duration: Decimal,
) -> Decimal:

    electric_power: Decimal = joule_heat / heating_duration
    return electric_power


def get_heating_duration_by_joule_lenz_law(
    *,
    joule_heat: Decimal,
    electric_power: Decimal,
) -> Decimal:

    heating_duration: Decimal = joule_heat / electric_power
    return heating_duration

#endregion


#region Coulombs law

def get_coulombs_force_by_coulombs_law(
    *,
    coulomb_constant: Decimal,
    charges_modules: list[Decimal],
    charges_distance: Decimal,
) -> Decimal:

    coulomb_force: Decimal = (coulomb_constant * decimal_product(charges_modules)) / pow(charges_distance, Decimal("2"))
    return coulomb_force


def get_charge_module_by_coulombs_law(
    *,
    coulomb_force: Decimal,
    coulomb_constant: Decimal,
    charges_distance: Decimal,
    given_charge_module: Decimal,
) -> Decimal:

    charge_module: Decimal = (coulomb_force * pow(charges_distance, Decimal("2"))) / (coulomb_constant * given_charge_module)
    return charge_module


def get_charge_distance_by_coulombs_law(
    *,
    coulomb_force: Decimal,
    coulomb_constant: Decimal,
    charge_modules: list[Decimal],
) -> Decimal:

    charge_distance: Decimal = ((coulomb_constant * decimal_product(charge_modules)) / coulomb_force).sqrt()
    return charge_distance

#endregion


#region Conductor resistance law

def get_conductor_electric_resistance_by_conductor_resistance_law(
    *,
    conductor_electric_resistivity: Decimal,
    conductor_length: Decimal,
    conductor_cross_sectional_area: Decimal,
) -> Decimal:

    conductor_electric_resistance: Decimal = (conductor_electric_resistivity * conductor_length) / conductor_cross_sectional_area
    return conductor_electric_resistance


def get_conductor_electric_resistivity_by_conductor_resistance_law(
    *,
    conductor_electric_resistance: Decimal,
    conductor_cross_sectional_area: Decimal,
    conductor_length: Decimal,
) -> Decimal:

    conductor_electric_resistivity: Decimal = (conductor_electric_resistance * conductor_cross_sectional_area) / conductor_length
    return conductor_electric_resistivity


def get_conductor_length_by_conductor_resistance_law(
    *,
    conductor_electric_resistance: Decimal,
    conductor_cross_sectional_area: Decimal,
    conductor_electric_resistivity: Decimal,
) -> Decimal:

    conductor_length: Decimal = (conductor_electric_resistance * conductor_cross_sectional_area) / conductor_electric_resistivity
    return conductor_length


def get_conductor_cross_sectional_area_by_conductor_resistance_law(
    *,
    conductor_electric_resistivity: Decimal,
    conductor_length: Decimal,
    conductor_electric_resistance: Decimal,
) -> Decimal:

    conductor_cross_sectional_area: Decimal = (conductor_electric_resistivity * conductor_length) / conductor_electric_resistance
    return conductor_cross_sectional_area

#endregion


#region Amperes law

def get_ampere_force_by_amperes_law(
    *,
    magnetic_induction: Decimal,
    electric_current: Decimal,
    conductor_length: Decimal,
    angle_sinus: Decimal,   
) -> Decimal:

    ampere_force: Decimal = magnetic_induction * electric_current * conductor_length * angle_sinus
    return ampere_force


def get_magnetic_induction_by_amperes_law(
    *,
    ampere_force: Decimal,
    electric_current: Decimal,
    conductor_length: Decimal,
    angle_sinus: Decimal,
) -> Decimal:

    magnetic_induction: Decimal = ampere_force / (electric_current * conductor_length * angle_sinus)
    return magnetic_induction


def get_electric_current_by_amperes_law(
    *,
    ampere_force: Decimal,
    magnetic_induction: Decimal,
    conductor_length: Decimal,
    angle_sinus: Decimal,
) -> Decimal:

    electric_current: Decimal = ampere_force / (magnetic_induction * conductor_length * angle_sinus)
    return electric_current


def get_conductor_length_by_amperes_law(
    *,
    ampere_force: Decimal,
    magnetic_induction: Decimal,
    electric_current: Decimal,
    angle_sinus: Decimal,
) -> Decimal:

    conductor_length: Decimal = ampere_force / (electric_current * magnetic_induction * angle_sinus)
    return conductor_length


def get_angle_sinus_by_amperes_law(
    *,
    ampere_force: Decimal,
    magnetic_induction: Decimal,
    electric_current: Decimal,
    conductor_length: Decimal,
) -> Decimal:

    angle_sinus: Decimal = ampere_force / (magnetic_induction * electric_current * conductor_length)
    return angle_sinus

#endregion


#region Lorentz law

def get_lorentz_force_by_lorentz_law(
    *,
    particle_charge: Decimal,
    particle_velocity: Decimal,
    magnetic_induction: Decimal,
    angle_sinus: Decimal,
) -> Decimal:

    lorentz_force: Decimal = particle_charge * particle_velocity * magnetic_induction * angle_sinus
    return lorentz_force


def get_particle_charge_by_lorentz_law(
    *,
    lorentz_force: Decimal,
    particle_velocity: Decimal,
    magnetic_induction: Decimal,
    angle_sinus: Decimal,
) -> Decimal:

    particle_charge: Decimal = lorentz_force / (particle_velocity * magnetic_induction * angle_sinus)
    return particle_charge


def get_particle_velocity_by_lorentz_law(
    *,
    lorentz_force: Decimal,
    particle_charge: Decimal,
    magnetic_induction: Decimal,
    angle_sinus: Decimal,
) -> Decimal:

    particle_velocity: Decimal = lorentz_force / (particle_charge * magnetic_induction * angle_sinus)
    return particle_velocity


def get_magnetic_induction_by_lorentz_law(
    *,
    lorentz_force: Decimal,
    particle_charge: Decimal,
    particle_velocity: Decimal,
    angle_sinus: Decimal,
) -> Decimal:

    magnetic_induction: Decimal = lorentz_force / (particle_charge * particle_velocity * angle_sinus)
    return magnetic_induction


def get_angle_sinus_by_lorentz_law(
    *,
    lorentz_force: Decimal,
    particle_charge: Decimal,
    particle_velocity: Decimal,
    magnetic_induction: Decimal,
) -> Decimal:

    angle_sinus: Decimal = lorentz_force / (particle_charge * particle_velocity * magnetic_induction)
    return angle_sinus

#endregion


#region Faradays law

def get_electromotive_force_by_faradays_law(
    *,
    delta_magnetic_flux: Decimal,
    delta_duration: Decimal,
) -> Decimal:

    electromotive_force: Decimal = -(delta_magnetic_flux / delta_duration)
    return electromotive_force


def get_delta_magnetic_flux_by_faradays_law(
    *,
    electromotive_force: Decimal,
    delta_duration: Decimal,
) -> Decimal:

    delta_magnetic_flux: Decimal = -(electromotive_force * delta_duration)
    return delta_magnetic_flux


def get_delta_duration_by_faradays_law(
    *,
    electromotive_force: Decimal,
    delta_magnetic_flux: Decimal,
) -> Decimal:

    delta_duration: Decimal = -(delta_magnetic_flux / electromotive_force)
    return delta_duration

#endregion


#region Magnetic flux law

def get_magnetic_flux_by_magnetic_flux_law(
    *,
    magnetic_induction: Decimal,
    contour_area: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    magnetic_flux: Decimal = magnetic_induction * contour_area * angle_cosinus
    return magnetic_flux


def get_magnetic_induction_by_magnetic_flux_law(
    *,
    magnetic_flux: Decimal,
    contour_area: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    magnetic_induction: Decimal = magnetic_flux / (contour_area * angle_cosinus)
    return magnetic_induction


def get_contour_area_by_magnetic_flux_law(
    *,
    magnetic_flux: Decimal,
    magnetic_induction: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    contour_area: Decimal = magnetic_flux / (magnetic_induction * angle_cosinus)
    return contour_area


def get_angle_cosinus_by_magnetic_flux_law(
    *,
    magnetic_flux: Decimal,
    magnetic_induction: Decimal,
    contour_area: Decimal,
) -> Decimal:

    angle_cosinus: Decimal = magnetic_flux / (magnetic_induction * contour_area)
    return angle_cosinus

#endregion
