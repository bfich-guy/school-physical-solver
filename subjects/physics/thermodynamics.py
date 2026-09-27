from decimal import Decimal


#region Classic thermodynamics

class SensibleHeatLaw:
    def __init__(self, *, Q: Decimal | None = None, c: Decimal | None = None, m: Decimal | None = None, Dt: Decimal | None = None) -> None:
        self.Q: Decimal | None = Q
        self.c: Decimal | None = c
        self.m: Decimal | None = m
        self.Dt: Decimal | None = Dt


    def get_Q(self) -> Decimal | None:
        try:
            Q: Decimal = self.c * self.m * self.Dt #type: ignore
            return Q
        except TypeError:
            return None


    def get_c(self) -> Decimal | None:
        try:
            c: Decimal = self.Q / (self.m * self.Dt) #type: ignore
            return c
        except (ZeroDivisionError, TypeError):
            return None


    def get_m(self) -> Decimal | None:
        try:
            m: Decimal = self.Q / (self.c * self.Dt) #type: ignore
            return m
        except (ZeroDivisionError, TypeError):
            return None


    def get_Dt(self) -> Decimal | None:
        try:
            Dt: Decimal = self.Q / (self.c * self.m) #type: ignore
            return Dt
        except (ZeroDivisionError, TypeError):
            return None


class CombustionHeatLaw:
    def __init__(self, *, Q: Decimal | None = None, q: Decimal | None = None, m: Decimal | None = None) -> None:
        self.Q: Decimal | None = Q
        self.q: Decimal | None = q
        self.m: Decimal | None = m


    def get_Q(self) -> Decimal | None:
        try:
            Q: Decimal = self.q * self.m #type: ignore
            return Q
        except TypeError:
            return None


    def get_q(self) -> Decimal | None:
        try:
            q: Decimal = self.Q / self.m #type: ignore
            return q
        except (ZeroDivisionError, TypeError):
            return None


    def get_m(self) -> Decimal | None:
        try:
            m: Decimal = self.Q / self.q #type: ignore
            return m
        except (ZeroDivisionError, TypeError):
            return None


class FusionHeatLaw:
    def __init__(self, *, Q: Decimal | None = None, lmb: Decimal | None = None, m: Decimal | None = None) -> None:
        self.Q: Decimal | None = Q
        self.lmb: Decimal | None = lmb
        self.m: Decimal | None = m


    def get_Q(self) -> Decimal | None:
        try:
            Q: Decimal = self.lmb * self.m #type: ignore
            return Q
        except TypeError:
            return None


    def get_lmb(self) -> Decimal | None:
        try:
            lmb: Decimal = self.Q / self.m #type: ignore
            return lmb
        except (ZeroDivisionError, TypeError):
            return None


    def get_m(self) -> Decimal | None:
        try:
            m: Decimal = self.Q / self.lmb #type: ignore
            return m
        except (ZeroDivisionError, TypeError):
            return None


class VaporizationHeatLaw:
    def __init__(self, *, Q: Decimal | None = None, L: Decimal | None = None, m: Decimal | None = None) -> None:
        self.Q: Decimal | None = Q
        self.L: Decimal | None = L
        self.m: Decimal | None = m


    def get_Q(self) -> Decimal | None:
        try:
            Q: Decimal = self.L * self.m #type: ignore
            return Q
        except TypeError:
            return None


    def get_L(self) -> Decimal | None:
        try:
            L: Decimal = self.Q / self.m #type: ignore
            return L
        except (ZeroDivisionError, TypeError):
            return None


    def get_m(self) -> Decimal | None:
        try:
            m: Decimal = self.Q / self.L #type: ignore
            return m
        except (ZeroDivisionError, TypeError):
            return None

#endregion


#region Molecular kinetic theory

class MendeleevClapeyronLaw:
    def __init__(self, *, p: Decimal | None = None, V: Decimal | None = None, v: Decimal | None = None, R: Decimal | None = None, T: Decimal | None = None) -> None:
        self.p: Decimal | None = p
        self.V: Decimal | None = V
        self.v: Decimal | None = v
        self.R: Decimal | None = R
        self.T: Decimal | None = T


    def get_p(self) -> Decimal | None:
        try:
            p: Decimal = (self.v * self.R * self.T) / self.V #type: ignore
            return p
        except (ZeroDivisionError, TypeError):
            return None


    def get_V(self) -> Decimal | None:
        try:
            V: Decimal = (self.v * self.R * self.T) / self.p #type: ignore
            return V
        except (ZeroDivisionError, TypeError):
            return None


    def get_v(self) -> Decimal | None:
        try:
            v: Decimal = (self.p * self.V) / (self.R * self.T) #type: ignore
            return v
        except (ZeroDivisionError, TypeError):
            return None


    def get_T(self) -> Decimal | None:
        try:
            T: Decimal = (self.p * self.V) / (self.R * self.v) #type: ignore
            return T
        except (ZeroDivisionError, TypeError):
            return None


class MolarMassLaw:
    def __init__(self, *, v: Decimal | None = None, m: Decimal | None = None, M: Decimal | None = None) -> None:
        self.v: Decimal | None = v
        self.m: Decimal | None = m
        self.M: Decimal | None = M


    def get_v(self) -> Decimal | None:
        try:
            v: Decimal = self.m / self.M #type: ignore
            return v
        except (ZeroDivisionError, TypeError):
            return None


    def get_m(self) -> Decimal | None:
        try:
            m: Decimal = self.v * self.M #type: ignore
            return m
        except TypeError:
            return None


    def get_M(self) -> Decimal | None:
        try:
            M: Decimal = self.m / self.v #type: ignore
            return M
        except (ZeroDivisionError, TypeError):
            return None

#endregion
