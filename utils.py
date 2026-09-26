from fastapi import FastAPI, APIRouter
from decimal import Decimal


#region Server helpers

def include_routers(
    *,
    app: FastAPI,
    routers_list: list[APIRouter],
) -> None:

    for router in routers_list:
        app.include_router(router=router)

#endregion


#region Decimal helpers

def clean_trailing_zeros_from_decimal_number(
    *,
    decimal_number: Decimal,
    format_mode: str = "f",
) -> Decimal:

    cleaned_decimal_number: Decimal = Decimal(format(decimal_number.normalize(), format_mode))
    return cleaned_decimal_number


def decimal_length(decimal_numbers: list[Decimal] | tuple[Decimal]) -> Decimal:
    decimal_length = Decimal("0")

    for _ in decimal_numbers:
        decimal_length += Decimal("1")

    return decimal_length


def decimal_sum(decimal_numbers: list[Decimal] | tuple[Decimal]) -> Decimal:
    decimal_sum = Decimal("0")

    for decimal_number in decimal_numbers:
        decimal_sum += decimal_number

    return decimal_sum


def decimal_product(decimal_numbers: list[Decimal] | tuple[Decimal]) -> Decimal:
    decimal_product = Decimal("1")

    for decimal_number in decimal_numbers:
        decimal_product *= decimal_number

    return decimal_product


def decimal_power(decimal_base: Decimal, decimal_exponent: Decimal) -> Decimal:
    decimal_power: Decimal = pow(decimal_base, decimal_exponent)
    return decimal_power


def decimal_logarithm(decimal_value: Decimal, decimal_base: Decimal) -> Decimal:
    decimal_logarithm: Decimal = (decimal_value.ln() / decimal_base.ln()).quantize(Decimal("1"))
    return decimal_logarithm


def decimal_array_length(decimal_numbers: list[Decimal] | tuple[Decimal]) -> Decimal:
    decimal_array_length: Decimal = Decimal(str(len(decimal_numbers)))
    return decimal_array_length


def decimal_factorial(decimal_number) -> Decimal:
    decimal_factorial = Decimal("1")
    integered_decimal_number: int = int(str(decimal_number))

    for integer_number in range(2, integered_decimal_number + 1):
        decimal_factorial *= Decimal(str(integer_number))

    return decimal_factorial

#endregion


#region Decimal calculators

def turn_decimal_fraction_into_fraction(
    *,
    decimal_number: Decimal,
    decimal_number_system_base = Decimal("10"),
) -> tuple[Decimal, Decimal, str]:

    fraction_sign: str = "-" if decimal_number < Decimal("0") else "+"

    fraction_divisor = Decimal("1")
    decimal_number_is_not_integer: bool = decimal_number % Decimal("1") != Decimal("0")

    while decimal_number_is_not_integer:
        decimal_number *= decimal_number_system_base
        fraction_divisor *= decimal_number_system_base

        decimal_number_is_not_integer: bool = decimal_number % Decimal("1") != Decimal("0")

    fraction: tuple[Decimal, Decimal, str] = (abs(clean_trailing_zeros_from_decimal_number(decimal_number=decimal_number)), fraction_divisor, fraction_sign)
    return fraction


def factorize_decimal_number(
    *,
    decimal_number: Decimal,
) -> list[Decimal]:

    decimal_number_is_zero: bool = decimal_number == Decimal("0")
    decimal_number_is_one: bool = decimal_number == Decimal("1")

    if decimal_number_is_zero:
        return [Decimal("0")]

    if decimal_number_is_one:
        return [Decimal("1")]

    decimal_number_multipliers: list[Decimal] = []
    divisor = Decimal("2")

    decimal_number_is_not_equal_to_one: bool = decimal_number != Decimal("1")

    while decimal_number_is_not_equal_to_one:
        decimal_number_is_divisible: bool = decimal_number % divisor == Decimal("0")

        if decimal_number_is_divisible:
            decimal_number_multipliers.append(divisor)
            decimal_number //= divisor
            divisor = Decimal("2")
        else:
            divisor += Decimal("1")

        decimal_number_is_not_equal_to_one: bool = decimal_number != Decimal("1")

    return decimal_number_multipliers


def reduce_fraction(
    *,
    fraction_numerator_multipliers: list[Decimal],
    fraction_denominator_multipliers: list[Decimal],
    fraction_sign: str,
) -> tuple[Decimal, Decimal, str]:

    greatest_divisor_multipliers: list[Decimal] = []

    sorted_fraction_numerator_multipliers: list[Decimal] = sorted(fraction_numerator_multipliers, reverse=True)
    sorted_fraction_denominator_multipliers: list[Decimal] = sorted(fraction_denominator_multipliers, reverse=True)

    fraction_numerator: Decimal = decimal_product(sorted_fraction_numerator_multipliers)
    fraction_denominator: Decimal = decimal_product(sorted_fraction_denominator_multipliers)

    sorted_fraction_numerator_multipliers_are_not_ran_out: bool = len(sorted_fraction_numerator_multipliers) > 0

    while sorted_fraction_numerator_multipliers_are_not_ran_out:
        greatest_number: Decimal = sorted_fraction_numerator_multipliers[0]
        greatest_number_in_denominator: bool = greatest_number in sorted_fraction_denominator_multipliers

        if greatest_number_in_denominator:
            greatest_divisor_multipliers.append(greatest_number)

            sorted_fraction_numerator_multipliers.remove(greatest_number)
            sorted_fraction_denominator_multipliers.remove(greatest_number)
        else:
            sorted_fraction_numerator_multipliers.remove(greatest_number)

        sorted_fraction_numerator_multipliers_are_not_ran_out: bool = len(sorted_fraction_numerator_multipliers) > 0

    greatest_divisor: Decimal = decimal_product(greatest_divisor_multipliers)

    reduced_fraction_numerator: Decimal = fraction_numerator // greatest_divisor
    reduced_fraction_denominator: Decimal = fraction_denominator // greatest_divisor

    reduced_fraction: tuple[Decimal, Decimal, str] = (reduced_fraction_numerator, reduced_fraction_denominator, fraction_sign)
    return reduced_fraction


def turn_decimal_number_into_fraction(
    *,
    decimal_number: Decimal,
) -> tuple[Decimal, Decimal, str]:

    fraction_numerator, common_fraction_denominator, common_fraction_sign = turn_decimal_fraction_into_fraction(decimal_number=decimal_number)

    fraction_numerator_multipliers: list[Decimal] = factorize_decimal_number(decimal_number=fraction_numerator)
    fraction_denominator_multipliers: list[Decimal] = factorize_decimal_number(decimal_number=common_fraction_denominator)

    reduced_common_fraction: tuple[Decimal, Decimal, str] = reduce_fraction(
        fraction_numerator_multipliers=fraction_numerator_multipliers,
        fraction_denominator_multipliers=fraction_denominator_multipliers,
        fraction_sign=common_fraction_sign,
    )

    return reduced_common_fraction

#endregion
