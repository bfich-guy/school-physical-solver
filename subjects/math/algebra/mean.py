from decimal import Decimal
from functools import reduce
import operator


#region Arithmetic mean

def get_arithmetic_mean_by_numbers_sum_and_amount(
    *,
    numbers_list: list[Decimal], 
) -> Decimal:

    numbers_sum: Decimal = Decimal(sum(numbers_list))
    number_amount: Decimal = Decimal(len(numbers_list))

    arithmetic_mean: Decimal = numbers_sum / number_amount
    return arithmetic_mean

#endregion


#region Geometric mean

def get_geometric_mean_by_numbers_product_and_amount(
    *,
    numbers_list: list[Decimal],
) -> Decimal:

    numbers_product: Decimal = reduce(operator.mul, numbers_list)
    numbers_amount: Decimal = Decimal(len(numbers_list))

    geometric_mean: Decimal = pow(numbers_product, Decimal("1") / numbers_amount)
    return geometric_mean

#endregion
