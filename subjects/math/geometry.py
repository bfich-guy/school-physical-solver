from decimal import Decimal

from system.utils.calculators import decimal_sum, decimal_product


#region Circles

def get_circle_area_by_circle_radius(
    *,
    pi: Decimal,
    circle_radius: Decimal,
) -> Decimal:

    circle_area: Decimal = pi * pow(circle_radius, Decimal("2"))
    return circle_area


def get_circle_area_by_circle_diameter(
    *,
    pi: Decimal,
    circle_diameter: Decimal,
) -> Decimal:

    circle_area: Decimal = (pi * pow(circle_diameter, Decimal("2"))) / Decimal("4")
    return circle_area


def get_circumference_by_circle_radius(
    *,
    pi: Decimal,
    circle_radius: Decimal,
) -> Decimal:

    circumference: Decimal = Decimal("2") * pi * circle_radius
    return circumference


def get_circumference_by_circle_diameter(
    *,
    pi: Decimal,
    circle_diameter: Decimal,
) -> Decimal:

    circumference: Decimal = pi * circle_diameter
    return circumference


def get_circle_radius_by_circle_area(
    *,
    pi: Decimal,
    circle_area: Decimal,
) -> Decimal:

    circle_radius: Decimal = (circle_area / pi).sqrt()
    return circle_radius


def get_circle_radius_by_circumference(
    *,
    pi: Decimal,
    circumference: Decimal,
) -> Decimal:

    circle_radius: Decimal = circumference / (Decimal("2") * pi)
    return circle_radius


def get_triangle_inradius_by_triangle_area_and_triangle_perimeter(
    *,
    triangle_area: Decimal,
    triangle_perimeter: Decimal,
) -> Decimal:

    triangle_inradius: Decimal = (triangle_area * Decimal("2")) / triangle_perimeter
    return triangle_inradius


def get_triangle_circumradius_by_triangle_sides_and_triangle_area(
    *,
    triangle_sides: list[Decimal],
    triangle_area: Decimal,
) -> Decimal:

    triangle_circumradius: Decimal = decimal_product(triangle_sides) / (Decimal("4") * triangle_area)
    return triangle_circumradius

#endregion


#region Parallelograms

def get_parallelogram_area_by_parallelogram_base_and_parallelogram_height(
    *,
    parallelogram_base: Decimal,
    parallelogram_height: Decimal,
) -> Decimal:

    parallelogram_area: Decimal = parallelogram_base * parallelogram_height
    return parallelogram_area


def get_parallelogram_base_by_parallelogram_area_and_parallelogram_height(
    *,
    parallelogram_area: Decimal,
    parallelogram_height: Decimal,
) -> Decimal:

    parallelogram_base: Decimal = parallelogram_area / parallelogram_height
    return parallelogram_base


def get_parallelogram_height_by_parallelogram_area_and_parallelogram_base(
    *,
    parallelogram_area: Decimal,
    parallelogram_base: Decimal,
) -> Decimal:

    parallelogram_height: Decimal = parallelogram_area / parallelogram_base
    return parallelogram_height

#endregion


#region Polygons

def get_regular_polygon_perimeter_by_regular_polygon_sides_length_and_regular_polygon_sides_amount(
    *,
    regular_polygon_sides_length: Decimal,
    regular_polygon_sides_amount: Decimal,
) -> Decimal:

    regular_polygon_perimeter: Decimal = regular_polygon_sides_length * regular_polygon_sides_amount
    return regular_polygon_perimeter


def get_regular_polygon_sides_length_by_regular_polygon_perimeter_and_regular_polygon_sides_amount(
    *,
    regular_polygon_perimeter: Decimal,
    regular_polygon_sides_amount: Decimal,
) -> Decimal:

    regular_polygon_sides_length: Decimal = regular_polygon_perimeter / regular_polygon_sides_amount
    return regular_polygon_sides_length


def get_general_polygon_sides_amount_by_general_polygon_angles_sum(
    *,
    general_polygon_angles_sum: Decimal,
) -> Decimal:

    general_polygon_sides_amount: Decimal = (general_polygon_angles_sum / Decimal("180")) + Decimal("2")
    return general_polygon_sides_amount


def get_regular_polygon_sides_amount_by_regular_polygon_perimeter_and_regular_polygon_sides_length(
    *,
    regular_polygon_perimeter: Decimal,
    regular_polygon_sides_length: Decimal,
) -> Decimal:

    regular_polygon_sides_amount: Decimal = regular_polygon_perimeter / regular_polygon_sides_length
    return regular_polygon_sides_amount


def get_regular_polygon_sides_amount_by_regular_polygon_angles_sum_and_regular_polygon_angle(
    *,
    regular_polygon_angles_sum: Decimal,
    regular_polygon_angle: Decimal,
) -> Decimal:

    regular_polygon_sides_amount: Decimal = regular_polygon_angles_sum / regular_polygon_angle
    return regular_polygon_sides_amount


def get_general_polygon_angles_sum_by_general_polygon_sides_amount(
    *,
    general_polygon_sides_amount: Decimal,
) -> Decimal:

    general_polygon_angles_sum: Decimal = (general_polygon_sides_amount - Decimal("2")) * Decimal("180")
    return general_polygon_angles_sum


def get_general_polygon_angles_sum_by_general_polygon_side_length_and_general_polygon_sides_amount(
    *,
    general_polygon_sides_amount: Decimal,
    general_polygon_side_length: Decimal,
) -> Decimal:

    general_polygon_angles_sum: Decimal = general_polygon_side_length * general_polygon_sides_amount
    return general_polygon_angles_sum


def get_regular_polygon_angles_sum_by_regular_polygon_angle_and_regular_polygon_sides_amount(
    *,
    regular_polygon_angle: Decimal,
    regular_polygon_sides_amount: Decimal,
) -> Decimal:

    regular_polygon_angles_sum: Decimal = regular_polygon_angle * regular_polygon_sides_amount
    return regular_polygon_angles_sum


def get_regular_polygon_angle_by_regular_polygon_side_amount(
    *,
    regular_polygon_angles_sum: Decimal,
    regular_polygon_side_amount: Decimal,
) -> Decimal:

    regular_polygon_angle: Decimal = regular_polygon_angles_sum / regular_polygon_side_amount
    return regular_polygon_angle

#endregion


#region Trapezoids

def get_trapezoid_area_by_trapezoid_bases_and_trapezoid_height(
    *,
    trapezoid_bases: list[Decimal],
    trapezoid_height: Decimal,
) -> Decimal:

    trapezoid_area: Decimal = ((trapezoid_bases[0] + trapezoid_bases[1]) / Decimal("2")) * trapezoid_height
    return trapezoid_area


def get_trapezoid_base_by_trapezoid_area_and_trapezoid_given_base_and_trapezoid_height(
    *,
    trapezoid_area: Decimal,
    trapezoid_given_base: Decimal,
    trapezoid_height: Decimal,
) -> Decimal:

    trapezoid_base: Decimal = ((Decimal("2") * trapezoid_area) / trapezoid_height) - trapezoid_given_base
    return trapezoid_base


def get_trapezoid_height_by_trapezoid_area_and_trapezoid_bases(
    *,
    trapezoid_area: Decimal,
    trapezoid_bases: list[Decimal],
) -> Decimal:

    trapezoid_height: Decimal = (Decimal("2") * trapezoid_area) / (trapezoid_bases[0] + trapezoid_bases[1])
    return trapezoid_height

#endregion


#region Triangles

def get_triangle_area_and_triangle_base_and_triangle_height(
    *,
    triangle_base: Decimal,
    triangle_height: Decimal,
) -> Decimal:

    triangle_area: Decimal = (triangle_base * triangle_height) / Decimal("2")
    return triangle_area


def get_triangle_area_by_heron_theorem(
    *,
    triangle_sides: list[Decimal],
) -> Decimal:

    semiperimeter: Decimal = decimal_sum(triangle_sides) / Decimal("2")
    triangle_area: Decimal = (semiperimeter * (semiperimeter - triangle_sides[0]) * (semiperimeter - triangle_sides[1]) * (semiperimeter - triangle_sides[2])).sqrt()
    return triangle_area


def get_triangle_area_by_adjastend_sides_and_angle_sinus(
    *,
    triangle_first_adjastend_side: Decimal,
    triangle_second_adjastend_side: Decimal,
    angle_sinus: Decimal,
) -> Decimal:

    triangle_area: Decimal = (triangle_first_adjastend_side * triangle_second_adjastend_side * angle_sinus) / Decimal("2")
    return triangle_area


def get_triangle_area_by_triangle_perimeter_and_triangle_inradius(
    *,
    triangle_perimeter: Decimal,
    triangle_inradius: Decimal,
) -> Decimal:

    triangle_area: Decimal = (triangle_perimeter * triangle_inradius) / Decimal("2")
    return triangle_area


def get_triangle_area_by_triangle_sides_and_triangle_circumradius(
    *,
    triangle_sides: list[Decimal],
    triangle_circumradius: Decimal,
) -> Decimal:

    triangle_area: Decimal = decimal_product(triangle_sides) / (Decimal("4") * triangle_circumradius)
    return triangle_area


def get_triangle_base_by_triangle_area_and_triangle_height(
    *,
    triangle_area: Decimal,
    triangle_height: Decimal,
) -> Decimal:

    triangle_base: Decimal = (Decimal("2") * triangle_area) / triangle_height
    return triangle_base


def get_triangle_height_by_triangle_area_and_triangle_base(
    *,
    triangle_area: Decimal,
    triangle_base: Decimal,
) -> Decimal:

    triangle_height: Decimal = (Decimal("2") * triangle_area) / triangle_base
    return triangle_height


def get_triangle_adjacent_side_by_triangle_area_and_triangle_given_adjastend_side_and_angle_sinus(
    *,
    triangle_area: Decimal,
    triangle_given_adjastend_side: Decimal,
    angle_sinus: Decimal,
) -> Decimal:

    triangle_adjacent_side: Decimal = (Decimal("2") * triangle_area) / (triangle_given_adjastend_side * angle_sinus)
    return triangle_adjacent_side


def get_triangle_opposite_side_by_cosine_theorem(
    *,
    triangle_sides: list[Decimal],
    angle_cosinus: Decimal,
) -> Decimal:

    triangle_opposite_side: Decimal = (pow(triangle_sides[0], Decimal("2")) + pow(triangle_sides[1], Decimal("2")) - (Decimal("2") * triangle_sides[0] * triangle_sides[1] * angle_cosinus)).sqrt()
    return triangle_opposite_side


def get_triangle_adjastend_sides_by_cosine_theorem(
    *,
    triangle_sides: list[Decimal],
    angle_cosinus: Decimal,
) -> list[Decimal]:
    
    adjacent_side_projection: Decimal = triangle_sides[0] * angle_cosinus
    geometric_discriminant_sqrt: Decimal = (pow(adjacent_side_projection, Decimal("2")) + pow(triangle_sides[1], Decimal("2")) - pow(triangle_sides[0], Decimal("2"))).sqrt()

    triangle_adjastend_sides: list[Decimal] = [adjacent_side_projection - geometric_discriminant_sqrt, adjacent_side_projection + geometric_discriminant_sqrt]
    return triangle_adjastend_sides


def get_triangle_hypotenuse_by_pythagorean_theorem(
    *,
    triangle_legs: list[Decimal],
) -> Decimal:

    triangle_hypotenuse: Decimal = (pow(triangle_legs[0], Decimal("2")) + pow(triangle_legs[1], Decimal("2"))).sqrt()
    return triangle_hypotenuse


def get_triangle_leg_by_pythagorean_theorem(
    *,
    triangle_hypotenuse: Decimal,
    triangle_given_leg: Decimal,
) -> Decimal:

    triangle_leg: Decimal = (pow(triangle_hypotenuse, Decimal("2")) - pow(triangle_given_leg, Decimal("2"))).sqrt()
    return triangle_leg


def get_triangle_side_by_triangle_area_and_triangle_given_sides_and_triangle_circumradius(
    *,
    triangle_area: Decimal,
    triangle_given_sides: list[Decimal],
    triangle_circumradius: Decimal,
) -> Decimal:

    triangle_side: Decimal = (Decimal("4") * triangle_area * triangle_circumradius) / decimal_product(triangle_given_sides)
    return triangle_side


def get_triangle_perimeter_by_triangle_area_and_triangle_inradius(
    *,
    triangle_area: Decimal,
    triangle_inradius: Decimal,
) -> Decimal:

    triangle_perimeter: Decimal = (Decimal("2") * triangle_area) / triangle_inradius
    return triangle_perimeter


def get_angle_cosinus_by_cosine_theorem(
    *,
    triangle_sides: list[Decimal],
) -> Decimal:

    angle_cosinus: Decimal = (pow(triangle_sides[0], Decimal("2")) + pow(triangle_sides[1], Decimal("2")) - pow(triangle_sides[2], Decimal("2"))) / (Decimal("2") * triangle_sides[0] * triangle_sides[1])
    return angle_cosinus


def get_angle_sinus_by_triangle_area_and_adjastend_sides(
    *,
    triangle_area: Decimal,
    triangle_sides: list[Decimal],
) -> Decimal:

    angle_sinus: Decimal = (Decimal("2") * triangle_area) / (triangle_sides[0] * triangle_sides[1])
    return angle_sinus

#endregion
