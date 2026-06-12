from decimal import Decimal, InvalidOperation
from math import tan, radians

from utils import get_decimal_array_from_string_array
from config import DECIMAL_QUANTIZE_TARGET, DECIMAL_FORMAT_MODE

def get_angle_tangent_by_degrees(*,
                                 degrees: str,
                                 ) -> Decimal | None:
    
    
    string_value_array: list[str] = [degrees]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    if decimal_value_array is None:
        return None
    
    try:
        decimal_degrees, = decimal_value_array
        angle_tangent: Decimal = Decimal(format(Decimal(str(tan(radians(float(decimal_degrees))))).quantize(DECIMAL_QUANTIZE_TARGET).normalize(), DECIMAL_FORMAT_MODE))
        return angle_tangent
    except (ZeroDivisionError, InvalidOperation):
        return None
    
