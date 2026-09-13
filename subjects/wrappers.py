from decimal import Decimal


from subjects.math.geometry.area import get_trapezoidal_figure_area_by_trapezoidal_figure_bases_and_trapezoidal_figure_height
from subjects.math.geometry.base import get_trapezoidal_figure_base_by_trapezoidal_figure_area_and_trapezoidal_figure_given_base_and_trapezoidal_figure_height
from subjects.math.geometry.height import get_trapezoidal_figure_height_by_trapezoidal_figure_area_and_trapezoidal_figure_upper_base_and_trapezoidal_figure_lower_base
from subjects.math.geometry.side import get_triangle_opposite_side_by_cosine_theorem

from subjects.physics.mechanics.mass import get_general_mass_by_general_density_and_general_volume

from subjects.physics.mechanics.force import get_resultant_force_by_general_mass_and_general_acceleration


#region Geometry

def get_triangle_hypotenuse_by_two_legs(
    *,
    first_leg: Decimal,
    second_leg: Decimal,
) -> Decimal:

    triangle_hypotenuse: Decimal = get_triangle_opposite_side_by_cosine_theorem(
        first_side=first_leg,
        second_side=second_leg,
        angle_cosinus=Decimal("0")
    )

    return triangle_hypotenuse


def get_triangle_area_by_triangle_base_and_triangle_height(
    *,
    triangle_base: Decimal,
    triangle_height: Decimal,
) -> Decimal:

    triangle_area: Decimal = get_trapezoidal_figure_area_by_trapezoidal_figure_bases_and_trapezoidal_figure_height(
        trapezoidal_figure_height=triangle_height,
        trapezoidal_figure_lower_base=triangle_base,
        trapezoidal_figure_upper_base=Decimal("0"),
    )

    return triangle_area


def get_parallelogram_area_by_parallelogram_base_and_parallelogram_height(
    *,
    parallelogram_base: Decimal,
    parallelogram_height: Decimal,
) -> Decimal:

    parallelogram_area: Decimal = get_trapezoidal_figure_area_by_trapezoidal_figure_bases_and_trapezoidal_figure_height(
        trapezoidal_figure_height=parallelogram_height,
        trapezoidal_figure_lower_base=parallelogram_base,
        trapezoidal_figure_upper_base=parallelogram_base,
    )

    return parallelogram_area


def get_trapezoid_area_by_trapezoid_bases_and_trapezoid_height(
    *,
    trapezoid_upper_base: Decimal,
    trapezoid_lower_base: Decimal,
    trapezoid_height: Decimal,
) -> Decimal:

    parallelogram_area: Decimal = get_trapezoidal_figure_area_by_trapezoidal_figure_bases_and_trapezoidal_figure_height(
        trapezoidal_figure_height=trapezoid_height,
        trapezoidal_figure_lower_base=trapezoid_lower_base,
        trapezoidal_figure_upper_base=trapezoid_upper_base,
    )

    return parallelogram_area


def get_triangle_base_by_triangle_area_and_triangle_height(
    *,
    triangle_area: Decimal,
    triangle_height: Decimal,
) -> Decimal:

    triangle_base: Decimal = get_trapezoidal_figure_base_by_trapezoidal_figure_area_and_trapezoidal_figure_given_base_and_trapezoidal_figure_height(
        trapezoidal_figure_area=triangle_area,
        trapezoidal_figure_given_base=Decimal("0"),
        trapezoidal_figure_height=triangle_height,
    )

    return triangle_base


def get_parallelogram_base_by_parallelogram_area_and_parallelogram_height(
    *,
    parallelogram_area: Decimal,
    parallelogram_height: Decimal,
) -> Decimal:

    parallelogram_base: Decimal = get_trapezoidal_figure_base_by_trapezoidal_figure_area_and_trapezoidal_figure_given_base_and_trapezoidal_figure_height(
        trapezoidal_figure_area=parallelogram_area,
        trapezoidal_figure_given_base=Decimal("0"),
        trapezoidal_figure_height=parallelogram_height,
    ) / Decimal("2")

    return parallelogram_base


def get_trapezoid_base_by_trapezoid_area_and_trapezoid_given_base_and_trapezoid_height(
    *,
    trapezoid_area: Decimal,
    trapezoid_given_base: Decimal,
    trapezoid_height: Decimal,
) -> Decimal:

    trapezoid_base: Decimal = get_trapezoidal_figure_base_by_trapezoidal_figure_area_and_trapezoidal_figure_given_base_and_trapezoidal_figure_height(
        trapezoidal_figure_area=trapezoid_area,
        trapezoidal_figure_given_base=trapezoid_given_base,
        trapezoidal_figure_height=trapezoid_height,
    )

    return trapezoid_base


def get_triangle_height_by_triangle_area_and_triangle_base(
    *,
    triangle_area: Decimal,
    triangle_base: Decimal,
) -> Decimal:

    triangle_height: Decimal = get_trapezoidal_figure_height_by_trapezoidal_figure_area_and_trapezoidal_figure_upper_base_and_trapezoidal_figure_lower_base(
        trapezoidal_figure_area=triangle_area,
        trapezoidal_figure_lower_base=triangle_base,
        trapezoidal_figure_upper_base=Decimal("0"),
    )

    return triangle_height


def get_parallelogram_height_by_parallelogram_area_and_parallelogram_base(
    *,
    parallelogram_area: Decimal,
    parallelogram_base: Decimal,
) -> Decimal:

    parallelogram_height: Decimal = get_trapezoidal_figure_height_by_trapezoidal_figure_area_and_trapezoidal_figure_upper_base_and_trapezoidal_figure_lower_base(
        trapezoidal_figure_area=parallelogram_area,
        trapezoidal_figure_lower_base=parallelogram_base,
        trapezoidal_figure_upper_base=parallelogram_base,
    )

    return parallelogram_height


def get_trapezoid_height_by_trapezoid_area_and_trapezoid_bases(
    *,
    trapezoid_area: Decimal,
    trapezoid_lower_base: Decimal,
    trapezoid_upper_base: Decimal,
) -> Decimal:

    trapezoid_height: Decimal = get_trapezoidal_figure_height_by_trapezoidal_figure_area_and_trapezoidal_figure_upper_base_and_trapezoidal_figure_lower_base(
        trapezoidal_figure_area=trapezoid_area,
        trapezoidal_figure_lower_base=trapezoid_lower_base,
        trapezoidal_figure_upper_base=trapezoid_upper_base,
    )

    return trapezoid_height

#endregion


#region Mechanics

def get_archimedes_force_by_fluid_density_and_submerged_volume_and_gravity_acceleration(
    *,
    fluid_density: Decimal,
    submerged_volume: Decimal,
    gravity_acceleration: Decimal,
) -> Decimal:

    displaced_fluid_mass: Decimal = get_general_mass_by_general_density_and_general_volume(
        general_density=fluid_density,
        general_volume=submerged_volume,
    )

    archimedes_force: Decimal = get_resultant_force_by_general_mass_and_general_acceleration(
        general_mass=displaced_fluid_mass,
        general_acceleration=gravity_acceleration,
    )

    return archimedes_force

#endregion
