from pydantic import BaseModel


#region Algebra

class LinearEquationSolving(BaseModel):
    a: str
    b: str


class QuadraticEquationSolving(BaseModel):
    a: str
    b: str
    c: str


class DerivativeEquationSolving(BaseModel):
    d: str
    Dy: str
    Dx: str


class TangentEquationSolving(BaseModel):
    y: str
    dfx: str
    Dx: str
    fx: str


class LinearGraphFunction(BaseModel):
    x: str
    y: str
    a: str
    b: str


class QuadraticGraphFunction(BaseModel):
    x: str
    y: str
    a: str
    b: str
    c: str


class CircleGraphFunction(BaseModel):
    r: str
    Dx: str
    Dy: str


class ArithmeticProgressionSumTheorem(BaseModel):
    S: str
    a1: str
    an: str
    n: str


class GeometricProgressionSumTheorem(BaseModel):
    S: str
    b1: str
    bn: str
    q: str


class ArithmeticProgressionTermTheorem(BaseModel):
    an: str
    a1: str
    d: str
    n: str


class GeometricProgressionTermTheorem(BaseModel):
    bn: str
    b1: str
    q: str
    n: str


class VectorCorrdinatesTheorem(BaseModel):
    a: list[str]
    B: list[str]
    A: list[str]


class VectorMagnitudeTheorem(BaseModel):
    a: list[str]


class VectorDotProductTheorem(BaseModel):
    a: list[str]
    b: list[str]


class AngleBetweenVectorsCosinusTheorem(BaseModel):
    cosa: str
    ab: str
    la: str
    lb: str

#endregion


#region Geometry

class CircleAreaTheorem(BaseModel):
    S: list[str]
    pi: list[str]
    r: list[str]


class CircumferenceTheorem(BaseModel):
    S: list[str]
    pi: list[str]
    r: list[str]


class ParallelogramAreaByBaseAndHeightTheorem(BaseModel):
    S: list[str]
    a: list[str]
    h: list[str]


class TrapezoidMidlineTheorem(BaseModel):
    m: list[str]
    a: list[str]
    h: list[str]


class TrapezoidAreaByMidlineAndHeightTheorem(BaseModel):
    S: list[str]
    m: list[str]
    h: list[str]


class TriangleAreaByBaseAndHeightTheorem(BaseModel):
    S: list[str]
    a: list[str]
    h: list[str]


class HeronTheorem(BaseModel):
    a: list[str]
    b: list[str]
    c: list[str]


class CosineTheorem(BaseModel):
    a: list[str]
    b: list[str]
    c: list[str]
    cosa: list[str]


class SineTheorem(BaseModel):
    a: list[str]
    sina: list[str]
    R: list[str]


class PythagoreanTheorem(BaseModel):
    a: list[str]
    b: list[str]
    c: list[str]


class TriangleAreaByInscribedCircleTheorem(BaseModel):
    S: list[str]
    p: list[str]
    r: list[str]


class TriangleAreaByCircumscripedCircleTheorem(BaseModel):
    S: list[str]
    a: list[str]
    b: list[str]
    c: list[str]
    R: list[str]


class TriangleSideProjection(BaseModel):
    c: str
    h: str
    cossina: str

#endregion


#region Electromagnetics

class OhmsSpecificLaw(BaseModel):
    U: str
    I: str
    R: str


class OhmsFullLaw(BaseModel):
    E: str
    U: str
    I: str
    r: str


class WattsLaw(BaseModel):
    P: str
    U: str
    I: str


class JouleLenzLaw(BaseModel):
    Q: str
    P: str
    t: str


class CoulombsLaw(BaseModel):
    F: str
    k: str
    q1: str
    q2: str
    r: str


class ConductorResistanceLaw(BaseModel):
    R: str
    rho: str
    l: str
    S: str


class AmperesLaw(BaseModel):
    F: str
    I: str
    B: str
    L: str
    sina: str


class LorentzLaw(BaseModel):
    F: str
    q: str
    v: str
    B: str
    sina: str


class FaradaysLaw(BaseModel):
    E: str
    Dphi: str
    Dt: str


class MagneticFluxLaw(BaseModel):
    phi: str
    B: str
    S: str
    cosa: str

#endregion


#region Mechanics

class NewtonSecondLaw(BaseModel):
    F: str
    m: str
    a: str


class HookesLaw(BaseModel):
    F: str
    k: str
    Dx: str


class AmontonsCoulombsLaw(BaseModel):
    F: str
    mu: str
    N: str


class NormalReactionLaw(BaseModel):
    N: str
    F: str
    cosa: str


class MomentumLaw(BaseModel):
    p: str
    m: str
    v: str


class KineticEnergyLaw(BaseModel):
    E: str
    p: str
    v: str


class PotentialEnergyLaw(BaseModel):
    E: str
    F: str
    h: str


class MechanicalWorkLaw(BaseModel):
    A: str
    F: str
    S: str
    cosa: str


class MechanicalPowerLaw(BaseModel):
    P: str
    A: str
    t: str


class LinearAccelerationLaw(BaseModel):
    a: str
    Dv: str
    Dt: str


class UniformlyAcceleratedRectilinearMotionLaw(BaseModel):
    S: str
    t: str
    v0: str
    Dv: str


class CentripetalAccelerationLaw(BaseModel):
    a: str
    v: str
    w: str


class TrajectoryRadiusLaw(BaseModel):
    R: str
    v: str
    w: str


class PascalsLaw(BaseModel):
    p: str
    F: str
    S: str


class ArchimedesLaw(BaseModel):
    p: str
    rho: str
    g: str
    h: str


class HydrostaticPressureLaw(BaseModel):
    p: str
    rho: str
    g: str
    h: str   

#endregion


#region Thermodynamics

class SensibleHeatLaw(BaseModel):
    Q: str
    c: str
    m: str
    Dt: str


class CombustionHeatLaw(BaseModel):
    Q: str
    q: str
    m: str


class FusionHeatLaw(BaseModel):
    Q: str
    lmb: str
    m: str


class VaporizationHeatLaw(BaseModel):
    Q: str
    L: str
    m: str


class MendeleevClapeyronLaw(BaseModel):
    p: str
    V: str
    v: str
    T: str


class MolarMassLaw(BaseModel):
    v: str
    m: str
    M: str

#endregion
