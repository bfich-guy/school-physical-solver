from decimal import Decimal


#region Classic thermodynamics

class SensibleHeatLaw:
    def __init__(self, *, Q: Decimal, c: Decimal, m: Decimal, Dt: Decimal) -> None:
        self.Q: Decimal = Q
        self.c: Decimal = c
        self.m: Decimal = m
        self.Dt: Decimal = Dt


    def get_Q(self) -> Decimal:
        Q: Decimal = self.c * self.m * self.Dt
        return Q


    def get_c(self) -> Decimal:
        c: Decimal = self.Q / (self.m * self.Dt)
        return c


    def get_m(self) -> Decimal:
        m: Decimal = self.Q / (self.c * self.Dt)
        return m


    def get_Dt(self) -> Decimal:
        Dt: Decimal = self.Q / (self.c * self.m)
        return Dt


class CombustionHeatLaw:
    def __init__(self, *, Q: Decimal, q: Decimal, m: Decimal) -> None:
        self.Q: Decimal = Q
        self.q: Decimal = q
        self.m: Decimal = m


    def get_Q(self) -> Decimal:
        Q: Decimal = self.q * self.m
        return Q


    def get_q(self) -> Decimal:
        q: Decimal = self.Q / self.m
        return q


    def get_m(self) -> Decimal:
        m: Decimal = self.Q / self.q
        return m


class FusionHeatLaw:
    def __init__(self, *, Q: Decimal, lmb: Decimal, m: Decimal) -> None:
        self.Q: Decimal = Q
        self.lmb: Decimal = lmb
        self.m: Decimal = m


    def get_Q(self) -> Decimal:
        Q: Decimal = self.lmb * self.m
        return Q


    def get_lmb(self) -> Decimal:
        lmb: Decimal = self.Q / self.m
        return lmb


    def get_m(self) -> Decimal:
        m: Decimal = self.Q / self.lmb
        return m


class VaporizationHeatLaw:
    def __init__(self, *, Q: Decimal, L: Decimal, m: Decimal) -> None:
        self.Q: Decimal = Q
        self.L: Decimal = L
        self.m: Decimal = m


    def get_Q(self) -> Decimal:
        Q: Decimal = self.L * self.m
        return Q


    def get_L(self) -> Decimal:
        L: Decimal = self.Q / self.m
        return L


    def get_m(self) -> Decimal:
        m: Decimal = self.Q / self.L
        return m

#endregion


#region Molecular kinetic theory

class MendeleevClapeyronLaw:
    def __init__(self, *, p: Decimal, V: Decimal, v: Decimal, R: Decimal, T: Decimal) -> None:
        self.p: Decimal = p
        self.V: Decimal = V
        self.v: Decimal = v
        self.R: Decimal = R
        self.T: Decimal = T


    def get_p(self) -> Decimal:
        p: Decimal = (self.v * self.R * self.T) / self.V
        return p


    def get_V(self) -> Decimal:
        V: Decimal = (self.v * self.R * self.T) / self.p
        return V


    def get_v(self) -> Decimal:
        v: Decimal = (self.p * self.V) / (self.R * self.T)
        return v


    def get_T(self) -> Decimal:
        T: Decimal = (self.p * self.V) / (self.R * self.v)
        return T


class MolarMassLaw:
    def __init__(self, *, v: Decimal, m: Decimal, M: Decimal) -> None:
        self.v: Decimal = v
        self.m: Decimal = m
        self.M: Decimal = M


    def get_v(self) -> Decimal:
        v: Decimal = self.m / self.M
        return v


    def get_m(self) -> Decimal:
        m: Decimal = self.v * self.M
        return m


    def get_M(self) -> Decimal:
        M: Decimal = self.m / self.v
        return M

#endregion
