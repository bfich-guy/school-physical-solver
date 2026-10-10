from calculators.math.algebra import *
from calculators.math.geometry import *
from calculators.physics.electromagnetics import *
from calculators.physics.mechanics import *
from calculators.physics.thermodynamics import *


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
ParallelogramAreaByBaseAndHeightTheoremSolver = ParallelogramAreaByBaseAndHeightTheorem()

#endregion


#region Geometry

CircleAreaTheoremSolver = CircleAreaTheorem()
CircumferenceTheoremSolver = CircumferenceTheorem()
TrapezoidMidlineTheoremSolver = TrapezoidMidlineTheorem()
TrapezoidAreaByMidlineAndHeightTheoremSolver = TrapezoidAreaByMidlineAndHeightTheorem()
TriangleAreaByBaseAndHeightTheoremSolver = TriangleAreaByBaseAndHeightTheorem()
HeronTheoremSolver = HeronTheorem()
CosineTheoremSolver = CosineTheorem()
SineTheoremSolver = SineTheorem()
PythagoreanTheoremSolver = PythagoreanTheorem()
TriangleAreaByInscribedCircleTheoremSolver = TriangleAreaByInscribedCircleTheorem()
TriangleAreaByCircumscripedCircleTheoremSolver = TriangleAreaByCircumscripedCircleTheorem()
TriangleSideProjectionTheoremSolver = TriangleSideProjectionTheorem()
FigureAreaBySimilarityCoefficientTheoremSolver = FigureAreaBySimilarityCoefficientTheorem()

#endregion


#region Electromagnetics

OhmsSpecificLawSolver = OhmsSpecificLaw()
OhmsFullLawSolver = OhmsFullLaw()
WattsLawSolver = WattsLaw()
JouleLenzLawSolver = JouleLenzLaw()
CoulombsLawSolver = CoulombsLaw()
ConductorResistanceLawSolver = ConductorResistanceLaw()
AmperesLawSolver = AmperesLaw()
LorentzLawSolver = LorentzLaw()
FaradaysLawSolver = FaradaysLaw()
MagneticFluxToContourLawSolver = MagneticFluxToContourLaw()

#endregion


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
    ("VectorCoordinatesTheorem", "get_a"): VectorCoordinatesTheoremSolver.get_a,
    ("VectorCoordinatesTheorem", "get_A"): VectorCoordinatesTheoremSolver.get_A,
    ("VectorCoordinatesTheorem", "get_B"): VectorCoordinatesTheoremSolver.get_B,
    ("VectorMagnitudeTheorem", "get_la"): VectorMagnitudeTheoremSolver.get_la,
    ("VectorDotProductTheorem", "get_ab"): VectorDotProductTheoremSolver.get_ab,
    ("VectorAngleCosinusTheorem", "get_cosa"): VectorAngleCosinusTheoremSolver.get_cosa,
    ("VectorAngleCosinusTheorem", "get_ab"): VectorAngleCosinusTheoremSolver.get_ab,
    ("VectorAngleCosinusTheorem", "get_la"): VectorAngleCosinusTheoremSolver.get_la,
    ("VectorAngleCosinusTheorem", "get_lb"): VectorAngleCosinusTheoremSolver.get_lb,
    ("VectorScalingTheorem", "get_b"): VectorScalingTheoremSolver.get_b,

    ("CircleAreaTheorem", "get_S"): CircleAreaTheoremSolver.get_S,
    ("CircleAreaTheorem", "get_r"): CircleAreaTheoremSolver.get_r,
    ("CircumferenceTheorem", "get_l"): CircumferenceTheoremSolver.get_l,
    ("CircumferenceTheorem", "get_r"): CircumferenceTheoremSolver.get_r,
    ("ParallelogramAreaByBaseAndHeightTheorem", "get_S"): ParallelogramAreaByBaseAndHeightTheoremSolver.get_S,
    ("ParallelogramAreaByBaseAndHeightTheorem", "get_a"): ParallelogramAreaByBaseAndHeightTheoremSolver.get_a,
    ("ParallelogramAreaByBaseAndHeightTheorem", "get_h"): ParallelogramAreaByBaseAndHeightTheoremSolver.get_h,
    ("TrapezoidMidlineTheorem", "get_m"): TrapezoidMidlineTheoremSolver.get_m,
    ("TrapezoidMidlineTheorem", "get_a"): TrapezoidMidlineTheoremSolver.get_a,
    ("TrapezoidMidlineTheorem", "get_b"): TrapezoidMidlineTheoremSolver.get_b,
    ("TrapezoidAreaByMidlineAndHeightTheorem", "get_S"): TrapezoidAreaByMidlineAndHeightTheoremSolver.get_S,
    ("TrapezoidAreaByMidlineAndHeightTheorem", "get_m"): TrapezoidAreaByMidlineAndHeightTheoremSolver.get_m,
    ("TrapezoidAreaByMidlineAndHeightTheorem", "get_h"): TrapezoidAreaByMidlineAndHeightTheoremSolver.get_h,
    ("TriangleAreaByBaseAndHeightTheorem", "get_S"): TriangleAreaByBaseAndHeightTheoremSolver.get_S,
    ("TriangleAreaByBaseAndHeightTheorem", "get_a"): TriangleAreaByBaseAndHeightTheoremSolver.get_a,
    ("TriangleAreaByBaseAndHeightTheorem", "get_h"): TriangleAreaByBaseAndHeightTheoremSolver.get_h,
    ("HeronTheorem", "get_S"): HeronTheoremSolver.get_S,
    ("CosineTheorem", "get_a"): CosineTheoremSolver.get_a,
    ("CosineTheorem", "get_b"): CosineTheoremSolver.get_b,
    ("CosineTheorem", "get_c"): CosineTheoremSolver.get_c,
    ("CosineTheorem", "get_cosa"): CosineTheoremSolver.get_cosa,
    ("SineTheorem", "get_a"): SineTheoremSolver.get_a,
    ("SineTheorem", "get_sina"): SineTheoremSolver.get_sina,
    ("SineTheorem", "get_R"): SineTheoremSolver.get_R,
    ("PythagoreanTheorem", "get_a"): PythagoreanTheoremSolver.get_a,
    ("PythagoreanTheorem", "get_b"): PythagoreanTheoremSolver.get_b,
    ("PythagoreanTheorem", "get_c"): PythagoreanTheoremSolver.get_c,
    ("TriangleAreaByInscribedCircleTheorem", "get_S"): TriangleAreaByInscribedCircleTheoremSolver.get_S,
    ("TriangleAreaByInscribedCircleTheorem", "get_p"): TriangleAreaByInscribedCircleTheoremSolver.get_p,
    ("TriangleAreaByInscribedCircleTheorem", "get_r"): TriangleAreaByInscribedCircleTheoremSolver.get_r,
    ("TriangleAreaByCircumscripedCircleTheorem", "get_S"): TriangleAreaByCircumscripedCircleTheoremSolver.get_S,
    ("TriangleAreaByCircumscripedCircleTheorem", "get_a"): TriangleAreaByCircumscripedCircleTheoremSolver.get_a,
    ("TriangleAreaByCircumscripedCircleTheorem", "get_b"): TriangleAreaByCircumscripedCircleTheoremSolver.get_b,
    ("TriangleAreaByCircumscripedCircleTheorem", "get_c"): TriangleAreaByCircumscripedCircleTheoremSolver.get_c,
    ("TriangleAreaByCircumscripedCircleTheorem", "get_R"): TriangleAreaByCircumscripedCircleTheoremSolver.get_R,
    ("TriangleSideProjectionTheorem", "get_h"): TriangleSideProjectionTheoremSolver.get_h,
    ("TriangleSideProjectionTheorem", "get_a"): TriangleSideProjectionTheoremSolver.get_a,
    ("TriangleSideProjectionTheorem", "get_cossina"): TriangleSideProjectionTheoremSolver.get_cossina,
    ("FigureAreaBySimilarityCoefficientTheorem", "get_S2"): FigureAreaBySimilarityCoefficientTheoremSolver.get_S2,
    ("FigureAreaBySimilarityCoefficientTheorem", "get_S1"): FigureAreaBySimilarityCoefficientTheoremSolver.get_S1,
    ("FigureAreaBySimilarityCoefficientTheorem", "get_k"): FigureAreaBySimilarityCoefficientTheoremSolver.get_k,

    ("OhmsSpecificLaw", "get_U"): OhmsSpecificLawSolver.get_U,
    ("OhmsSpecificLaw", "get_I"): OhmsSpecificLawSolver.get_I,
    ("OhmsSpecificLaw", "get_R"): OhmsSpecificLawSolver.get_R,
    ("OhmsFullLaw", "get_E"): OhmsFullLawSolver.get_E,
    ("OhmsFullLaw", "get_U"): OhmsFullLawSolver.get_U,
    ("OhmsFullLaw", "get_I"): OhmsFullLawSolver.get_I,
    ("OhmsFullLaw", "get_r"): OhmsFullLawSolver.get_r,
    ("WattsLaw", "get_P"): WattsLawSolver.get_P,
    ("WattsLaw", "get_U"): WattsLawSolver.get_U,
    ("WattsLaw", "get_I"): WattsLawSolver.get_I,
    ("JouleLenzLaw", "get_Q"): JouleLenzLawSolver.get_Q,
    ("JouleLenzLaw", "get_P"): JouleLenzLawSolver.get_P,
    ("JouleLenzLaw", "get_t"): JouleLenzLawSolver.get_t,
    ("CoulombsLaw", "get_F"): CoulombsLawSolver.get_F,
    ("CoulombsLaw", "get_q1"): CoulombsLawSolver.get_q1,
    ("CoulombsLaw", "get_q2"): CoulombsLawSolver.get_q2,
    ("CoulombsLaw", "get_r"): CoulombsLawSolver.get_r,
    ("ConductorResistanceLaw", "get_R"): ConductorResistanceLawSolver.get_R,
    ("ConductorResistanceLaw", "get_rho"): ConductorResistanceLawSolver.get_rho,
    ("ConductorResistanceLaw", "get_l"): ConductorResistanceLawSolver.get_l,
    ("ConductorResistanceLaw", "get_S"): ConductorResistanceLawSolver.get_S,
    ("AmperesLaw", "get_F"): AmperesLawSolver.get_F,
    ("AmperesLaw", "get_B"): AmperesLawSolver.get_B,
    ("AmperesLaw", "get_I"): AmperesLawSolver.get_I,
    ("AmperesLaw", "get_L"): AmperesLawSolver.get_L,
    ("AmperesLaw", "get_sina"): AmperesLawSolver.get_sina,
    ("LorentzLaw", "get_F"): LorentzLawSolver.get_F,
    ("LorentzLaw", "get_q"): LorentzLawSolver.get_q,
    ("LorentzLaw", "get_v"): LorentzLawSolver.get_v,
    ("LorentzLaw", "get_B"): LorentzLawSolver.get_B,
    ("LorentzLaw", "get_sina"): LorentzLawSolver.get_sina,
    ("FaradaysLaw", "get_E"): FaradaysLawSolver.get_E,
    ("FaradaysLaw", "get_Dphi"): FaradaysLawSolver.get_Dphi,
    ("FaradaysLaw", "get_Dt"): FaradaysLawSolver.get_Dt,
    ("MagneticFluxToContourLaw", "get_phi"): MagneticFluxToContourLawSolver.get_phi,
    ("MagneticFluxToContourLaw", "get_B"): MagneticFluxToContourLawSolver.get_B,
    ("MagneticFluxToContourLaw", "get_S"): MagneticFluxToContourLawSolver.get_S,
    ("MagneticFluxToContourLaw", "get_cosa"): MagneticFluxToContourLawSolver.get_cosa,
}
