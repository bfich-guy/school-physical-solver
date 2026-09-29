from decimal import Decimal

from system.utils.calculators import decimal_sum, decimal_product, get_quadratic_equation_roots


#region Planimetry

class CircleAreaTheorem:
    def __init__(self, *, S: Decimal, pi: Decimal, r: Decimal) -> None:
        self.S: Decimal = S
        self.pi: Decimal = pi
        self.r: Decimal = r


    def get_S(self) -> Decimal:
        S: Decimal = self.pi * (self.r ** Decimal("2"))
        return S

    def get_r(self) -> Decimal:
        r: Decimal = (self.S / self.pi).sqrt()
        return r


class CircumferenceTheorem:
    def __init__(self, *, l: Decimal, pi: Decimal, r: Decimal) -> None:
        self.l: Decimal = l
        self.pi: Decimal = pi
        self.r: Decimal = r


    def get_l(self) -> Decimal:
        l: Decimal = Decimal("2") * self.pi * self.r
        return l


    def get_r(self) -> Decimal:
        r: Decimal = self.l / (Decimal("2") * self.pi)
        return r


class ParallelogramAreaByBaseAndHeightTheorem:
    def __init__(self, *, S: Decimal, a: Decimal, h: Decimal) -> None:
        self.S: Decimal = S
        self.a: Decimal = a
        self.h: Decimal = h


    def get_S(self) -> Decimal:
        S: Decimal = self.a * self.h
        return S


    def get_a(self) -> Decimal:
        a: Decimal = self.S / self.h
        return a


    def get_h(self) -> Decimal:
        h: Decimal = self.S / self.a
        return h
    

class TrapezoidMidlineTheorem:
    def __init__(self, *, m: Decimal, a: Decimal, b: Decimal) -> None:
        self.m: Decimal = m
        self.a: Decimal = a
        self.b: Decimal = b


    def get_m(self) -> Decimal:
        m: Decimal = (self.a + self.b) / Decimal("2")
        return m


    def get_a(self) -> Decimal:
        a: Decimal = (Decimal("2") * self.m) - self.b
        return a


    def get_b(self) -> Decimal:
        b: Decimal = (Decimal("2") * self.m) - self.a
        return b


class TrapezoidAreaByMidlineAndHeightTheorem:
    def __init__(self, *, S: Decimal, m: Decimal, h: Decimal) -> None:
        self.S: Decimal = S
        self.m: Decimal = m
        self.h: Decimal = h


    def get_S(self) -> Decimal:
        S: Decimal = self.m * self.h
        return S


    def get_m(self) -> Decimal:
        m: Decimal = self.S / self.h
        return m


    def get_h(self) -> Decimal:
        h: Decimal = self.S / self.m
        return h


class TriangleAreaByBaseAndHeightTheorem:
    def __init__(self, *, S: Decimal, a: Decimal, h: Decimal) -> None:
        self.S: Decimal = S
        self.a: Decimal = a
        self.h: Decimal = h


    def get_S(self) -> Decimal:
        S: Decimal = (self.a * self.h) / Decimal("2")
        return S


    def get_a(self) -> Decimal:
        a: Decimal = (Decimal("2") * self.S) / self.h
        return a


    def get_h(self) -> Decimal:
        h: Decimal = (Decimal("2") * self.S) / self.a
        return h


class HeronTheorem:
    def __init__(self, *, a: Decimal, b: Decimal, c: Decimal) -> None:
        self.a: Decimal = a
        self.b: Decimal = b
        self.c: Decimal = c


    def get_S(self) -> Decimal:
        p: Decimal = decimal_sum([self.a, self.b, self.c]) / Decimal("2")
        S: Decimal = decimal_product([p, p - self.a, p - self.b, p - self.c]).sqrt()
        return S


class CosineTheorem:
    def __init__(self, *, a: Decimal, b: Decimal, c: Decimal, cosa: Decimal) -> None:
        self.a: Decimal = a
        self.b: Decimal = b
        self.c: Decimal = c
        self.cosa: Decimal = cosa


    def get_a(self) -> list[Decimal]:
        a: list[Decimal] = get_quadratic_equation_roots(a=Decimal("1"), b=(Decimal("-2") * self.b * self.cosa), c=((self.b ** Decimal("2")) - (self.c ** Decimal("2"))))
        return a


    def get_b(self) -> list[Decimal]:
        b: list[Decimal] = get_quadratic_equation_roots(a=Decimal("1"), b=(Decimal("-2") * self.a * self.cosa), c=((self.a ** Decimal("2")) - (self.c ** Decimal("2"))))
        return b


    def get_c(self) -> Decimal:
        c: Decimal = (self.a ** Decimal("2")) + (self.b ** Decimal("2")) - (Decimal("2") * self.a * self.b * self.cosa) #type: ignore
        return c


    def get_cosa(self) -> Decimal:
        cosa: Decimal = -((self.c - (self.a ** Decimal("2")) - (self.b ** Decimal("2"))) / (Decimal("2") * self.a * self.b))
        return cosa


class SineTheorem:
    def __init__(self, *, a: Decimal, sina: Decimal, R: Decimal) -> None:
        self.a: Decimal = a
        self.sina: Decimal = sina
        self.R: Decimal = R


    def get_a(self) -> Decimal:
        a: Decimal = Decimal("2") * self.R * self.sina
        return a


    def get_sina(self) -> Decimal:
        sina: Decimal = self.a / (Decimal("2") * self.R)
        return sina


    def get_R(self) -> Decimal:
        R: Decimal = self.a / (Decimal("2") * self.sina)
        return R


class PythagoreanTheorem:
    def __init__(self, *, a: Decimal, b: Decimal, c: Decimal) -> None:
        self.a: Decimal = a
        self.b: Decimal = b
        self.c: Decimal = c


    def get_a(self) -> Decimal:
        a: Decimal = ((self.c ** Decimal("2")) - (self.b ** Decimal("2"))).sqrt()
        return a


    def get_b(self) -> Decimal:
        b: Decimal = ((self.c ** Decimal("2")) - (self.a ** Decimal("2"))).sqrt()
        return b


    def get_c(self) -> Decimal:
        c: Decimal = ((self.a ** Decimal("2")) + (self.b ** Decimal("2"))).sqrt()
        return c


class TriangleAreaByInscribedCircleTheorem:
    def __init__(self, *, S: Decimal, p: Decimal, r: Decimal) -> None:
        self.S: Decimal = S
        self.p: Decimal = p
        self.r: Decimal = r


    def get_S(self) -> Decimal:
        S: Decimal = self.p * self.r
        return S


    def get_p(self) -> Decimal:
        p: Decimal = self.S / self.r
        return p


    def get_r(self) -> Decimal:
        r: Decimal = self.S / self.p
        return r


class TriangleAreaByCircumscripedCircleTheorem:
    def __init__(self, *, S: Decimal, a: Decimal, b: Decimal, c: Decimal, R: Decimal) -> None:
        self.S: Decimal = S
        self.a: Decimal = a
        self.b: Decimal = b
        self.c: Decimal = c
        self.R: Decimal = R


    def get_S(self) -> Decimal:
        S: Decimal = (self.a * self.b * self.c) / (Decimal("4") * self.R)
        return S


    def get_a(self) -> Decimal:
        a: Decimal = (self.S * Decimal("4") * self.R) / (self.b * self.c)
        return a


    def get_b(self) -> Decimal:
        b: Decimal = (self.S * Decimal("4") * self.R) / (self.a * self.c)
        return b


    def get_c(self) -> Decimal:
        c: Decimal = (self.S * Decimal("4") * self.R) / (self.a * self.b)
        return c


    def get_R(self) -> Decimal:
        R: Decimal = (self.a * self.b * self.c) / (Decimal("4") * self.S)
        return R

#endregion


#region Stereometry

class PlaneEquation:
    def __init__(self, *, x: Decimal, y: Decimal, z: Decimal, A: Decimal, B: Decimal, C: Decimal, D: Decimal) -> None:
        self.x: Decimal = x
        self.y: Decimal = y
        self.z: Decimal = z
        self.A: Decimal = A
        self.B: Decimal = B
        self.C: Decimal = C
        self.D: Decimal = D


    def get_x(self) -> Decimal:
        x: Decimal = (Decimal("0") - self.D - (self.C * self.z) - (self.B * self.y)) / self.A
        return x


    def get_y(self) -> Decimal:
        y: Decimal = (Decimal("0") - self.D - (self.C * self.z) - (self.A * self.x)) / self.B
        return y


    def get_z(self) -> Decimal:
        z: Decimal = (Decimal("0") - self.D - (self.A * self.x) - (self.B * self.y)) / self.C
        return z


    def get_A(self) -> Decimal:
        A: Decimal = (Decimal("0") - self.D - (self.C * self.z) - (self.B * self.y)) / self.x
        return A


    def get_B(self) -> Decimal:
        B: Decimal = (Decimal("0") - self.D - (self.C * self.z) - (self.A * self.x)) / self.y
        return B


    def get_C(self) -> Decimal:
        C: Decimal = (Decimal("0") - self.D - (self.A * self.x) - (self.B * self.y)) / self.z
        return C


    def get_D(self) -> Decimal:
        D: Decimal = Decimal("0") - self.D - (self.A * self.x) - (self.B * self.y) - (self.C * self.z)
        return D


class PrismSurfaceBySidesAndBasesAreasTheorem:
    def __init__(self, *, S: Decimal, Ss: Decimal, Sb: Decimal) -> None:
        self.S: Decimal = S
        self.Ss: Decimal = Ss
        self.Sb: Decimal = Sb


    def get_S(self) -> Decimal:
        S: Decimal = self.Ss + Decimal("2") * self.Sb
        return S


    def get_Ss(self) -> Decimal:
        Ss: Decimal = self.S - Decimal("2") * self.Sb
        return Ss


    def get_Sb(self) -> Decimal:
        Sb: Decimal = (self.S - self.Sb) / Decimal("2")
        return Sb


class PrismVolumeByBaseAndHeightTheorem:
    def __init__(self, *, V: Decimal, Sb: Decimal, h: Decimal) -> None:
        self.V: Decimal = V
        self.Sb: Decimal = Sb
        self.h: Decimal = h


    def get_V(self) -> Decimal:
        V: Decimal = self.Sb * self.h
        return V


    def get_Sb(self) -> Decimal:
        Sb: Decimal = self.V / self.h
        return Sb


    def get_h(self) -> Decimal:
        h: Decimal = self.V / self.Sb
        return h


class ConeVolumeByBaseAndHeightTheorem:
    def __init__(self, *, V: Decimal, Sb: Decimal, h: Decimal) -> None:
        self.V: Decimal = V
        self.Sb: Decimal = Sb
        self.h: Decimal = h


    def get_V(self) -> Decimal:
        V: Decimal = (self.Sb * self.h) / Decimal("3")
        return V


    def get_Sb(self) -> Decimal:
        Sb: Decimal = (Decimal("3") * self.V) / self.h
        return Sb


    def get_h(self) -> Decimal:
        h: Decimal = (Decimal("3") * self.V) / self.Sb
        return h

#endregion
