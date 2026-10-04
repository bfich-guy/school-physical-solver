from subjects.math.algebra import *
from subjects.math.geometry import *
from subjects.physics.electromagnetics import *
from subjects.physics.mechanics import *
from subjects.physics.thermodynamics import *

from system.config.constants import FormulaMapData, InputMethod


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


formulas_map: dict = {
    ("LinearEquation", "get_x"): {
        FormulaMapData.FUNCTION.value: LinearEquationSolver.get_x,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("QuadraticEquation", "get_x"): {
        FormulaMapData.FUNCTION.value: QuadraticEquationSolver.get_x,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("LinearFunction", "get_y"): {
        FormulaMapData.FUNCTION.value: LinearFunctionSolver.get_y,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("LinearFunction", "get_k"): {
        FormulaMapData.FUNCTION.value: LinearFunctionSolver.get_k,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("LinearFunction", "get_b"): {
        FormulaMapData.FUNCTION.value: LinearFunctionSolver.get_b,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("QuadraticFunction", "get_y"): {
        FormulaMapData.FUNCTION.value: QuadraticFunctionSolver.get_y,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("QuadraticFunction", "get_a"): {
        FormulaMapData.FUNCTION.value: QuadraticFunctionSolver.get_a,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("QuadraticFunction", "get_b"): {
        FormulaMapData.FUNCTION.value: QuadraticFunctionSolver.get_b,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("QuadraticFunction", "get_c"): {
        FormulaMapData.FUNCTION.value: QuadraticFunctionSolver.get_c,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("ArithmeticProgressionSumTheorem", "get_S"): {
        FormulaMapData.FUNCTION.value: ArithmeticProgressionSumTheoremSolver.get_S,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("ArithmeticProgressionSumTheorem", "get_a1"): {
        FormulaMapData.FUNCTION.value: ArithmeticProgressionSumTheoremSolver.get_a1,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("ArithmeticProgressionSumTheorem", "get_an"): {
        FormulaMapData.FUNCTION.value: ArithmeticProgressionSumTheoremSolver.get_an,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("ArithmeticProgressionSumTheorem", "get_n"): {
        FormulaMapData.FUNCTION.value: ArithmeticProgressionSumTheoremSolver.get_n,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("GeometricProgressionSumTheorem", "get_S"): {
        FormulaMapData.FUNCTION.value: GeometricProgressionSumTheoremSolver.get_S,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("GeometricProgressionSumTheorem", "get_b1"): {
        FormulaMapData.FUNCTION.value: GeometricProgressionSumTheoremSolver.get_b1,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("GeometricProgressionSumTheorem", "get_bn"): {
        FormulaMapData.FUNCTION.value: GeometricProgressionSumTheoremSolver.get_bn,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("GeometricProgressionSumTheorem", "get_q"): {
        FormulaMapData.FUNCTION.value: GeometricProgressionSumTheoremSolver.get_q,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("ArithmeticProgressionTermTheorem", "get_an"): {
        FormulaMapData.FUNCTION.value: ArithmeticProgressionTermTheoremSolver.get_an,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("ArithmeticProgressionTermTheorem", "get_a1"): {
        FormulaMapData.FUNCTION.value: ArithmeticProgressionTermTheoremSolver.get_a1,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("ArithmeticProgressionTermTheorem", "get_d"): {
        FormulaMapData.FUNCTION.value: ArithmeticProgressionTermTheoremSolver.get_d,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("ArithmeticProgressionTermTheorem", "get_n"): {
        FormulaMapData.FUNCTION.value: ArithmeticProgressionTermTheoremSolver.get_n,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("GeometricProgressionTermTheorem", "get_bn"): {
        FormulaMapData.FUNCTION.value: GeometricProgressionTermTheoremSolver.get_bn,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("GeometricProgressionTermTheorem", "get_b1"): {
        FormulaMapData.FUNCTION.value: GeometricProgressionTermTheoremSolver.get_b1,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("GeometricProgressionTermTheorem", "get_q"): {
        FormulaMapData.FUNCTION.value: GeometricProgressionTermTheoremSolver.get_q,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
    ("GeometricProgressionTermTheorem", "get_n"): {
        FormulaMapData.FUNCTION.value: GeometricProgressionTermTheoremSolver.get_n,
        FormulaMapData.METHOD.value: InputMethod.FIRST_NUMBER.value,
        },
}
