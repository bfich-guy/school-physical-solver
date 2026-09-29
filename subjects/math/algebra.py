from decimal import Decimal

from system.utils.calculators import get_quadratic_equation_roots, decimal_logarithm


#region Equations

class LinearEquationSolving:
    def __init__(self, *, a: Decimal, b: Decimal) -> None:
        self.a: Decimal = a
        self.b: Decimal = b


    def get_x(self) -> Decimal:
        x: Decimal = -self.a / self.b
        return x


class QuadraticEquationSolving:
    def __init__(self, *, a: Decimal, b: Decimal, c: Decimal) -> None:
        self.a: Decimal = a
        self.b: Decimal = b
        self.c: Decimal = c


    def get_x(self) -> list[Decimal]:
        x: list[Decimal] = get_quadratic_equation_roots(a=self.a, b=self.b, c=self.c)
        return x


class DerivativeEquationSolving:
    def __init__(self, *, d: Decimal, Dy: Decimal, Dx: Decimal) -> None:
        self.d: Decimal = d
        self.Dy: Decimal = Dy
        self.Dx: Decimal = Dx


    def get_d(self) -> Decimal:
        d: Decimal = self.Dy / self.Dx
        return d


    def get_Dy(self) -> Decimal:
        d: Decimal = self.d * self.Dx
        return d


    def get_Dx(self) -> Decimal:
        d: Decimal = self.Dy / self.d
        return d


class TangentEquationSolving:
    def __init__(self, *, y: Decimal, dfx: Decimal, Dx: Decimal, fx: Decimal) -> None:
        self.y: Decimal = y
        self.dfx: Decimal = dfx
        self.Dx: Decimal = Dx
        self.fx: Decimal = fx


    def get_y(self) -> Decimal:
        y: Decimal = self.dfx * self.Dx + self.fx
        return y


    def get_dfx(self) -> Decimal:
        dfx: Decimal = (self.y - self.fx) / self.Dx
        return dfx


    def get_Dx(self) -> Decimal:
        Dx: Decimal = (self.y - self.fx) / self.dfx
        return Dx


    def get_fx(self) -> Decimal:
        fx: Decimal = self.y - (self.dfx * self.Dx)
        return fx

#endregion


#region Functions

class LinearGraphFunction:
    def __init__(self, *, x: Decimal, y: Decimal, a: Decimal, b: Decimal) -> None:
        self.x: Decimal = x
        self.y: Decimal = y
        self.a: Decimal = a
        self.b: Decimal = b


    def get_y(self) -> Decimal:
        y: Decimal = self.a * self.x + self.b
        return y


    def get_a(self) -> Decimal:
        a: Decimal = (self.y - self.b) / self.x
        return a


    def get_b(self) -> Decimal:
        b: Decimal = self.y - (self.a * self.x)
        return b


class QuadraticGraphFunction:
    def __init__(self, *, x: Decimal, y: Decimal, a: Decimal, b: Decimal, c: Decimal) -> None:
        self.x: Decimal = x
        self.y: Decimal = y
        self.a: Decimal = a
        self.b: Decimal = b
        self.c: Decimal = c


    def get_y(self) -> Decimal:
        y: Decimal = self.a * (self.x ** Decimal("2")) + (self.b * self.x) + self.c
        return y


    def get_a(self) -> Decimal:
        a: Decimal = (self.y - (self.b * self.x) - self.c) / (self.x ** Decimal("2"))
        return a


    def get_b(self) -> Decimal:
        b: Decimal = (self.y - self.a * (self.x ** Decimal("2")) - self.c) / self.x
        return b


    def get_c(self) -> Decimal:
        c: Decimal = self.y - self.a * (self.x ** Decimal("2")) - (self.b * self.x)
        return c


class CircleGraphFunction:
    def __init__(self, *, r: Decimal, Dx: Decimal, Dy: Decimal) -> None:
        self.r: Decimal = r
        self.Dx: Decimal = Dx
        self.Dy: Decimal = Dy


    def get_r(self) -> Decimal:
        r: Decimal = (self.Dx ** Decimal("2") + self.Dy ** Decimal("2")).sqrt()
        return r


    def get_Dx(self) -> Decimal:
        Dy: Decimal = (self.r ** Decimal("2") - self.Dy ** Decimal("2")).sqrt()
        return Dy


    def get_Dy(self) -> Decimal:
        Dx: Decimal = (self.r ** Decimal("2") - self.Dx ** Decimal("2")).sqrt()
        return Dx

#endregion


#region Progressions

class ArithmeticProgressionSumTheorem:
    def __init__(self, *, S: Decimal, a1: Decimal, an: Decimal, n: Decimal) -> None:
        self.S: Decimal = S
        self.a1: Decimal = a1
        self.an: Decimal = an
        self.n: Decimal = n


    def get_S(self) -> Decimal:
        S: Decimal = ((self.a1 + self.an) * self.n) / Decimal("2")
        return S


    def get_a1(self) -> Decimal:
        a1: Decimal = (Decimal("2") * self.S) / (self.a1 + self.an)
        return a1


    def get_an(self) -> Decimal:
        an: Decimal = ((Decimal("2") * self.S) - (self.an * self.n)) / self.n
        return an


    def get_n(self) -> Decimal:
        n: Decimal = ((Decimal("2") * self.S) - (self.a1 * self.n)) / self.n
        return n


class GeometricProgressionSumTheorem:
    def __init__(self, *, S: Decimal, b1: Decimal, bn: Decimal, q: Decimal) -> None:
        self.S: Decimal = S
        self.b1: Decimal = b1
        self.bn: Decimal = bn
        self.q: Decimal = q

    
    def get_S(self) -> Decimal:
        S: Decimal = ((self.bn * self.q) - self.b1) / (self.q - Decimal("1"))
        return S


    def get_b1(self) -> Decimal:
        b1: Decimal = self.S * (self.q - Decimal("1")) - (self.bn * self.q)
        return b1


    def get_bn(self) -> Decimal:
        bn: Decimal = (self.S * (self.q - Decimal("1")) + self.bn) / self.q
        return bn


    def get_q(self) -> Decimal:
        q: Decimal = (self.S - self.b1) / (self.S - self.bn)
        return q


class ArithmeticProgressionTermTheorem:
    def __init__(self, *, an: Decimal, a1: Decimal, d: Decimal, n: Decimal) -> None:
        self.an: Decimal = an
        self.a1: Decimal = a1
        self.d: Decimal = d
        self.n: Decimal = n


    def get_an(self) -> Decimal:
        an: Decimal = self.a1 + self.d * (self.n - Decimal("1"))
        return an


    def get_a1(self) -> Decimal:
        a1: Decimal = self.an - self.d * (self.n - Decimal("1"))
        return a1


    def get_d(self) -> Decimal:
        d: Decimal = (self.an - self.a1) / (self.n - Decimal("1"))
        return d


    def get_n(self) -> Decimal:
        n: Decimal = ((self.an - self.a1) / self.d) + Decimal("1")
        return n


class GeometricProgressionTermTheorem:
    def __init__(self, *, bn: Decimal, b1: Decimal, q: Decimal, n: Decimal) -> None:
        self.bn: Decimal = bn
        self.b1: Decimal = b1
        self.q: Decimal = q
        self.n: Decimal = n


    def get_bn(self) -> Decimal:
        q_is_one: bool = self.q == Decimal("1")

        if q_is_one:
            bn: Decimal = self.b1 * self.q
            return bn
        else:
            bn: Decimal = self.b1 * (self.q ** (self.n - Decimal("1")))
            return bn


    def get_b1(self) -> Decimal:
        b1: Decimal = self.bn / (self.q ** (self.n - Decimal("1")))
        return b1


    def get_q(self) -> Decimal:
        ratio: Decimal = self.bn / self.b1
        steps: Decimal = self.n - Decimal("1")

        ratio_is_less_than_zero: bool = ratio < Decimal("0")
        steps_amount_is_odd: bool = steps % Decimal("2") != Decimal("0")

        if ratio_is_less_than_zero and steps_amount_is_odd:
            q: Decimal = -((-ratio) ** (Decimal("1") / steps))
            return q
        else:
            q: Decimal = ratio ** (Decimal("1") / steps)
            return q


    def get_n(self) -> Decimal:
        n: Decimal = decimal_logarithm((self.bn / self.b1), self.q) + Decimal("1")
        return n

#endregion


#region Vectors

class VectorCorrdinatesTheorem:
    def __init__(self, *, a: list[Decimal], B: list[Decimal], A: list[Decimal]) -> None:
        self.a: list[Decimal] = a
        self.B: list[Decimal] = B
        self.A: list[Decimal] = A


    def get_a(self) -> list[Decimal]:
        a: list[Decimal] = [x2 - x1 for x2, x1 in zip(self.B, self.A)]
        return a


    def get_B(self) -> list[Decimal]:
        B: list[Decimal] = [x2 + x1 for x2, x1 in zip(self.a, self.A)]
        return B


    def get_A(self) -> list[Decimal]:
        A: list[Decimal] = [x2 - x1 for x2, x1 in zip(self.B, self.a)]
        return A


class VectorMagnitudeTheorem:
    def __init__(self, *, a: list[Decimal]) -> None:
        self.a: list[Decimal] = a


    def get_la(self) -> Decimal:
        la = Decimal("0")

        for Dx in self.a:
            la += Dx ** Decimal("2")

        la = la.sqrt()
        return la


class VectorDotProductTheorem:
    def __init__(self, *, a: list[Decimal], b: list[Decimal]) -> None:
        self.a: list[Decimal] = a
        self.b: list[Decimal] = b


    def get_ab(self) -> Decimal:
        ab = Decimal("0")

        for x1i, x1j in zip(self.a, self.b):
            ab += x1i * x1j

        return ab


class AngleBetweenVectorsCosinusTheorem:
    def __init__(self, *, cosa: Decimal, ab: Decimal, la: Decimal, lb: Decimal) -> None:
        self.cosa: Decimal = cosa
        self.ab: Decimal = ab
        self.la: Decimal = la
        self.lb: Decimal = lb


    def get_cosa(self) -> Decimal:
        cosa: Decimal = self.ab / (self.la * self.lb)
        return cosa


    def get_ab(self) -> Decimal:
        ab: Decimal = self.cosa * self.la * self.lb
        return ab


    def get_la(self) -> Decimal:
        la: Decimal = self.ab / (self.lb * self.cosa)
        return la


    def get_lb(self) -> Decimal:
        lb: Decimal = self.ab / (self.la * self.cosa)
        return lb

#endregion
