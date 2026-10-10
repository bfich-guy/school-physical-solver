from decimal import Decimal


#region Classic thermodynamics

class SensibleHeatLaw:
    def __init__(self) -> None:
        pass


    def get_Q(self, *, c: Decimal, m: Decimal, Dt: Decimal) -> Decimal:
        Q: Decimal = c * m * Dt
        return Q


    def get_c(self, *, Q: Decimal, m: Decimal, Dt: Decimal) -> Decimal:
        c: Decimal = Q / (m * Dt)
        return c


    def get_m(self, *, Q: Decimal, c: Decimal, Dt: Decimal) -> Decimal:
        m: Decimal = Q / (c * Dt)
        return m


    def get_Dt(self, *, Q: Decimal, c: Decimal, m: Decimal) -> Decimal:
        Dt: Decimal = Q / (c * m)
        return Dt


class CombustionHeatLaw:
    def __init__(self) -> None:
        pass


    def get_Q(self, *, q: Decimal, m: Decimal) -> Decimal:
        Q: Decimal = q * m
        return Q


    def get_q(self, *, Q: Decimal, m: Decimal) -> Decimal:
        q: Decimal = Q / m
        return q


    def get_m(self, *, Q: Decimal, q: Decimal) -> Decimal:
        m: Decimal = Q / q
        return m


class FusionHeatLaw:
    def __init__(self) -> None:
        pass


    def get_Q(self, *, lmb: Decimal, m: Decimal) -> Decimal:
        Q: Decimal = lmb * m
        return Q


    def get_lmb(self, *, Q: Decimal, m: Decimal) -> Decimal:
        lmb: Decimal = Q / m
        return lmb


    def get_m(self, *, Q: Decimal, lmb: Decimal) -> Decimal:
        m: Decimal = Q / lmb
        return m


class VaporizationHeatLaw:
    def __init__(self) -> None:
        pass


    def get_Q(self, *, L: Decimal, m: Decimal) -> Decimal:
        Q: Decimal = L * m
        return Q


    def get_L(self, *, Q: Decimal, m: Decimal) -> Decimal:
        L: Decimal = Q / m
        return L


    def get_m(self, *, Q: Decimal, L: Decimal) -> Decimal:
        m: Decimal = Q / L
        return m

#endregion


#region Molecular kinetic theory

class MendeleevClapeyronLaw:
    def __init__(self) -> None:
        pass


    def get_p(self, *, v: Decimal, R: Decimal, T: Decimal, V: Decimal) -> Decimal:
        p: Decimal = (v * R * T) / V
        return p


    def get_V(self, *, v: Decimal, R: Decimal, T: Decimal, p: Decimal) -> Decimal:
        V: Decimal = (v * R * T) / p
        return V


    def get_v(self, *, p: Decimal, V: Decimal, R: Decimal, T: Decimal) -> Decimal:
        v: Decimal = (p * V) / (R * T)
        return v


    def get_T(self, *, p: Decimal, V: Decimal, R: Decimal, v: Decimal) -> Decimal:
        T: Decimal = (p * V) / (R * v)
        return T


class MolarMassLaw:
    def __init__(self) -> None:
        pass


    def get_v(self, *, m: Decimal, M: Decimal) -> Decimal:
        v: Decimal = m / M
        return v


    def get_m(self, *, v: Decimal, M: Decimal) -> Decimal:
        m: Decimal = v * M
        return m


    def get_M(self, *, m: Decimal, v: Decimal) -> Decimal:
        M: Decimal = m / v
        return M

#endregion
