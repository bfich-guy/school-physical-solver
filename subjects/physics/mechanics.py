from decimal import Decimal


#region Dynamics

class SecondNewtonLaw:
    def __init__(self, *, F: Decimal | None = None, m: Decimal | None = None, a: Decimal | None = None) -> None:
        self.F: Decimal | None = F
        self.m: Decimal | None = m
        self.a: Decimal | None = a


    def get_F(self) -> Decimal | None:
        try:
            F: Decimal = self.m * self.a #type: ignore
            return F
        except TypeError:
            return None


    def get_m(self) -> Decimal | None:
        try:
            m: Decimal = self.F / self.a #type: ignore
            return m
        except (ZeroDivisionError, TypeError):
            return None


    def get_a(self) -> Decimal | None:
        try:
            a: Decimal = self.F / self.m #type: ignore
            return a
        except (ZeroDivisionError, TypeError):
            return None


class HookesLaw:
    def __init__(self, *, F: Decimal | None = None, k: Decimal | None = None, Dx: Decimal | None = None) -> None:
        self.F: Decimal | None = F
        self.k: Decimal | None = k
        self.Dx: Decimal | None = Dx


    def get_F(self) -> Decimal | None:
        try:
            F: Decimal = self.k * self.Dx #type: ignore
            return F
        except TypeError:
            return None


    def get_k(self) -> Decimal | None:
        try:
            k: Decimal = self.F / self.Dx #type: ignore
            return k
        except (ZeroDivisionError, TypeError):
            return None


    def get_Dx(self) -> Decimal | None:
        try:
            Dx: Decimal = self.F / self.k #type: ignore
            return Dx
        except (ZeroDivisionError, TypeError):
            return None


class AmontonsCoulombLaw:
    def __init__(self, *, F: Decimal | None = None, mu: Decimal | None = None, N: Decimal | None = None) -> None:
        self.F: Decimal | None = F
        self.mu: Decimal | None = mu
        self.N: Decimal | None = N


    def get_F(self) -> Decimal | None:
        try:
            F: Decimal = self.mu * self.N #type: ignore
            return F
        except TypeError:
            return None


    def get_mu(self) -> Decimal | None:
        try:
            mu: Decimal = self.F / self.N #type: ignore
            return mu
        except (ZeroDivisionError, TypeError):
            return None


    def get_N(self) -> Decimal | None:
        try:
            N: Decimal = self.F / self.mu #type: ignore
            return N
        except (ZeroDivisionError, TypeError):
            return None


class NormalReactionLaw:
    def __init__(self, *, N: Decimal | None = None, F: Decimal | None = None, cosa: Decimal | None = None) -> None:
        self.N: Decimal | None = N
        self.F: Decimal | None = F
        self.cosa: Decimal | None = cosa


    def get_N(self) -> Decimal | None:
        try:
            N: Decimal = self.F * self.cosa #type: ignore
            return N
        except TypeError:
            return None


    def get_F(self) -> Decimal | None:
        try:
            F: Decimal = self.N / self.cosa #type: ignore
            return F
        except (ZeroDivisionError, TypeError):
            return None


    def get_cosa(self) -> Decimal | None:
        try:
            cosa: Decimal = self.N / self.F #type: ignore
            return cosa
        except (ZeroDivisionError, TypeError):
            return None


class MomentumLaw:
    def __init__(self, *, p: Decimal | None = None, m: Decimal | None = None, v: Decimal | None = None) -> None:
        self.p: Decimal | None = p
        self.m: Decimal | None = m
        self.v: Decimal | None = v


    def get_p(self) -> Decimal | None:
        try:
            p: Decimal = self.m * self.v #type: ignore
            return p
        except TypeError:
            return None


    def get_m(self) -> Decimal | None:
        try:
            m: Decimal = self.p / self.v #type: ignore
            return m
        except (ZeroDivisionError, TypeError):
            return None


    def get_v(self) -> Decimal | None:
        try:
            v: Decimal = self.p / self.m #type: ignore
            return v
        except (ZeroDivisionError, TypeError):
            return None


class MomentumConservationLaw:
    def __init__(self, *, p1i: Decimal | None = None, p2i: Decimal | None = None, p1f: Decimal | None = None, p2f: Decimal | None = None) -> None:
        self.p1i: Decimal | None = p1i
        self.p2i: Decimal | None = p2i
        self.p1f: Decimal | None = p1f
        self.p2f: Decimal | None = p2f


    def get_p1i(self) -> Decimal | None:
        try:
            p1i: Decimal = self.p1f + self.p2f - self.p2i #type: ignore
            return p1i
        except TypeError:
            return None

    def get_p2i(self) -> Decimal | None:
        try:
            p2i: Decimal = self.p1f + self.p2f - self.p1i #type: ignore
            return p2i
        except TypeError:
            return None

    def get_p1f(self) -> Decimal | None:
        try:
            p1f: Decimal = self.p1i + self.p2i - self.p2f #type: ignore
            return p1f
        except TypeError:
            return None

    def get_p2f(self) -> Decimal | None:
        try:
            p2f: Decimal = self.p1i + self.p2i - self.p1f #type: ignore
            return p2f
        except TypeError:
            return None


class KineticEnergyLaw:
    def __init__(self, *, E: Decimal | None = None, p: Decimal | None = None, v: Decimal | None = None) -> None:
        self.E: Decimal | None = E
        self.p: Decimal | None = p
        self.v: Decimal | None = v


    def get_E(self) -> Decimal | None:
        try:
            E: Decimal = (self.p * self.v) / Decimal("2") #type: ignore
            return E
        except TypeError:
            return None


    def get_p(self) -> Decimal | None:
        try:
            p: Decimal = (Decimal("2") * self.E) / self.v #type: ignore
            return p
        except (ZeroDivisionError, TypeError):
            return None


    def get_v(self) -> Decimal | None:
        try:
            v: Decimal = (Decimal("2") * self.E) / self.p #type: ignore
            return v
        except (ZeroDivisionError, TypeError):
            return None


class PotentialEnergyLaw:
    def __init__(self, *, E: Decimal | None = None, F: Decimal | None = None, h: Decimal | None = None) -> None:
        self.E: Decimal | None = E
        self.F: Decimal | None = F
        self.h: Decimal | None = h


    def get_E(self) -> Decimal | None:
        try:
            E: Decimal = self.F * self.H #type: ignore
            return E
        except TypeError:
            return None


    def get_F(self) -> Decimal | None:
        try:
            F: Decimal = self.E / self.h #type: ignore
            return F
        except (ZeroDivisionError, TypeError):
            return None


    def get_h(self) -> Decimal | None:
        try:
            h: Decimal = self.E / self.F #type: ignore
            return h
        except (ZeroDivisionError, TypeError):
            return None


class MechanicalWorkLaw:
    def __init__(self, *, A: Decimal | None = None, F: Decimal | None = None, S: Decimal | None = None, cosa: Decimal | None = None) -> None:
        self.A: Decimal | None = A
        self.F: Decimal | None = F
        self.S: Decimal | None = S
        self.cosa: Decimal | None = cosa


    def get_A(self) -> Decimal | None:
        try:
            A: Decimal = self.F * self.S * self.cosa #type: ignore
            return A
        except TypeError:
            return None


    def get_F(self) -> Decimal | None:
        try:
            F: Decimal = self.A / (self.S * self.cosa) #type: ignore
            return F
        except (ZeroDivisionError, TypeError):
            return None


    def get_S(self) -> Decimal | None:
        try:
            S: Decimal = self.A / (self.F * self.cosa) #type: ignore
            return S
        except (ZeroDivisionError, TypeError):
            return None


    def get_cosa(self) -> Decimal | None:
        try:
            cosa: Decimal = self.A / (self.F * self.S) #type: ignore
            return cosa
        except (ZeroDivisionError, TypeError):
            return None


class MechanicalPowerLaw:
    def __init__(self, *, P: Decimal | None = None, A: Decimal | None = None, t: Decimal | None = None) -> None:
        self.P: Decimal | None = P
        self.A: Decimal | None = A
        self.t: Decimal | None = t


    def get_P(self) -> Decimal | None:
        try:
            P: Decimal = self.A / self.t #type: ignore
            return P
        except (ZeroDivisionError, TypeError):
            return None


    def get_A(self) -> Decimal | None:
        try:
            A: Decimal = self.P * self.t #type: ignore
            return A
        except TypeError:
            return None


    def get_t(self) -> Decimal | None:
        try:
            t: Decimal = self.A / self.P #type: ignore
            return t
        except (ZeroDivisionError, TypeError):
            return None

#endregion


#region Kinematics

class LinearAccelerationLaw:
    def __init__(self, *, a: Decimal | None = None, Dv: Decimal | None = None, Dt: Decimal | None = None) -> None:
        self.a: Decimal | None = a
        self.Dv: Decimal | None = Dv
        self.Dt: Decimal | None = Dt


    def get_a(self) -> Decimal | None:
        try:
            a: Decimal = self.Dv / self.Dt#type: ignore
            return a
        except (ZeroDivisionError, TypeError):
            return None


    def get_Dv(self) -> Decimal | None:
        try:
            Dv: Decimal = self.a * self.Dt #type: ignore
            return Dv
        except TypeError:
            return None


    def get_Dt(self) -> Decimal | None:
        try:
            Dt: Decimal = self.Dv / self.a #type: ignore
            return Dt
        except (ZeroDivisionError, TypeError):
            return None


class CentripetalAccelerationLaw:
    def __init__(self, *, a: Decimal | None = None, v: Decimal | None = None, w: Decimal | None = None) -> None:
        self.a: Decimal | None = a
        self.v: Decimal | None = v
        self.w: Decimal | None = w


    def get_a(self) -> Decimal | None:
        try:
            a: Decimal = self.v * self.w #type: ignore
            return a
        except TypeError:
            return None


    def get_v(self) -> Decimal | None:
        try:
            v: Decimal = self.a / self.w #type: ignore
            return v
        except (ZeroDivisionError, TypeError):
            return None


    def get_w(self) -> Decimal | None:
        try:
            w: Decimal = self.a / self.v #type: ignore
            return w
        except (ZeroDivisionError, TypeError):
            return None


class TrajectoryRadiusLaw:
    def __init__(self, *, R: Decimal | None = None, v: Decimal | None = None, w: Decimal | None = None) -> None:
        self.R: Decimal | None = R
        self.v: Decimal | None = v
        self.w: Decimal | None = w


    def get_R(self) -> Decimal | None:
        try:
            R: Decimal = self.v / self.w #type: ignore
            return R
        except (ZeroDivisionError, TypeError):
            return None


    def get_v(self) -> Decimal | None:
        try:
            v: Decimal = self.w * self.R #type: ignore
            return v
        except TypeError:
            return None


    def get_w(self) -> Decimal | None:
        try:
            w: Decimal = self.v / self.R #type: ignore
            return w
        except (ZeroDivisionError, TypeError):
            return None

#endregion


#region Statics

class PascalsLaw:
    def __init__(self, *, p: Decimal | None = None, F: Decimal | None = None, S: Decimal | None = None) -> None:
        self.p: Decimal | None = p
        self.F: Decimal | None = F
        self.S: Decimal | None = S


    def get_p(self) -> Decimal | None:
        try:
            p: Decimal = self.F / self.S #type: ignore
            return p
        except (ZeroDivisionError, TypeError):
            return None


    def get_F(self) -> Decimal | None:
        try:
            F: Decimal = self.p * self.S #type: ignore
            return F
        except TypeError:
            return None


    def get_S(self) -> Decimal | None:
        try:
            S: Decimal = self.F / self.p #type: ignore
            return S
        except (ZeroDivisionError, TypeError):
            return None


class ArchimedesLaw:
    def __init__(self, *, F: Decimal | None = None, rho: Decimal | None = None, V: Decimal | None = None, g: Decimal | None = None) -> None:
        self.F: Decimal | None = F
        self.rho: Decimal | None = rho
        self.V: Decimal | None = V
        self.g: Decimal | None = g


    def get_F(self) -> Decimal | None:
        try:
            F: Decimal = self.rho * self.V * self.g #type: ignore
            return F
        except TypeError:
            return None


    def get_rho(self) -> Decimal | None:
        try:
            rho: Decimal = self.F / (self.V * self.g) #type: ignore
            return rho
        except (ZeroDivisionError, TypeError):
            return None


    def get_V(self) -> Decimal | None:
        try:
            V: Decimal = self.F / (self.rho * self.g) #type: ignore
            return V
        except (ZeroDivisionError, TypeError):
            return None


    def get_g(self) -> Decimal | None:
        try:
            g: Decimal = self.F / (self.rho * self.V) #type: ignore
            return g
        except (ZeroDivisionError, TypeError):
            return None


class HydrostaticPressureLaw:
    def __init__(self, *, p: Decimal | None = None, rho: Decimal | None = None, g: Decimal | None = None, h: Decimal | None = None) -> None:
        self.p: Decimal | None = p
        self.rho: Decimal | None = rho
        self.g: Decimal | None = g
        self.h: Decimal | None = h


    def get_p(self) -> Decimal | None:
        try:
            p: Decimal = self.rho * self.g * self.h #type: ignore
            return p
        except TypeError:
            return None


    def get_rho(self) -> Decimal | None:
        try:
            rho: Decimal = self.p / (self.g * self.h) #type: ignore
            return rho
        except (ZeroDivisionError, TypeError):
            return None


    def get_g(self) -> Decimal | None:
        try:
            g: Decimal = self.p / (self.rho * self.h) #type: ignore
            return g
        except (ZeroDivisionError, TypeError):
            return None


    def get_h(self) -> Decimal | None:
        try:
            h: Decimal = self.p / (self.rho * self.g) #type: ignore
            return h
        except (ZeroDivisionError, TypeError):
            return None

#endregion
