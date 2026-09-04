from decimal import Decimal

from subjects.math.algebra.coordinate import get_linear_graph_x_coordinate, get_quadratic_graph_x_coordinate
from subjects.math.geometry.side import get_triangle_side_by_cosine_theorem
from subjects.physics.mechanics.mass import get_general_mass_by_general_density_and_general_volume
from subjects.physics.mechanics.force import get_resultant_force_by_general_mass_and_general_acceleration


#region Algebra

def solve_linear_equation(
    *,
    linear_equation_linear_coefficient: Decimal,
    linear_equation_constant_coefficient: Decimal,
) -> Decimal:

    linear_equation_root: Decimal = get_linear_graph_x_coordinate(
        linear_graph_y_coordinate=Decimal("0"),
        linear_graph_linear_coefficient=linear_equation_linear_coefficient,
        linear_graph_constant_coefficient=linear_equation_constant_coefficient,
    )

    return linear_equation_root


def solve_quadratic_equation(
    *,
    quadraric_equation_quadratic_coefficient: Decimal,
    quadraric_equation_linear_coefficient: Decimal,
    quadraric_equation_constant_coefficient: Decimal,
) -> list[Decimal]:

    quadratic_equation_roots: list[Decimal] = get_quadratic_graph_x_coordinate(
        quadratic_graph_y_coordinate=Decimal("0"),
        quadratic_graph_quadratic_coefficient=quadraric_equation_quadratic_coefficient,
        quadratic_graph_linear_coefficient=quadraric_equation_linear_coefficient,
        quadratic_graph_constant_coefficient=quadraric_equation_constant_coefficient,
    )

    return quadratic_equation_roots

#endregion


#region Geometry

def get_triangle_hypotenuse_by_two_catets(
    *,
    first_catet: Decimal,
    second_catet: Decimal,
) -> Decimal:

    triangle_hypotenuse: Decimal = get_triangle_side_by_cosine_theorem(
        first_side=first_catet,
        second_side=second_catet,
        angle_cosinus=Decimal("0")
    )

    return triangle_hypotenuse

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
