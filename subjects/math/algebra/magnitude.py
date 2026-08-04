from decimal import Decimal


#region Vector magnitude

def get_vector_magnitude_by_delta_coordinates_sum(
    *,
    delta_coordinates_list: list[Decimal],
) -> Decimal:

    squared_vector_magnitude: Decimal = Decimal("0")

    for delta_coordinate in delta_coordinates_list:
        squared_delta_coordinate: Decimal = delta_coordinate ** Decimal("2")
        vector_magnitude += squared_delta_coordinate

    vector_magnitude: Decimal = squared_vector_magnitude.sqrt()
    return vector_magnitude

#endregion
