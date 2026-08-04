from decimal import Decimal


#region Probability

def get_success_and_failure_probabilities_by_favorite_and_total_outcomes(
    *,
    favorable_outcomes: Decimal,
    total_outcomes: Decimal,
) -> tuple[Decimal, Decimal]:

    success_probability: Decimal = favorable_outcomes / total_outcomes
    failure_probability: Decimal = Decimal("1") - success_probability
    
    probabilities: tuple[Decimal, Decimal] = (success_probability, failure_probability)
    return probabilities 

#endregion
