from decimal import Decimal

from system.utils.calculators import get_quadratic_equation_roots


#region Planimetry

class CircleAreaTheorem:
    def __init__(self) -> None:
        pass


    def get_S(self, *, pi: Decimal, r: Decimal) -> Decimal:
        S: Decimal = pi * (r ** Decimal("2"))
        return S

    def get_r(self, *, S: Decimal, pi: Decimal) -> Decimal:
        r: Decimal = (S / pi).sqrt()
        return r


class CircumferenceTheorem:
    def __init__(self) -> None:
        pass


    def get_l(self, *, pi: Decimal, r: Decimal) -> Decimal:
        l: Decimal = Decimal("2") * pi * r
        return l


    def get_r(self, *, l: Decimal, pi: Decimal) -> Decimal:
        r: Decimal = l / (Decimal("2") * pi)
        return r


class ParallelogramAreaByBaseAndHeightTheorem:
    def __init__(self) -> None:
        pass


    def get_S(self, *, a: Decimal, h: Decimal) -> Decimal:
        S: Decimal = a * h
        return S


    def get_a(self, *, S: Decimal, h: Decimal) -> Decimal:
        a: Decimal = S / h
        return a


    def get_h(self, *, S: Decimal, a: Decimal) -> Decimal:
        h: Decimal = S / a
        return h
    

class TrapezoidMidlineTheorem:
    def __init__(self) -> None:
        pass


    def get_m(self, *, a: Decimal, b: Decimal) -> Decimal:
        m: Decimal = (a + b) / Decimal("2")
        return m


    def get_a(self, *, m: Decimal, b: Decimal) -> Decimal:
        a: Decimal = (Decimal("2") * m) - b
        return a


    def get_b(self, *, m: Decimal, a: Decimal) -> Decimal:
        b: Decimal = (Decimal("2") * m) - a
        return b


class TrapezoidAreaByMidlineAndHeightTheorem:
    def __init__(self) -> None:
        pass


    def get_S(self, *, m: Decimal, h: Decimal) -> Decimal:
        S: Decimal = m * h
        return S


    def get_m(self, *, S: Decimal, h: Decimal) -> Decimal:
        m: Decimal = S / h
        return m


    def get_h(self, *, S: Decimal, m: Decimal) -> Decimal:
        h: Decimal = S / m
        return h


class TriangleAreaByBaseAndHeightTheorem:
    def __init__(self) -> None:
        pass


    def get_S(self, *, a: Decimal, h: Decimal) -> Decimal:
        S: Decimal = (a * h) / Decimal("2")
        return S


    def get_a(self, *, S: Decimal, h: Decimal) -> Decimal:
        a: Decimal = (Decimal("2") * S) / h
        return a


    def get_h(self, *, S: Decimal, a: Decimal) -> Decimal:
        h: Decimal = (Decimal("2") * S) / a
        return h


class HeronTheorem:
    def __init__(self) -> None:
        pass


    def get_S(self, *, a: Decimal, b: Decimal, c: Decimal) -> Decimal:
        p: Decimal = (a + b + c) / Decimal("2")

        S: Decimal = (p * (p - a) * (p - b) * (p - c)).sqrt()
        return S


class CosineTheorem:
    def __init__(self) -> None:
        pass


    def get_a(self, *, b: Decimal, c: Decimal, cosa: Decimal) -> list[Decimal]:
        a: list[Decimal] = get_quadratic_equation_roots(a=Decimal("1"), b=(Decimal("-2") * b * cosa), c=((b ** Decimal("2")) - (c ** Decimal("2"))))
        return a


    def get_b(self, *, a: Decimal, c: Decimal, cosa: Decimal) -> list[Decimal]:
        b: list[Decimal] = get_quadratic_equation_roots(a=Decimal("1"), b=(Decimal("-2") * a * cosa), c=((a ** Decimal("2")) - (c ** Decimal("2"))))
        return b


    def get_c(self, *, a: Decimal, b: Decimal, cosa: Decimal) -> Decimal:
        c: Decimal = (a ** Decimal("2")) + (b ** Decimal("2")) - (Decimal("2") * a * b * cosa)
        return c


    def get_cosa(self, *, a: Decimal, b: Decimal, c: Decimal) -> Decimal:
        cosa: Decimal = -((c - (a ** Decimal("2")) - (b ** Decimal("2"))) / (Decimal("2") * a * b))
        return cosa


class SineTheorem:
    def __init__(self) -> None:
        pass


    def get_a(self, *, sina: Decimal, R: Decimal) -> Decimal:
        a: Decimal = Decimal("2") * R * sina
        return a


    def get_sina(self, *, a: Decimal, R: Decimal) -> Decimal:
        sina: Decimal = a / (Decimal("2") * R)
        return sina


    def get_R(self, *, a: Decimal, sina: Decimal) -> Decimal:
        R: Decimal = a / (Decimal("2") * sina)
        return R


class PythagoreanTheorem:
    def __init__(self) -> None:
        pass


    def get_a(self, *, c: Decimal, b: Decimal) -> Decimal:
        a: Decimal = (c ** Decimal("2") - b ** Decimal("2")).sqrt()
        return a


    def get_b(self, *, c: Decimal, a: Decimal) -> Decimal:
        b: Decimal = (c ** Decimal("2") - a ** Decimal("2")).sqrt()
        return b


    def get_c(self, *, a: Decimal, b: Decimal) -> Decimal:
        c: Decimal = (a ** Decimal("2") + b ** Decimal("2")).sqrt()
        return c


class TriangleAreaByInscribedCircleTheorem:
    def __init__(self) -> None:
        pass


    def get_S(self, *, p: Decimal, r: Decimal) -> Decimal:
        S: Decimal = p * r
        return S


    def get_p(self, *, S: Decimal, r: Decimal) -> Decimal:
        p: Decimal = S / r
        return p


    def get_r(self, *, S: Decimal, p: Decimal) -> Decimal:
        r: Decimal = S / p
        return r


class TriangleAreaByCircumscripedCircleTheorem:
    def __init__(self) -> None:
        pass


    def get_S(self, *, a: Decimal, b: Decimal, c: Decimal, R: Decimal) -> Decimal:
        S: Decimal = (a * b * c) / (Decimal("4") * R)
        return S


    def get_a(self, *, S: Decimal, b: Decimal, c: Decimal, R: Decimal) -> Decimal:
        a: Decimal = (S * Decimal("4") * R) / (b * c)
        return a


    def get_b(self, *, S: Decimal, R: Decimal, a: Decimal, c: Decimal) -> Decimal:
        b: Decimal = (S * Decimal("4") * R) / (a * c)
        return b


    def get_c(self, *, S: Decimal, R: Decimal, a: Decimal, b: Decimal) -> Decimal:
        c: Decimal = (S * Decimal("4") * R) / (a * b)
        return c


    def get_R(self, *, a: Decimal, b: Decimal, c: Decimal, S: Decimal) -> Decimal:
        R: Decimal = (a * b * c) / (Decimal("4") * S)
        return R


class TriangleSideProjection:
    def __init__(self) -> None:
        pass


    def get_h(self, *, c: Decimal, cossina: Decimal) -> Decimal:
        h: Decimal = c * cossina
        return h


    def get_c(self, *, h: Decimal, cossina: Decimal) -> Decimal:
        c: Decimal = h / cossina
        return c


    def get_cossina(self, *, h: Decimal, c: Decimal) -> Decimal:
        cossina: Decimal = h / c
        return cossina

#endregion
