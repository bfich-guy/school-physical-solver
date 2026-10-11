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


#region Mechanics

NewtonsSecondLawSolver = NewtonsSecondLaw()
HookesLawSolver = HookesLaw()
AmontonsCoulombLawSolver = AmontonsCoulombLaw()
NormalReactionLawSolver = NormalReactionLaw()
MomentumLawSolver = MomentumLaw()
KineticEnergyLawSolver = KineticEnergyLaw()
PotentialEnergyLawSolver = PotentialEnergyLaw()
MechanicalWorkLawSolver = MechanicalWorkLaw()
MechanicalPowerLawSolver = MechanicalPowerLaw()
MechanicalEfficiencyLawSolver = MechanicalEfficiencyLaw()
LinearAccelerationLawSolver = LinearAccelerationLaw()
UniformlyAcceleratedRectilinearMotionLawSolver = UniformlyAcceleratedRectilinearMotionLaw()
CentripetalAccelerationLawSolver = CentripetalAccelerationLaw()
TrajectoryRadiusLawSolver = TrajectoryRadiusLaw()
PascalsLawSolver = PascalsLaw()
ArchimedesLawSolver = ArchimedesLaw()
HydrostaticPressureLawSolver = HydrostaticPressureLaw()

#endregion


#region Thermodynamics

SensibleHeatLawSolver = SensibleHeatLaw()
CombustionHeatLawSolver = CombustionHeatLaw()
FusionHeatLawSolver = FusionHeatLaw()
VaporizationHeatLawSolver = VaporizationHeatLaw()
MendeleevClapeyronLawSolver = MendeleevClapeyronLaw()
MolarMassLawSolver = MolarMassLaw()


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

    ("NewtonsSecondLaw", "get_F"): NewtonsSecondLawSolver.get_F,
    ("NewtonsSecondLaw", "get_m"): NewtonsSecondLawSolver.get_m,
    ("NewtonsSecondLaw", "get_a"): NewtonsSecondLawSolver.get_a,
    ("HookesLaw", "get_F"): HookesLawSolver.get_F,
    ("HookesLaw", "get_k"): HookesLawSolver.get_k,
    ("HookesLaw", "get_Dx"): HookesLawSolver.get_Dx,
    ("AmontonsCoulombLaw", "get_F"): AmontonsCoulombLawSolver.get_F,
    ("AmontonsCoulombLaw", "get_mu"): AmontonsCoulombLawSolver.get_mu,
    ("AmontonsCoulombLaw", "get_N"): AmontonsCoulombLawSolver.get_N,
    ("NormalReactionLaw", "get_N"): NormalReactionLawSolver.get_N,
    ("NormalReactionLaw", "get_F"): NormalReactionLawSolver.get_F,
    ("NormalReactionLaw", "get_cosa"): NormalReactionLawSolver.get_cosa,
    ("MomentumLaw", "get_p"): MomentumLawSolver.get_p,
    ("MomentumLaw", "get_m"): MomentumLawSolver.get_m,
    ("MomentumLaw", "get_v"): MomentumLawSolver.get_v,
    ("KineticEnergyLaw", "get_E"): KineticEnergyLawSolver.get_E,
    ("KineticEnergyLaw", "get_m"): KineticEnergyLawSolver.get_m,
    ("KineticEnergyLaw", "get_v"): KineticEnergyLawSolver.get_v,
    ("PotentialEnergyLaw", "get_E"): PotentialEnergyLawSolver.get_E,
    ("PotentialEnergyLaw", "get_F"): PotentialEnergyLawSolver.get_F,
    ("PotentialEnergyLaw", "get_h"): PotentialEnergyLawSolver.get_h,
    ("MechanicalWorkLaw", "get_A"): MechanicalWorkLawSolver.get_A,
    ("MechanicalWorkLaw", "get_F"): MechanicalWorkLawSolver.get_F,
    ("MechanicalWorkLaw", "get_S"): MechanicalWorkLawSolver.get_S,
    ("MechanicalWorkLaw", "get_cosa"): MechanicalWorkLawSolver.get_cosa,
    ("MechanicalPowerLaw", "get_P"): MechanicalPowerLawSolver.get_P,
    ("MechanicalPowerLaw", "get_A"): MechanicalPowerLawSolver.get_A,
    ("MechanicalPowerLaw", "get_t"): MechanicalPowerLawSolver.get_t,
    ("MechanicalEfficiencyLaw", "get_eta"): MechanicalEfficiencyLawSolver.get_eta,
    ("MechanicalEfficiencyLaw", "get_Au"): MechanicalEfficiencyLawSolver.get_Au,
    ("MechanicalEfficiencyLaw", "get_At"): MechanicalEfficiencyLawSolver.get_At,
    ("LinearAccelerationLaw", "get_a"): LinearAccelerationLawSolver.get_a,
    ("LinearAccelerationLaw", "get_v"): LinearAccelerationLawSolver.get_v,
    ("LinearAccelerationLaw", "get_t"): LinearAccelerationLawSolver.get_t,
    ("UniformlyAcceleratedRectilinearMotionLaw", "get_S"): UniformlyAcceleratedRectilinearMotionLawSolver.get_S,
    ("UniformlyAcceleratedRectilinearMotionLaw", "get_v0"): UniformlyAcceleratedRectilinearMotionLawSolver.get_v0,
    ("UniformlyAcceleratedRectilinearMotionLaw", "get_a"): UniformlyAcceleratedRectilinearMotionLawSolver.get_a,
    ("UniformlyAcceleratedRectilinearMotionLaw", "get_t"): UniformlyAcceleratedRectilinearMotionLawSolver.get_t,
    ("CentripetalAccelerationLaw", "get_a"): CentripetalAccelerationLawSolver.get_a,
    ("CentripetalAccelerationLaw", "get_v"): CentripetalAccelerationLawSolver.get_v,
    ("CentripetalAccelerationLaw", "get_w"): CentripetalAccelerationLawSolver.get_w,
    ("TrajectoryRadiusLaw", "get_R"): TrajectoryRadiusLawSolver.get_R,
    ("TrajectoryRadiusLaw", "get_v"): TrajectoryRadiusLawSolver.get_v,
    ("TrajectoryRadiusLaw", "get_w"): TrajectoryRadiusLawSolver.get_w,
    ("PascalsLaw", "get_p"): PascalsLawSolver.get_p,
    ("PascalsLaw", "get_F"): PascalsLawSolver.get_F,
    ("PascalsLaw", "get_S"): PascalsLawSolver.get_S,
    ("ArchimedesLaw", "get_F"): ArchimedesLawSolver.get_F,
    ("ArchimedesLaw", "get_rho"): ArchimedesLawSolver.get_rho,
    ("ArchimedesLaw", "get_V"): ArchimedesLawSolver.get_V,
    ("ArchimedesLaw", "get_g"): ArchimedesLawSolver.get_g,
    ("HydrostaticPressureLaw", "get_p"): HydrostaticPressureLawSolver.get_p,
    ("HydrostaticPressureLaw", "get_rho"): HydrostaticPressureLawSolver.get_rho,
    ("HydrostaticPressureLaw", "get_g"): HydrostaticPressureLawSolver.get_g,
    ("HydrostaticPressureLaw", "get_h"): HydrostaticPressureLawSolver.get_h,

    ("SensibleHeatLaw", "get_Q"): SensibleHeatLawSolver.get_Q,
    ("SensibleHeatLaw", "get_c"): SensibleHeatLawSolver.get_c,
    ("SensibleHeatLaw", "get_m"): SensibleHeatLawSolver.get_m,
    ("SensibleHeatLaw", "get_Dt"): SensibleHeatLawSolver.get_Dt,
    ("CombustionHeatLaw", "get_Q"): CombustionHeatLawSolver.get_Q,
    ("CombustionHeatLaw", "get_q"): CombustionHeatLawSolver.get_q,
    ("CombustionHeatLaw", "get_m"): CombustionHeatLawSolver.get_m,
    ("FusionHeatLaw", "get_Q"): FusionHeatLawSolver.get_Q,
    ("FusionHeatLaw", "get_lmb"): FusionHeatLawSolver.get_lmb,
    ("FusionHeatLaw", "get_m"): FusionHeatLawSolver.get_m,
    ("VaporizationHeatLaw", "get_Q"): VaporizationHeatLawSolver.get_Q,
    ("VaporizationHeatLaw", "get_L"): VaporizationHeatLawSolver.get_L,
    ("VaporizationHeatLaw", "get_m"): VaporizationHeatLawSolver.get_m,
    ("MolarMassLaw", "get_v"): MolarMassLawSolver.get_v,
    ("MolarMassLaw", "get_m"): MolarMassLawSolver.get_m,
    ("MolarMassLaw", "get_M"): MolarMassLawSolver.get_M,
    ("MendeleevClapeyronLaw", "get_p"): MendeleevClapeyronLawSolver.get_p,
    ("MendeleevClapeyronLaw", "get_V"): MendeleevClapeyronLawSolver.get_V,
    ("MendeleevClapeyronLaw", "get_v"): MendeleevClapeyronLawSolver.get_v,
    ("MendeleevClapeyronLaw", "get_T"): MendeleevClapeyronLawSolver.get_T,
}
