from decimal import Decimal, InvalidOperation


#region Electricity

class OhmsSpecificLaw:
    def __init__(self, *, U: Decimal | None = None, I: Decimal | None = None, R: Decimal | None = None) -> None:
        self.U: Decimal | None = U
        self.I: Decimal | None = I
        self.R: Decimal | None = R

    
    def get_U(self) -> Decimal | None:
        try:
            U: Decimal = self.I * self.R #type: ignore
            return U
        except (ZeroDivisionError, TypeError):
            return None


    def get_I(self) -> Decimal | None:
        try:
            I: Decimal = self.U / self.R #type: ignore
            return I
        except (ZeroDivisionError, TypeError):
            return None


    def get_R(self) -> Decimal | None:
        try:
            R: Decimal = self.U / self.I #type: ignore
            return R
        except (ZeroDivisionError, TypeError):
            return None


class OhmsFullLaw:
    def __init__(self, *, E: Decimal | None = None, U: Decimal | None = None, I: Decimal | None = None, r: Decimal | None = None) -> None:
        self.E: Decimal | None = E
        self.U: Decimal | None = U
        self.I: Decimal | None = I
        self.r: Decimal | None = r


    def get_E(self) -> Decimal | None:
        try:
            E: Decimal = self.U + self.I * self.r #type: ignore
            return E
        except (ZeroDivisionError, TypeError):
            return None


    def get_U(self) -> Decimal | None:
        try:
            U: Decimal = self.E - self.I * self.r #type: ignore
            return U
        except (ZeroDivisionError, TypeError):
            return None


    def get_I(self) -> Decimal | None:
        try:
            I: Decimal = (self.E - self.U) / self.r #type: ignore
            return I
        except (ZeroDivisionError, TypeError):
            return None


    def get_r(self) -> Decimal | None:
        try:
            r: Decimal = (self.E - self.U) / self.I #type: ignore
            return r
        except (ZeroDivisionError, TypeError):
            return None


class WattsLaw:
    def __init__(self, *, P: Decimal | None = None, U: Decimal | None = None, I: Decimal | None = None) -> None:
        self.P: Decimal | None = P
        self.U: Decimal | None = U
        self.I: Decimal | None = I


    def get_P(self) -> Decimal | None:
        try:
            P: Decimal = self.U * self.I #type: ignore
            return P
        except (ZeroDivisionError, TypeError):
            return None


    def get_U(self) -> Decimal | None:
        try:
            U: Decimal = self.P / self.I #type: ignore
            return U
        except (ZeroDivisionError, TypeError):
            return None


    def get_I(self) -> Decimal | None:
        try:
            I: Decimal = self.P / self.U #type: ignore
            return I
        except (ZeroDivisionError, TypeError):
            return None


class JouleLenzLaw:
    def __init__(self, *, Q: Decimal | None = None, P: Decimal | None = None, t: Decimal | None = None) -> None:
        self.Q: Decimal | None = Q
        self.P: Decimal | None = P
        self.t: Decimal | None = t


    def get_Q(self) -> Decimal | None:
        try:
            Q: Decimal = self.P * self.t #type: ignore
            return Q
        except (ZeroDivisionError, TypeError):
            return None


    def get_P(self) -> Decimal | None:
        try:
            P: Decimal = self.Q / self.t #type: ignore
            return P
        except (ZeroDivisionError, TypeError):
            return None


    def get_t(self) -> Decimal | None:
        try:
            t: Decimal = self.Q / self.P #type: ignore
            return t
        except (ZeroDivisionError, TypeError):
            return None


class CoulombsLaw:
    def __init__(self, *, F: Decimal | None = None, k: Decimal | None = None, q1: Decimal | None = None, q2: Decimal | None = None, r: Decimal | None = None) -> None:
        self.F: Decimal | None = F
        self.k: Decimal | None = k
        self.q1: Decimal | None = q1
        self.q2: Decimal | None = q2
        self.r: Decimal | None = r


    def get_F(self) -> Decimal | None:
        try:
            F: Decimal = (self.k * self.q1 * self.q2) / (self.r ** Decimal("2")) #type: ignore
            return F
        except (ZeroDivisionError, TypeError):
            return None


    def get_k(self) -> Decimal | None:
        try:
            k: Decimal = self.F * (self.r ** Decimal("2")) / (self.q1 * self.q2) #type: ignore
            return k
        except (ZeroDivisionError, TypeError):
            return None


    def get_q1(self) -> Decimal | None:
        try:
            q1: Decimal = self.F * (self.r ** Decimal("2")) / (self.k * self.q2) #type: ignore
            return q1
        except (ZeroDivisionError, TypeError):
            return None


    def get_q2(self) -> Decimal | None:
        try:
            q2: Decimal = self.F * (self.r ** Decimal("2")) / (self.k * self.q1) #type: ignore
            return q2
        except (ZeroDivisionError, TypeError):
            return None


    def get_r(self) -> Decimal | None:
        try:
            r: Decimal = ((self.k * self.q1 * self.q2) / self.F).sqrt() #type: ignore
            return r
        except (ZeroDivisionError, InvalidOperation, TypeError):
            return None


class ConductorResistanceLaw:
    def __init__(self, *, R: Decimal | None = None, rho: Decimal | None = None, l: Decimal | None = None, S: Decimal | None = None) -> None:
        self.R: Decimal | None = R
        self.rho: Decimal | None = rho
        self.l: Decimal | None = l
        self.S: Decimal | None = S


    def get_R(self) -> Decimal | None:
        try:
            R: Decimal = (self.rho * self.l) / self.S #type: ignore
            return R
        except (ZeroDivisionError, TypeError):
            return None


    def get_rho(self) -> Decimal | None:
        try:
            rho: Decimal = (self.R * self.S) / self.l #type: ignore
            return rho
        except (ZeroDivisionError, TypeError):
            return None


    def get_l(self) -> Decimal | None:
        try:
            l: Decimal = (self.R * self.S) / self.rho #type: ignore
            return l
        except (ZeroDivisionError, TypeError):
            return None


    def get_S(self) -> Decimal | None:
        try:
            S: Decimal = (self.rho * self.l) / self.R #type: ignore
            return S
        except (ZeroDivisionError, TypeError):
            return None

#endregion


#region Magnetism

class AmperesLaw:
    def __init__(self, *, F: Decimal | None = None, I: Decimal | None = None, B: Decimal | None = None, L: Decimal | None = None, sina: Decimal | None = None) -> None:
        self.F: Decimal | None = F
        self.I: Decimal | None = I
        self.B: Decimal | None = B
        self.L: Decimal | None = L
        self.sina: Decimal | None = sina


    def get_F(self) -> Decimal | None:
        try:
            F: Decimal = self.I * self.B * self.L * self.sina #type: ignore
            return F
        except (ZeroDivisionError, TypeError):
            return None


    def get_I(self) -> Decimal | None:
        try:
            I: Decimal = self.F / (self.B * self.I * self.sina) #type: ignore
            return I
        except (ZeroDivisionError, TypeError):
            return None


    def get_B(self) -> Decimal | None:
        try:
            B: Decimal = self.F / (self.I * self.L * self.sina) #type: ignore
            return B
        except (ZeroDivisionError, TypeError):
            return None


    def get_L(self) -> Decimal | None:
        try:
            L: Decimal = self.F / (self.I * self.B * self.sina) #type: ignore
            return L
        except (ZeroDivisionError, TypeError):
            return None


    def get_sina(self) -> Decimal | None:
        try:
            sina: Decimal = self.F / (self.I * self.B * self.L) #type: ignore
            return sina
        except (ZeroDivisionError, TypeError):
            return None


class LorentzLaw:
    def __init__(self, *, F: Decimal | None = None, q: Decimal | None = None, v: Decimal | None = None, B: Decimal | None = None, sina: Decimal | None = None) -> None:
        self.F: Decimal | None = F
        self.q: Decimal | None = q
        self.v: Decimal | None = v
        self.B: Decimal | None = B
        self.sina: Decimal | None = sina


    def get_F(self) -> Decimal | None:
        try:
            F: Decimal = self.q * self.v * self.B * self.sina #type: ignore
            return F
        except (ZeroDivisionError, TypeError):
            return None


    def get_q(self) -> Decimal | None:
        try:
            q: Decimal = self.F / (self.v * self.B * self.sina) #type: ignore
            return q
        except (ZeroDivisionError, TypeError):
            return None


    def get_v(self) -> Decimal | None:
        try:
            v: Decimal = self.F / (self.q * self.B * self.sina) #type: ignore
            return v
        except (ZeroDivisionError, TypeError):
            return None


    def get_B(self) -> Decimal | None:
        try:
            B: Decimal = self.F / (self.q * self.v * self.sina) #type: ignore
            return B
        except (ZeroDivisionError, TypeError):
            return None


    def get_sina(self) -> Decimal | None:
        try:
            sina: Decimal = self.F / (self.q * self.v * self.B) #type: ignore
            return sina
        except (ZeroDivisionError, TypeError):
            return None


class FaradaysLaw:
    def __init__(self, *, E: Decimal | None = None, Dphi: Decimal | None = None, Dt: Decimal | None = None) -> None:
        self.E: Decimal | None = E
        self.Dphi: Decimal | None = Dphi
        self.Dt: Decimal | None = Dt


    def get_E(self) -> Decimal | None:
        try:
            E: Decimal = -self.Dphi / self.Dt #type: ignore
            return E
        except (ZeroDivisionError, TypeError):
            return None


    def get_Dphi(self) -> Decimal | None:
        try:
            Dphi: Decimal = -self.E * self.Dt #type: ignore
            return Dphi
        except (ZeroDivisionError, TypeError):
            return None


    def get_Dt(self) -> Decimal | None:
        try:
            Dt: Decimal = -self.Dphi / self.E #type: ignore
            return Dt
        except (ZeroDivisionError, TypeError):
            return None


class MagneticFluxLaw:
    def __init__(self, *, phi: Decimal | None = None, B: Decimal | None = None, S: Decimal | None = None, cosa: Decimal | None = None) -> None:
        self.phi: Decimal | None = phi
        self.B: Decimal | None = B
        self.S: Decimal | None = S
        self.cosa: Decimal | None = cosa


    def get_phi(self) -> Decimal | None:
        try:
            phi: Decimal = self.B * self.S * self.cosa #type: ignore
            return phi
        except (ZeroDivisionError, TypeError):
            return None


    def get_B(self) -> Decimal | None:
        try:
            B: Decimal = self.phi / (self.S * self.cosa) #type: ignore
            return B
        except (ZeroDivisionError, TypeError):
            return None


    def get_S(self) -> Decimal | None:
        try:
            S: Decimal = self.phi / (self.B * self.cosa) #type: ignore
            return S
        except (ZeroDivisionError, TypeError):
            return None


    def get_cosa(self) -> Decimal | None:
        try:
            cosa: Decimal = self.phi / (self.B * self.S) #type: ignore
            return cosa
        except (ZeroDivisionError, TypeError):
            return None

#endregion
