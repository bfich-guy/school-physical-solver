from decimal import Decimal


#region Electricity

class OhmsSpecificLaw:
    def __init__(self, *, U: Decimal, I: Decimal, R: Decimal) -> None:
        self.U: Decimal = U
        self.I: Decimal = I
        self.R: Decimal = R

    
    def get_U(self) -> Decimal:
        U: Decimal = self.I * self.R
        return U


    def get_I(self) -> Decimal:
        I: Decimal = self.U / self.R
        return I


    def get_R(self) -> Decimal:
        R: Decimal = self.U / self.I
        return R


class OhmsFullLaw:
    def __init__(self, *, E: Decimal, U: Decimal, I: Decimal, r: Decimal) -> None:
        self.E: Decimal = E
        self.U: Decimal = U
        self.I: Decimal = I
        self.r: Decimal = r


    def get_E(self) -> Decimal:
        E: Decimal = self.U + self.I * self.r
        return E


    def get_U(self) -> Decimal:
        U: Decimal = self.E - self.I * self.r
        return U


    def get_I(self) -> Decimal:
        I: Decimal = (self.E - self.U) / self.r
        return I


    def get_r(self) -> Decimal:
        r: Decimal = (self.E - self.U) / self.I
        return r


class WattsLaw:
    def __init__(self, *, P: Decimal, U: Decimal, I: Decimal) -> None:
        self.P: Decimal = P
        self.U: Decimal = U
        self.I: Decimal = I


    def get_P(self) -> Decimal:
        P: Decimal = self.U * self.I
        return P


    def get_U(self) -> Decimal:
        U: Decimal = self.P / self.I
        return U


    def get_I(self) -> Decimal:
        I: Decimal = self.P / self.U
        return I


class JouleLenzLaw:
    def __init__(self, *, Q: Decimal, P: Decimal, t: Decimal) -> None:
        self.Q: Decimal = Q
        self.P: Decimal = P
        self.t: Decimal = t


    def get_Q(self) -> Decimal:
        Q: Decimal = self.P * self.t
        return Q


    def get_P(self) -> Decimal:
        P: Decimal = self.Q / self.t
        return P


    def get_t(self) -> Decimal:
        t: Decimal = self.Q / self.P
        return t


class CoulombsLaw:
    def __init__(self, *, F: Decimal, k: Decimal, q1: Decimal, q2: Decimal, r: Decimal) -> None:
        self.F: Decimal = F
        self.k: Decimal = k
        self.q1: Decimal = q1
        self.q2: Decimal = q2
        self.r: Decimal = r


    def get_F(self) -> Decimal:
        F: Decimal = (self.k * self.q1 * self.q2) / (self.r ** Decimal("2"))
        return F


    def get_k(self) -> Decimal:
        k: Decimal = self.F * (self.r ** Decimal("2")) / (self.q1 * self.q2)
        return k


    def get_q1(self) -> Decimal:
        q1: Decimal = self.F * (self.r ** Decimal("2")) / (self.k * self.q2)
        return q1


    def get_q2(self) -> Decimal:
        q2: Decimal = self.F * (self.r ** Decimal("2")) / (self.k * self.q1)
        return q2


    def get_r(self) -> Decimal:
        r: Decimal = ((self.k * self.q1 * self.q2) / self.F).sqrt()
        return r


class ConductorResistanceLaw:
    def __init__(self, *, R: Decimal, rho: Decimal, l: Decimal, S: Decimal) -> None:
        self.R: Decimal = R
        self.rho: Decimal = rho
        self.l: Decimal = l
        self.S: Decimal = S


    def get_R(self) -> Decimal:
        R: Decimal = (self.rho * self.l) / self.S
        return R


    def get_rho(self) -> Decimal:
        rho: Decimal = (self.R * self.S) / self.l
        return rho


    def get_l(self) -> Decimal:
        l: Decimal = (self.R * self.S) / self.rho
        return l


    def get_S(self) -> Decimal:
        S: Decimal = (self.rho * self.l) / self.R
        return S

#endregion


#region Magnetism

class AmperesLaw:
    def __init__(self, *, F: Decimal, I: Decimal, B: Decimal, L: Decimal, sina: Decimal) -> None:
        self.F: Decimal = F
        self.I: Decimal = I
        self.B: Decimal = B
        self.L: Decimal = L
        self.sina: Decimal = sina


    def get_F(self) -> Decimal:
        F: Decimal = self.I * self.B * self.L * self.sina
        return F


    def get_I(self) -> Decimal:
        I: Decimal = self.F / (self.B * self.I * self.sina)
        return I


    def get_B(self) -> Decimal:
        B: Decimal = self.F / (self.I * self.L * self.sina)
        return B


    def get_L(self) -> Decimal:
        L: Decimal = self.F / (self.I * self.B * self.sina)
        return L


    def get_sina(self) -> Decimal:
        sina: Decimal = self.F / (self.I * self.B * self.L)
        return sina


class LorentzLaw:
    def __init__(self, *, F: Decimal, q: Decimal, v: Decimal, B: Decimal, sina: Decimal) -> None:
        self.F: Decimal = F
        self.q: Decimal = q
        self.v: Decimal = v
        self.B: Decimal = B
        self.sina: Decimal = sina


    def get_F(self) -> Decimal:
        F: Decimal = self.q * self.v * self.B * self.sina
        return F


    def get_q(self) -> Decimal:
        q: Decimal = self.F / (self.v * self.B * self.sina)
        return q


    def get_v(self) -> Decimal:
        v: Decimal = self.F / (self.q * self.B * self.sina)
        return v


    def get_B(self) -> Decimal:
        B: Decimal = self.F / (self.q * self.v * self.sina)
        return B


    def get_sina(self) -> Decimal:
        sina: Decimal = self.F / (self.q * self.v * self.B)
        return sina


class FaradaysLaw:
    def __init__(self, *, E: Decimal, Dphi: Decimal, Dt: Decimal) -> None:
        self.E: Decimal = E
        self.Dphi: Decimal = Dphi
        self.Dt: Decimal = Dt


    def get_E(self) -> Decimal:
        E: Decimal = -self.Dphi / self.Dt
        return E


    def get_Dphi(self) -> Decimal:
        Dphi: Decimal = -self.E * self.Dt
        return Dphi


    def get_Dt(self) -> Decimal:
        Dt: Decimal = -self.Dphi / self.E
        return Dt


class MagneticFluxLaw:
    def __init__(self, *, phi: Decimal, B: Decimal, S: Decimal, cosa: Decimal) -> None:
        self.phi: Decimal = phi
        self.B: Decimal = B
        self.S: Decimal = S
        self.cosa: Decimal = cosa


    def get_phi(self) -> Decimal:
        phi: Decimal = self.B * self.S * self.cosa
        return phi


    def get_B(self) -> Decimal:
        B: Decimal = self.phi / (self.S * self.cosa)
        return B


    def get_S(self) -> Decimal:
        S: Decimal = self.phi / (self.B * self.cosa)
        return S


    def get_cosa(self) -> Decimal:
        cosa: Decimal = self.phi / (self.B * self.S)
        return cosa

#endregion
