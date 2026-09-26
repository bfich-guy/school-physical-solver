from enum import Enum
from decimal import Decimal


#region System

class Folders(Enum):
    TEMPLATES = "templates"
    STATIC = "static"

    ABOUTUS = "aboutusfolder"

    MATH = "mathfolder"
    PHYSICS = "physicsfolder"

    ALGEBRA = "algebrafolder"
    GEOMETRY = "geometryfolder"

    ELECTROMAGNETICS = "electromagneticsfolder"
    MECHANICS = "mechanicsfolder"
    THERMODYNAMICS = "thermodynamicsfolder"


class Files(Enum):
    INDEX = "index"
    ANSWER = "answer"

    USAGEPOLICY = "usagepolicy"
    FAQ = "faq"
    EXTRAINFO = "extrainfo"

    MATH = "math"
    PHYSICS = "physics"

    ALGEBRA = "algebra"
    GEOMETRY = "geometry"

    ELECTROMAGNETICS = "electromagnetics"
    MECHANICS = "mechanics"
    THERMODYNAMICS = "thermodynamics"


class FileExtenstions(Enum):
    HTML = "html"
    PY = "py"
    PNG = "png"


class DotenvServerKeys(Enum):
    APP_NAME = "APP_NAME"
    APP_HOST = "APP_HOST"
    APP_PORT = "APP_POST"
    APP_RELOAD = "APP_RELOAD"

#endregion


#region Server

class Mounts(Enum):
    STATIC = f"/{Folders.STATIC.value}"    


class Prefix(Enum):
    INDEX = ""

    MATH = f"/{Files.MATH.value}"
    PHYSICS = f"/{Files.PHYSICS.value}"

    ALGEBRA = f"/{Files.MATH.value}/{Files.ALGEBRA.value}"
    GEOMETRY = f"/{Files.MATH.value}/{Files.GEOMETRY.value}"

    ELECTROMAGNETICS = f"/{Files.PHYSICS.value}/{Files.ELECTROMAGNETICS.value}"
    MECHANICS = f"/{Files.PHYSICS.value}/{Files.MECHANICS.value}"
    THERMODYNAMICS = f"/{Files.PHYSICS.value}/{Files.THERMODYNAMICS.value}"


class Endpoints(Enum):
    INDEX = f"/"
    ANSWER = f"/{Files.ANSWER.value}"

    USAGEPOLICY = f"/{Files.USAGEPOLICY.value}"
    FAQ = f"/{Files.FAQ.value}"
    EXTRAINFO = f"/{Files.EXTRAINFO.value}"

    MATH = f"/{Files.MATH.value}"
    PHYSICS = f"/{Files.PHYSICS.value}"

    ALGEBRA = f"/{Files.ALGEBRA.value}"
    GEOMETRY = f"/{Files.GEOMETRY.value}"

    ELECTROMAGNETICS = f"/{Files.ELECTROMAGNETICS.value}"
    MECHANICS = f"/{Files.MECHANICS.value}"
    THERMODYNAMICS = f"/{Files.THERMODYNAMICS.value}"


class Templates(Enum):
    INDEX = f"{Files.INDEX.value}.{FileExtenstions.HTML.value}"
    ANSWER = f"{Files.ANSWER.value}.{FileExtenstions.HTML.value}"

    USAGEPOLICY = f"{Folders.ABOUTUS.value}/{Files.USAGEPOLICY.value}.{FileExtenstions.HTML.value}"
    FAQ = f"{Folders.ABOUTUS.value}/{Files.FAQ.value}.{FileExtenstions.HTML.value}"
    EXTRAINFO = f"{Folders.ABOUTUS.value}/{Files.EXTRAINFO.value}.{FileExtenstions.HTML.value}"

    MATH = f"{Files.MATH.value}.{FileExtenstions.HTML.value}"
    PHYSICS = f"{Files.PHYSICS.value}.{FileExtenstions.HTML.value}"

    ALGEBRA = f"/{Folders.MATH.value}/{Files.ALGEBRA.value}.{FileExtenstions.HTML.value}"
    GEOMETRY = f"/{Folders.MATH.value}/{Files.GEOMETRY.value}.{FileExtenstions.HTML.value}"\

    ELECTROMAGNETICS = f"/{Folders.PHYSICS.value}/{Files.ELECTROMAGNETICS.value}.{FileExtenstions.HTML.value}"
    MECHANICS = f"/{Folders.PHYSICS.value}/{Files.MECHANICS.value}.{FileExtenstions.HTML.value}"
    THERMODYNAMICS = f"/{Folders.PHYSICS.value}/{Files.THERMODYNAMICS.value}.{FileExtenstions.HTML.value}" 

#endregion


#region Constants

class PhysMathConstants(Enum):
    EARTH_GRAVITY_ACCELERATION = Decimal("9.81")
    GAS_CONSTANT = Decimal("8.31446261815324")
    COULOMB_CONSTANT = Decimal("8987551792.3")


class QuantitiesNames(Enum):
    RESULTANT_FORCE = "resultant_force"
    OBJECT_MASS = "object_mass"
    OBJECT_ACCELERATION = "object_acceleration"
    HOOKES_FORCE = "hookes_force"
    SPRING_STIFFNESS = "spring_stiffness"
    SPRING_ELONGATION = "spring_elongation"
    AMONTONS_COULOMB_FORCE = "amontons_coulumb_force"
    FRICTION_COEFFICIENT = "friction_coefficient"
    NORMAL_FORCE = "normal_force"
    PRESSURE_FORCE = "pressure_force"
    MECHANICAL_PRESSURE = "mechanical_pressure"
    SURFACE_AREA = "surface_area"
    ARCHIMEDES_FORCE = "archimedes_force"
    FLUID_DENSITY = "fluid_density"
    SUBMERGED_VOLUME = "submerged_volume"
    GRAVITATIONAL_ACCELERATION = "gravitational_acceleration"
    WEIGHT_FORCE = "weight_force"
    ANGLE_COSINUS = "angle_cosinus"
    OBJECT_MOMENTUM = "object_momentum"
    OBJECT_VELOCITY = "object_velocity"
    FIRST_INITIAL_MOMENTUM = "first_initial_momentum"
    SECOND_INITIAL_MOMENTUM = "second_initital_momentum"
    FIRST_FINAL_MOMENTUM = "first_final_momentum"
    SECOND_FINAL_MOMENTUM = "second_final_momentum"
    KINETIC_ENERGY = "kinetic_energy"
    POTENTIAL_ENERGY = "potential_energy"
    HEIGHT_ABOVE_SURFACE = "height_above_surface"
    HYDROSTATIC_PRESSURE = "hydrostatic_pressure"
    FLUID_COLUMN_HEIGHT = "fluid_column_height"
    MECHANICAL_WORK = "mechanical_work"
    APPLIED_FORCE = "applied_force"
    COVERED_DISTANCE = "covered_distance"
    MECHANICAL_POWER = "mechanical_power"
    ELAPSED_TIME = "elapsed_time"
    LINEAR_ACCELERATION = "linear_acceleration"
    DELTA_VELOCITY = "delta_velocity"
    DELTA_TIME = "delta_time"
    CENTRIPETAL_ACCELERATION = "centripetal_acceleration"
    LINEAR_VELOCITY = "linear_velocity"
    ANGULAR_VELOCITY = "angular_velocity"
    TRAJECTORY_RADIUS = "trajectory_radius"

    SENSIBLE_HEAT = "sensible_heat"
    SPECIFIC_HEAT = "specific_heat"
    DELTA_TEMPERATURE = "delta_temperature"
    COMBUSTION_HEAT = "combustion_heat"
    SPECIFIC_HEAT_OF_COMBUSTION = "specific_heat_of_combustion"
    FUSION_HEAT = "fusion_heat"
    SPECIFIC_HEAT_OF_FUSION = "specific_heat_of_fusion"
    VAPORIZATION_HEAT = "vaporization_heat"
    SPECIFIC_HEAT_OF_VAPORIZATION = "specific_heat_of_vaporization"
    GAS_PRESSURE = "gas_pressure"
    GAS_VOLUME = "gas_volume"
    GAS_MOLES = "gas_moles"
    GAS_TEMPERATURE = "gas_temperature"
    OBJECT_MOLES = "object_moles"
    OBJECT_MOLAR_MASS = "object_molar_mass"

    ELECTRIC_VOLTAGE = "electric_voltage"
    ELECTRIC_CURRENT = "electric_current"
    ELECTRIC_RESISTANCE = "electric_resistance"
    ELECTRIC_POWER = "electric_power"
    ELECTROMOTIVE_FORCE = "electromotive_force"
    ELECTRIC_INTERNAL_RESISTANCE = "electric_internal_resistance"
    JOULE_HEAT = "joule_heat"
    HEATING_TIME = "heating_time"
    ELECTROSTATIC_FORCE = "electrostatic_force"
    PARTICLE_CHARGES = "particle_charges"
    PARTICLE_CHARGE = "particle_charge"
    DISTANCE_BETWEEN_CHARGES = "distance_between_charges"
    CONDUCTOR_ELECTRIC_RESISTIVITY = "electric_resistivity"
    CONDUCTOR_LENGTH = "conductor_length"
    CONDUCTOR_ELECTRIC_RESISTANCE = "conductor_electric_resistance"
    CONDUCTOR_CROSS_SECTIONAL_AREA = "conductor_cross_sectional_area"
    AMPERES_FORCE = "amperes_force"
    LORENTZ_FORCE = "lorentz_force"
    MAGNETIC_INDUCTION = "magnetic_induction"
    ANGLE_SINUS = "angle_sinus"
    PARTICLE_VELOCITY = "particle_velocity"
    DELTA_MAGNETIC_FLUX = "delta_magnetic_flux"
    MAGNETIC_FLUX = "magnetic_flux"
    CONTOUR_AREA = "contour_area"



global_error_message: str = (
    "Увы, но Физмат-калькулятор заметил математические ошибки в Вашем вводе. "
    "Проверьте, чтобы в Вашем следующем вводе не содержалось деление на ноль или отрицательных корней."
    "Так же убедитесь, что вводите именно столько чисел, сколько положено в формуле."
)



#endregion
