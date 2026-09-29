from decimal import Decimal


#region Dynamics

class NewtonSecondLaw:
    def __init__(self, *, F: Decimal, m: Decimal, a: Decimal) -> None:
        self.F: Decimal = F
        self.m: Decimal = m
        self.a: Decimal = a


    def get_F(self) -> Decimal:
        F: Decimal = self.m * self.a
        return F


    def get_m(self) -> Decimal:
        m: Decimal = self.F / self.a
        return m


    def get_a(self) -> Decimal:
        a: Decimal = self.F / self.m
        return a


class HookesLaw:
    def __init__(self, *, F: Decimal, k: Decimal, Dx: Decimal) -> None:
        self.F: Decimal = F
        self.k: Decimal = k
        self.Dx: Decimal = Dx


    def get_F(self) -> Decimal:
        F: Decimal = self.k * self.Dx
        return F


    def get_k(self) -> Decimal:
        k: Decimal = self.F / self.Dx
        return k


    def get_Dx(self) -> Decimal:
        Dx: Decimal = self.F / self.k
        return Dx


class AmontonsCoulombLaw:
    def __init__(self, *, F: Decimal, mu: Decimal, N: Decimal) -> None:
        self.F: Decimal = F
        self.mu: Decimal = mu
        self.N: Decimal = N


    def get_F(self) -> Decimal:
        F: Decimal = self.mu * self.N
        return F


    def get_mu(self) -> Decimal:
        mu: Decimal = self.F / self.N
        return mu


    def get_N(self) -> Decimal:
        N: Decimal = self.F / self.mu
        return N


class NormalReactionLaw:
    def __init__(self, *, N: Decimal, F: Decimal, cosa: Decimal) -> None:
        self.N: Decimal = N
        self.F: Decimal = F
        self.cosa: Decimal = cosa


    def get_N(self) -> Decimal:
        N: Decimal = self.F * self.cosa
        return N


    def get_F(self) -> Decimal:
        F: Decimal = self.N / self.cosa
        return F


    def get_cosa(self) -> Decimal:
        cosa: Decimal = self.N / self.F
        return cosa


class MomentumLaw:
    def __init__(self, *, p: Decimal, m: Decimal, v: Decimal) -> None:
        self.p: Decimal = p
        self.m: Decimal = m
        self.v: Decimal = v


    def get_p(self) -> Decimal:
        p: Decimal = self.m * self.v
        return p


    def get_m(self) -> Decimal:
        m: Decimal = self.p / self.v
        return m


    def get_v(self) -> Decimal:
        v: Decimal = self.p / self.m
        return v


class MomentumConservationLaw:
    def __init__(self, *, p1i: Decimal, p2i: Decimal, p1f: Decimal, p2f: Decimal) -> None:
        self.p1i: Decimal = p1i
        self.p2i: Decimal = p2i
        self.p1f: Decimal = p1f
        self.p2f: Decimal = p2f


    def get_p1i(self) -> Decimal:
        p1i: Decimal = self.p1f + self.p2f - self.p2i
        return p1i


    def get_p2i(self) -> Decimal:
        p2i: Decimal = self.p1f + self.p2f - self.p1i
        return p2i


    def get_p1f(self) -> Decimal:
        p1f: Decimal = self.p1i + self.p2i - self.p2f
        return p1f


    def get_p2f(self) -> Decimal:
        p2f: Decimal = self.p1i + self.p2i - self.p1f
        return p2f


class KineticEnergyLaw:
    def __init__(self, *, E: Decimal, p: Decimal, v: Decimal) -> None:
        self.E: Decimal = E
        self.p: Decimal = p
        self.v: Decimal = v


    def get_E(self) -> Decimal:
        E: Decimal = (self.p * self.v) / Decimal("2")
        return E


    def get_p(self) -> Decimal:
        p: Decimal = (Decimal("2") * self.E) / self.v
        return p


    def get_v(self) -> Decimal:
        v: Decimal = (Decimal("2") * self.E) / self.p
        return v


class PotentialEnergyLaw:
    def __init__(self, *, E: Decimal, F: Decimal, h: Decimal) -> None:
        self.E: Decimal = E
        self.F: Decimal = F
        self.h: Decimal = h


    def get_E(self) -> Decimal:
        E: Decimal = self.F * self.h
        return E


    def get_F(self) -> Decimal:
        F: Decimal = self.E / self.h
        return F


    def get_h(self) -> Decimal:
        h: Decimal = self.E / self.F
        return h


class MechanicalWorkLaw:
    def __init__(self, *, A: Decimal, F: Decimal, S: Decimal, cosa: Decimal) -> None:
        self.A: Decimal = A
        self.F: Decimal = F
        self.S: Decimal = S
        self.cosa: Decimal = cosa


    def get_A(self) -> Decimal:
        A: Decimal = self.F * self.S * self.cosa
        return A


    def get_F(self) -> Decimal:
        F: Decimal = self.A / (self.S * self.cosa)
        return F


    def get_S(self) -> Decimal:
        S: Decimal = self.A / (self.F * self.cosa)
        return S


    def get_cosa(self) -> Decimal:
        cosa: Decimal = self.A / (self.F * self.S)
        return cosa


class MechanicalPowerLaw:
    def __init__(self, *, P: Decimal, A: Decimal, t: Decimal) -> None:
        self.P: Decimal = P
        self.A: Decimal = A
        self.t: Decimal = t


    def get_P(self) -> Decimal:
        P: Decimal = self.A / self.t
        return P


    def get_A(self) -> Decimal:
        A: Decimal = self.P * self.t
        return A


    def get_t(self) -> Decimal:
        t: Decimal = self.A / self.P
        return t

#endregion


#region Kinematics

class LinearAccelerationLaw:
    def __init__(self, *, a: Decimal, Dv: Decimal, Dt: Decimal) -> None:
        self.a: Decimal = a
        self.Dv: Decimal = Dv
        self.Dt: Decimal = Dt


    def get_a(self) -> Decimal:
        a: Decimal = self.Dv / self.Dt
        return a


    def get_Dv(self) -> Decimal:
        Dv: Decimal = self.a * self.Dt
        return Dv


    def get_Dt(self) -> Decimal:
        Dt: Decimal = self.Dv / self.a
        return Dt


class UniformlyAcceleratedRectilinearMotionLaw:
    def __init__(self, *, S: Decimal, t: Decimal, v0: Decimal, Dv: Decimal) -> None:
        self.S: Decimal = S
        self.t: Decimal = t
        self.v0: Decimal = v0
        self.Dv: Decimal = Dv


    def get_S(self) -> Decimal:
        S: Decimal = self.t * (self.v0 + (self.Dv / Decimal("2")))
        return S


    def get_t(self) -> Decimal:
        t: Decimal = self.S / (self.v0 + (self.Dv / Decimal("2")))
        return t


    def get_v0(self) -> Decimal:
        v0: Decimal = (self.S - self.t * (self.Dv / Decimal("2"))) / self.t
        return v0


    def get_Dv(self) -> Decimal:
        Dv: Decimal = (Decimal("2") * (self.S - self.t * self.v0)) / self.t
        return Dv


class CentripetalAccelerationLaw:
    def __init__(self, *, a: Decimal, v: Decimal, w: Decimal) -> None:
        self.a: Decimal = a
        self.v: Decimal = v
        self.w: Decimal = w


    def get_a(self) -> Decimal:
        a: Decimal = self.v * self.w
        return a


    def get_v(self) -> Decimal:
        v: Decimal = self.a / self.w
        return v


    def get_w(self) -> Decimal:
        w: Decimal = self.a / self.v
        return w


class TrajectoryRadiusLaw:
    def __init__(self, *, R: Decimal, v: Decimal, w: Decimal) -> None:
        self.R: Decimal = R
        self.v: Decimal = v
        self.w: Decimal = w


    def get_R(self) -> Decimal:
        R: Decimal = self.v / self.w
        return R


    def get_v(self) -> Decimal:
        v: Decimal = self.w * self.R
        return v


    def get_w(self) -> Decimal:
        w: Decimal = self.v / self.R
        return w

#endregion


#region Statics

class PascalsLaw:
    def __init__(self, *, p: Decimal, F: Decimal, S: Decimal) -> None:
        self.p: Decimal = p
        self.F: Decimal = F
        self.S: Decimal = S


    def get_p(self) -> Decimal:
        p: Decimal = self.F / self.S
        return p


    def get_F(self) -> Decimal:
        F: Decimal = self.p * self.S
        return F


    def get_S(self) -> Decimal:
        S: Decimal = self.F / self.p
        return S


class ArchimedesLaw:
    def __init__(self, *, F: Decimal, rho: Decimal, V: Decimal, g: Decimal) -> None:
        self.F: Decimal = F
        self.rho: Decimal = rho
        self.V: Decimal = V
        self.g: Decimal = g


    def get_F(self) -> Decimal:
        F: Decimal = self.rho * self.V * self.g
        return F


    def get_rho(self) -> Decimal:
        rho: Decimal = self.F / (self.V * self.g)
        return rho


    def get_V(self) -> Decimal:
        V: Decimal = self.F / (self.rho * self.g)
        return V


    def get_g(self) -> Decimal:
        g: Decimal = self.F / (self.rho * self.V)
        return g


class HydrostaticPressureLaw:
    def __init__(self, *, p: Decimal, rho: Decimal, g: Decimal, h: Decimal) -> None:
        self.p: Decimal = p
        self.rho: Decimal = rho
        self.g: Decimal = g
        self.h: Decimal = h


    def get_p(self) -> Decimal:
        p: Decimal = self.rho * self.g * self.h
        return p


    def get_rho(self) -> Decimal:
        rho: Decimal = self.p / (self.g * self.h)
        return rho


    def get_g(self) -> Decimal:
        g: Decimal = self.p / (self.rho * self.h)
        return g


    def get_h(self) -> Decimal:
        h: Decimal = self.p / (self.rho * self.g)
        return h

#endregion
