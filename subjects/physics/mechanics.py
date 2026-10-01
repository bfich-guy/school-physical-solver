from decimal import Decimal


#region Dynamics

class NewtonSecondLaw:
    def __init__(self) -> None:
        pass


    def get_F(self, *, m: Decimal, a: Decimal) -> Decimal:
        F: Decimal = m * a
        return F


    def get_m(self, *, F: Decimal, a: Decimal) -> Decimal:
        m: Decimal = F / a
        return m


    def get_a(self, *, F: Decimal, m: Decimal) -> Decimal:
        a: Decimal = F / m
        return a


class HookesLaw:
    def __init__(self) -> None:
        pass


    def get_F(self, *, k: Decimal, Dx: Decimal) -> Decimal:
        F: Decimal = k * Dx
        return F


    def get_k(self, *, F: Decimal, Dx: Decimal) -> Decimal:
        k: Decimal = F / Dx
        return k


    def get_Dx(self, *, F: Decimal, k: Decimal) -> Decimal:
        Dx: Decimal = F / k
        return Dx


class AmontonsCoulombLaw:
    def __init__(self) -> None:
        pass


    def get_F(self, *, mu: Decimal, N: Decimal) -> Decimal:
        F: Decimal = mu * N
        return F


    def get_mu(self, *, F: Decimal, N: Decimal) -> Decimal:
        mu: Decimal = F / N
        return mu


    def get_N(self, *, F: Decimal, mu: Decimal) -> Decimal:
        N: Decimal = F / mu
        return N


class NormalReactionLaw:
    def __init__(self) -> None:
        pass


    def get_N(self, *, F: Decimal, cosa: Decimal) -> Decimal:
        N: Decimal = F * cosa
        return N


    def get_F(self, *, N: Decimal, cosa: Decimal) -> Decimal:
        F: Decimal = N / cosa
        return F


    def get_cosa(self, *, N: Decimal, F: Decimal) -> Decimal:
        cosa: Decimal = N / F
        return cosa


class MomentumLaw:
    def __init__(self) -> None:
        pass


    def get_p(self, *, m: Decimal, v: Decimal) -> Decimal:
        p: Decimal = m * v
        return p


    def get_m(self, *, p: Decimal, v: Decimal) -> Decimal:
        m: Decimal = p / v
        return m


    def get_v(self, *, p: Decimal, m: Decimal) -> Decimal:
        v: Decimal = p / m
        return v


class KineticEnergyLaw:
    def __init__(self) -> None:
        pass


    def get_E(self, *, p: Decimal, v: Decimal) -> Decimal:
        E: Decimal = (p * v) / Decimal("2")
        return E


    def get_p(self, *, E: Decimal, v: Decimal) -> Decimal:
        p: Decimal = (Decimal("2") * E) / v
        return p


    def get_v(self, *, E: Decimal, p: Decimal) -> Decimal:
        v: Decimal = (Decimal("2") * E) / p
        return v


class PotentialEnergyLaw:
    def __init__(self) -> None:
        pass


    def get_E(self, *, F: Decimal, h: Decimal) -> Decimal:
        E: Decimal = F * h
        return E


    def get_F(self, *, E: Decimal, h: Decimal) -> Decimal:
        F: Decimal = E / h
        return F


    def get_h(self, *, E: Decimal, F: Decimal) -> Decimal:
        h: Decimal = E / F
        return h


class MechanicalWorkLaw:
    def __init__(self) -> None:
        pass


    def get_A(self, *, F: Decimal, S: Decimal, cosa: Decimal) -> Decimal:
        A: Decimal = F * S * cosa
        return A


    def get_F(self, *, A: Decimal, S: Decimal, cosa: Decimal) -> Decimal:
        F: Decimal = A / (S * cosa)
        return F


    def get_S(self, *, A: Decimal, F: Decimal, cosa: Decimal) -> Decimal:
        S: Decimal = A / (F * cosa)
        return S


    def get_cosa(self, *, A: Decimal, F: Decimal, S: Decimal) -> Decimal:
        cosa: Decimal = A / (F * S)
        return cosa


class MechanicalPowerLaw:
    def __init__(self) -> None:
        pass


    def get_P(self, *, A: Decimal, t: Decimal) -> Decimal:
        P: Decimal = A / t
        return P


    def get_A(self, *, P: Decimal, t: Decimal) -> Decimal:
        A: Decimal = P * t
        return A


    def get_t(self, *, A: Decimal, P: Decimal) -> Decimal:
        t: Decimal = A / P
        return t

#endregion


#region Kinematics

class LinearAccelerationLaw:
    def __init__(self) -> None:
        pass


    def get_a(self, *, Dv: Decimal, Dt: Decimal) -> Decimal:
        a: Decimal = Dv / Dt
        return a


    def get_Dv(self, *, a: Decimal, Dt: Decimal) -> Decimal:
        Dv: Decimal = a * Dt
        return Dv


    def get_Dt(self, *, Dv: Decimal, a: Decimal) -> Decimal:
        Dt: Decimal = Dv / a
        return Dt


class UniformlyAcceleratedRectilinearMotionLaw:
    def __init__(self) -> None:
        pass


    def get_S(self, *, t: Decimal, v0: Decimal, Dv: Decimal) -> Decimal:
        S: Decimal = t * (v0 + (Dv / Decimal("2")))
        return S


    def get_t(self, *, S: Decimal, v0: Decimal, Dv: Decimal) -> Decimal:
        t: Decimal = S / (v0 + (Dv / Decimal("2")))
        return t


    def get_v0(self, *, S: Decimal, t: Decimal, Dv: Decimal) -> Decimal:
        v0: Decimal = (S - t * (Dv / Decimal("2"))) / t
        return v0


    def get_Dv(self, *, S: Decimal, t: Decimal, v0: Decimal) -> Decimal:
        Dv: Decimal = (Decimal("2") * (S - t * v0)) / t
        return Dv


class CentripetalAccelerationLaw:
    def __init__(self) -> None:
        pass


    def get_a(self, *, v: Decimal, w: Decimal) -> Decimal:
        a: Decimal = v * w
        return a


    def get_v(self, *, a: Decimal, w: Decimal) -> Decimal:
        v: Decimal = a / w
        return v


    def get_w(self, *, a: Decimal, v: Decimal) -> Decimal:
        w: Decimal = a / v
        return w


class TrajectoryRadiusLaw:
    def __init__(self) -> None:
        pass


    def get_R(self, *, v: Decimal, w: Decimal) -> Decimal:
        R: Decimal = v / w
        return R


    def get_v(self, *, w: Decimal, R: Decimal) -> Decimal:
        v: Decimal = w * R
        return v


    def get_w(self, *, v: Decimal, R: Decimal) -> Decimal:
        w: Decimal = v / R
        return w

#endregion


#region Statics

class PascalsLaw:
    def __init__(self) -> None:
        pass


    def get_p(self, *, F: Decimal, S: Decimal) -> Decimal:
        p: Decimal = F / S
        return p


    def get_F(self, *, p: Decimal, S: Decimal) -> Decimal:
        F: Decimal = p * S
        return F


    def get_S(self, *, F: Decimal, p: Decimal) -> Decimal:
        S: Decimal = F / p
        return S


class ArchimedesLaw:
    def __init__(self) -> None:
        pass


    def get_F(self, *, rho: Decimal, V: Decimal, g: Decimal) -> Decimal:
        F: Decimal = rho * V * g
        return F


    def get_rho(self, *, F: Decimal, V: Decimal, g: Decimal) -> Decimal:
        rho: Decimal = F / (V * g)
        return rho


    def get_V(self, *, F: Decimal, rho: Decimal, g: Decimal) -> Decimal:
        V: Decimal = F / (rho * g)
        return V


    def get_g(self, *, F: Decimal, rho: Decimal, V: Decimal) -> Decimal:
        g: Decimal = F / (rho * V)
        return g


class HydrostaticPressureLaw:
    def __init__(self) -> None:
        pass


    def get_p(self, *, rho: Decimal, g: Decimal, h: Decimal) -> Decimal:
        p: Decimal = rho * g * h
        return p


    def get_rho(self, *, p: Decimal, g: Decimal, h: Decimal) -> Decimal:
        rho: Decimal = p / (g * h)
        return rho


    def get_g(self, *, p: Decimal, rho: Decimal, h: Decimal) -> Decimal:
        g: Decimal = p / (rho * h)
        return g


    def get_h(self, *, p: Decimal, rho: Decimal, g: Decimal) -> Decimal:
        h: Decimal = p / (rho * g)
        return h

#endregion
