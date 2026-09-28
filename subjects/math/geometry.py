from decimal import Decimal

from utils import decimal_sum, decimal_product, get_quadratic_equation_roots


#region Circles

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

#endregion


#region Parallelograms

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

#endregion


#region Trapezoids

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

#endregion


#region Triangles

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
