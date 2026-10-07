from subjects.math.algebra import *
from subjects.math.geometry import *
from subjects.physics.electromagnetics import *
from subjects.physics.mechanics import *
from subjects.physics.thermodynamics import *


#region Algebra

LinearEquationSolver = LinearEquation()
QuadraticEquationSolver = QuadraticEquation()
LinearFunctionSolver = LinearFunction()
QuadraticFunctionSolver = QuadraticFunction()
LinearFunctionSolver = LinearFunction()
ArithmeticProgressionSumTheoremSolver = ArithmeticProgressionSumTheorem()
GeometricProgressionSumTheoremSolver = GeometricProgressionSumTheorem()
ArithmeticProgressionTermTheoremSolver = ArithmeticProgressionTermTheorem()
GeometricProgressionTermTheoremSolver = GeometricProgressionTermTheorem()
VectorCoordinatesTheoremSolver = VectorCoordinatesTheorem()
VectorMagnitudeTheoremSolver = VectorMagnitudeTheorem()
VectorDotProductTheoremSolver = VectorDotProductTheorem()
VectorAngleCosinusTheoremSolver = VectorAngleCosinusTheorem()
VectorScalingTheoremSolver = VectorScalingTheorem()

#endregion


#region Geometry

CircleAreaTheoremSolver = CircleAreaTheorem()
CircumferenceTheoremSolver = CircumferenceTheorem()


formulas_map: dict = {
    ("LinearEquation", "get_x"): LinearEquationSolver.get_x,
    ("QuadraticEquation", "get_x"): QuadraticEquationSolver.get_x,
    ("LinearFunction", "get_y"): LinearFunctionSolver.get_y,
    ("LinearFunction", "get_k"): LinearFunctionSolver.get_k,
    ("LinearFunction", "get_b"): LinearFunctionSolver.get_b,
    ("QuadraticFunction", "get_y"): QuadraticFunctionSolver.get_y,
    ("QuadraticFunction", "get_a"): QuadraticFunctionSolver.get_a,
    ("QuadraticFunction", "get_b"): QuadraticFunctionSolver.get_b,
    ("QuadraticFunction", "get_c"): QuadraticFunctionSolver.get_c,
    ("ArithmeticProgressionSumTheorem", "get_S"): ArithmeticProgressionSumTheoremSolver.get_S,
    ("ArithmeticProgressionSumTheorem", "get_a1"): ArithmeticProgressionSumTheoremSolver.get_a1,
    ("ArithmeticProgressionSumTheorem", "get_an"): ArithmeticProgressionSumTheoremSolver.get_an,
    ("ArithmeticProgressionSumTheorem", "get_n"): ArithmeticProgressionSumTheoremSolver.get_n,
    ("GeometricProgressionSumTheorem", "get_S"): GeometricProgressionSumTheoremSolver.get_S,
    ("GeometricProgressionSumTheorem", "get_b1"): GeometricProgressionSumTheoremSolver.get_b1,
    ("GeometricProgressionSumTheorem", "get_bn"): GeometricProgressionSumTheoremSolver.get_bn,
    ("GeometricProgressionSumTheorem", "get_q"): GeometricProgressionSumTheoremSolver.get_q,
    ("ArithmeticProgressionTermTheorem", "get_an"): ArithmeticProgressionTermTheoremSolver.get_an,
    ("ArithmeticProgressionTermTheorem", "get_a1"): ArithmeticProgressionTermTheoremSolver.get_a1,
    ("ArithmeticProgressionTermTheorem", "get_d"): ArithmeticProgressionTermTheoremSolver.get_d,
    ("ArithmeticProgressionTermTheorem", "get_n"): ArithmeticProgressionTermTheoremSolver.get_n,
    ("GeometricProgressionTermTheorem", "get_bn"): GeometricProgressionTermTheoremSolver.get_bn,
    ("GeometricProgressionTermTheorem", "get_b1"): GeometricProgressionTermTheoremSolver.get_b1,
    ("GeometricProgressionTermTheorem", "get_q"): GeometricProgressionTermTheoremSolver.get_q,
    ("GeometricProgressionTermTheorem", "get_n"): GeometricProgressionTermTheoremSolver.get_n,
}
