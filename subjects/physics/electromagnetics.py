from decimal import Decimal


#region Electricity

class OhmsSpecificLaw:
    def __init__(self) -> None:
        pass

    
    def get_U(self, *, I: Decimal, R: Decimal) -> Decimal:
        U: Decimal = I * R
        return U


    def get_I(self, *, U: Decimal, R: Decimal) -> Decimal:
        I: Decimal = U / R
        return I


    def get_R(self, *, U: Decimal, I: Decimal) -> Decimal:
        R: Decimal = U / I
        return R


class OhmsFullLaw:
    def __init__(self) -> None:
        pass


    def get_E(self, *, U: Decimal, I: Decimal, r: Decimal) -> Decimal:
        E: Decimal = U + I * r
        return E


    def get_U(self, *, E: Decimal, I: Decimal, r: Decimal) -> Decimal:
        U: Decimal = E - I * r
        return U


    def get_I(self, *, E: Decimal, U: Decimal, r: Decimal) -> Decimal:
        I: Decimal = (E - U) / r
        return I


    def get_r(self, *, E: Decimal, U: Decimal, I: Decimal) -> Decimal:
        r: Decimal = (E - U) / I
        return r


class WattsLaw:
    def __init__(self) -> None:
        pass


    def get_P(self, *, U: Decimal, I: Decimal) -> Decimal:
        P: Decimal = U * I
        return P


    def get_U(self, *, P: Decimal, I: Decimal) -> Decimal:
        U: Decimal = P / I
        return U


    def get_I(self, *, P: Decimal, U: Decimal) -> Decimal:
        I: Decimal = P / U
        return I


class JouleLenzLaw:
    def __init__(self) -> None:
        pass


    def get_Q(self, *, P: Decimal, t: Decimal) -> Decimal:
        Q: Decimal = P * t
        return Q


    def get_P(self, *, Q: Decimal, t: Decimal) -> Decimal:
        P: Decimal = Q / t
        return P


    def get_t(self, *, Q: Decimal, P: Decimal) -> Decimal:
        t: Decimal = Q / P
        return t


class CoulombsLaw:
    def __init__(self) -> None:
        pass


    def get_F(self, *, k: Decimal, q1: Decimal, q2: Decimal, r: Decimal) -> Decimal:
        F: Decimal = (k * q1 * q2) / (r ** Decimal("2"))
        return F


    def get_k(self, *, F: Decimal, r: Decimal, q1: Decimal, q2: Decimal) -> Decimal:
        k: Decimal = F * (r ** Decimal("2")) / (q1 * q2)
        return k


    def get_q1(self, *, F: Decimal, r: Decimal, k: Decimal, q2: Decimal) -> Decimal:
        q1: Decimal = F * (r ** Decimal("2")) / (k * q2)
        return q1


    def get_q2(self, *, F: Decimal, r: Decimal, k: Decimal, q1: Decimal) -> Decimal:
        q2: Decimal = F * (r ** Decimal("2")) / (k * q1)
        return q2


    def get_r(self, *, k: Decimal, q1: Decimal, q2: Decimal, F: Decimal) -> Decimal:
        r: Decimal = ((k * q1 * q2) / F).sqrt()
        return r


class ConductorResistanceLaw:
    def __init__(self) -> None:
        pass


    def get_R(self, *, rho: Decimal, l: Decimal, S: Decimal) -> Decimal:
        R: Decimal = (rho * l) / S
        return R


    def get_rho(self, *, R: Decimal, S: Decimal, l: Decimal) -> Decimal:
        rho: Decimal = (R * S) / l
        return rho


    def get_l(self, *, R: Decimal, S: Decimal, rho: Decimal) -> Decimal:
        l: Decimal = (R * S) / rho
        return l


    def get_S(self, *, rho: Decimal, l: Decimal, R: Decimal) -> Decimal:
        S: Decimal = (rho * l) / R
        return S

#endregion


#region Magnetism

class AmperesLaw:
    def __init__(self) -> None:
        pass


    def get_F(self, *, I: Decimal, B: Decimal, L: Decimal, sina: Decimal) -> Decimal:
        F: Decimal = I * B * L * sina
        return F


    def get_I(self, *, F: Decimal, B: Decimal, L: Decimal, sina: Decimal) -> Decimal:
        I: Decimal = F / (B * L * sina)
        return I


    def get_B(self, *, F: Decimal, I: Decimal, L: Decimal, sina: Decimal) -> Decimal:
        B: Decimal = F / (I * L * sina)
        return B


    def get_L(self, *, F: Decimal, I: Decimal, B: Decimal, sina: Decimal) -> Decimal:
        L: Decimal = F / (I * B * sina)
        return L


    def get_sina(self, *, F: Decimal, I: Decimal, B: Decimal, L: Decimal) -> Decimal:
        sina: Decimal = F / (I * B * L)
        return sina


class LorentzLaw:
    def __init__(self) -> None:
        pass


    def get_F(self, *, q: Decimal, v: Decimal, B: Decimal, sina: Decimal) -> Decimal:
        F: Decimal = q * v * B * sina
        return F


    def get_q(self, *, F: Decimal, v: Decimal, B: Decimal, sina: Decimal) -> Decimal:
        q: Decimal = F / (v * B * sina)
        return q


    def get_v(self, *, F: Decimal, q: Decimal, B: Decimal, sina: Decimal) -> Decimal:
        v: Decimal = F / (q * B * sina)
        return v


    def get_B(self, *, F: Decimal, q: Decimal, v: Decimal, sina: Decimal) -> Decimal:
        B: Decimal = F / (q * v * sina)
        return B


    def get_sina(self, *, F: Decimal, q: Decimal, v: Decimal, B: Decimal) -> Decimal:
        sina: Decimal = F / (q * v * B)
        return sina


class FaradaysLaw:
    def __init__(self) -> None:
        pass


    def get_E(self, *, Dphi: Decimal, Dt: Decimal) -> Decimal:
        E: Decimal = -Dphi / Dt
        return E


    def get_Dphi(self, *, E: Decimal, Dt: Decimal) -> Decimal:
        Dphi: Decimal = -E * Dt
        return Dphi


    def get_Dt(self, *, Dphi: Decimal, E: Decimal) -> Decimal:
        Dt: Decimal = -Dphi / E
        return Dt


class MagneticFluxLaw:
    def __init__(self) -> None:
        pass


    def get_phi(self, *, B: Decimal, S: Decimal, cosa: Decimal) -> Decimal:
        phi: Decimal = B * S * cosa
        return phi


    def get_B(self, *, phi: Decimal, S: Decimal, cosa: Decimal) -> Decimal:
        B: Decimal = phi / (S * cosa)
        return B


    def get_S(self, *, phi: Decimal, B: Decimal, cosa: Decimal) -> Decimal:
        S: Decimal = phi / (B * cosa)
        return S


    def get_cosa(self, *, phi: Decimal, B: Decimal, S: Decimal) -> Decimal:
        cosa: Decimal = phi / (B * S)
        return cosa

#endregion
