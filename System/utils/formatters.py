from decimal import Decimal

from system.utils.helpers import clean_trailing_zeros_from_decimal_number


#region Number formatters

def turn_common_decimal_fraction_into_fraction(
    *,
    decimal_number: Decimal,
) -> list[Decimal]:
    
    decimal_numerator: Decimal = decimal_number
    decimal_denominator: Decimal = Decimal("1")

    numerator_and_denominator_are_not_integers: bool = any([
        decimal_numerator % Decimal("1") != Decimal("0"),
        decimal_denominator % Decimal("1") != Decimal("0"),
    ])

    while numerator_and_denominator_are_not_integers:
        decimal_numerator *= Decimal("10")
        decimal_denominator *= Decimal("10")

        numerator_and_denominator_are_not_integers: bool = any([
            decimal_numerator % Decimal("1") != Decimal("0"),
            decimal_denominator % Decimal("1") != Decimal("0"),
        ])

    cleaned_decimal_numerator: Decimal = clean_trailing_zeros_from_decimal_number(decimal_number=decimal_numerator)
    cleaned_decimal_denominator: Decimal = clean_trailing_zeros_from_decimal_number(decimal_number=decimal_denominator)

    integer_fraction: list[Decimal] = [cleaned_decimal_numerator, cleaned_decimal_denominator]
    return integer_fraction


def turn_fraction_into_mixed_number(
    *,
    decimal_numerator: Decimal,
    decimal_denominator: Decimal,
) -> list[Decimal]:

    mixed_number_integer_part: Decimal = decimal_numerator // decimal_denominator
    mixed_number_numerator: Decimal = decimal_numerator % decimal_denominator
    mixed_number_denominator: Decimal = decimal_denominator

    mixed_number: list[Decimal] = [mixed_number_integer_part, mixed_number_numerator, mixed_number_denominator]
    return mixed_number


def turn_mixed_number_into_fraction(
    *,
    mixed_number_integer_part: Decimal,
    mixed_number_numerator: Decimal,
    mixed_number_denominator: Decimal,
) -> list[Decimal]:

    fraction_numerator: Decimal = (mixed_number_integer_part * mixed_number_denominator) + mixed_number_numerator
    fraction_denominator: Decimal = mixed_number_denominator

    fraction: list[Decimal] = [fraction_numerator, fraction_denominator]
    return fraction

#endregion
