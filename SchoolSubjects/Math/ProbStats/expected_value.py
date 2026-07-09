from decimal import Decimal


#region Expected value

def get_expected_value_by_values_and_probabilities(
    *,
    values: list[Decimal],
    probabilities: list[Decimal],
) -> Decimal:

    expected_value = Decimal("0")

    for value, probability in zip(values, probabilities):
        weighted_value: Decimal = value * probability
        expected_value += weighted_value

    return expected_value

#endregion
