from decimal import Decimal


#region Vector magnitude

def get_vector_magnitude_by_delta_coordinates_sum(
    *,
    end_coordinates_list: list[Decimal],
    start_coordinates_list: list[Decimal],
) -> Decimal:

    vector_magnitude: Decimal = Decimal("0")
    
    for end_coordinate, start_coordinate in zip(end_coordinates_list, start_coordinates_list):
        delta_coordinate: Decimal = end_coordinate - start_coordinate
        squared_delta_coordinate: Decimal = pow(delta_coordinate, Decimal("2"))
        vector_magnitude += squared_delta_coordinate

    vector_magnitude: Decimal = vector_magnitude.sqrt()
    return vector_magnitude

#endregion
