from decimal import Decimal

from system.utils.calculators import get_quadratic_equation_roots, decimal_logarithm


#region Equations

class LinearEquationSolving:
    def __init__(self) -> None:
        pass


    def get_x(self, *, a: Decimal, b: Decimal) -> Decimal:
        x: Decimal = -a / b
        return x


class QuadraticEquationSolving:
    def __init__(self) -> None:
        pass

    def get_x(self, *, a: Decimal, b: Decimal, c: Decimal) -> list[Decimal]:
        x: list[Decimal] = get_quadratic_equation_roots(a=a, b=b, c=c)
        return x


class DerivativeEquationSolving:
    def __init__(self) -> None:
        pass


    def get_d(self, *, Dy: Decimal, Dx: Decimal) -> Decimal:
        d: Decimal = Dy / Dx
        return d


    def get_Dy(self, *, d: Decimal, Dx: Decimal) -> Decimal:
        Dy: Decimal = d * Dx
        return Dy


    def get_Dx(self, *, Dy: Decimal, d: Decimal) -> Decimal:
        Dx: Decimal = Dy / d
        return Dx


class TangentEquationSolving:
    def __init__(self) -> None:
        pass


    def get_y(self, *, dfx: Decimal, Dx: Decimal, fx: Decimal) -> Decimal:
        y: Decimal = dfx * Dx + fx
        return y


    def get_dfx(self, *, y: Decimal, fx: Decimal, Dx: Decimal) -> Decimal:
        dfx: Decimal = (y - fx) / Dx
        return dfx


    def get_Dx(self, *, y: Decimal, fx: Decimal, dfx: Decimal) -> Decimal:
        Dx: Decimal = (y - fx) / dfx
        return Dx


    def get_fx(self, *, y: Decimal, dfx: Decimal, Dx: Decimal) -> Decimal:
        fx: Decimal = y - (dfx * Dx)
        return fx

#endregion


#region Functions

class LinearGraphFunction:
    def __init__(self) -> None:
        pass


    def get_y(self, *, a: Decimal, x: Decimal, b: Decimal) -> Decimal:
        y: Decimal = a * x + b
        return y


    def get_a(self, *, y: Decimal, b: Decimal, x: Decimal) -> Decimal:
        a: Decimal = (y - b) / x
        return a


    def get_b(self, *, y: Decimal, a: Decimal, x: Decimal) -> Decimal:
        b: Decimal = y - (a * x)
        return b


class QuadraticGraphFunction:
    def __init__(self) -> None:
        pass


    def get_y(self, *, x: Decimal, a: Decimal, b: Decimal, c: Decimal) -> Decimal:
        y: Decimal = a * x ** Decimal("2") + (b * x) + c
        return y


    def get_a(self, *, x: Decimal, y: Decimal, b: Decimal, c: Decimal) -> Decimal:
        a: Decimal = (y - b * x - c) / (x ** Decimal("2"))
        return a


    def get_b(self, *, x: Decimal, y: Decimal, a: Decimal, c: Decimal) -> Decimal:
        b: Decimal = (y - a * x ** Decimal("2") - c) / x
        return b


    def get_c(self, *, x: Decimal, y: Decimal, a: Decimal, b: Decimal) -> Decimal:
        c: Decimal = y - a * x ** Decimal("2") - (b * x)
        return c


class CircleGraphFunction:
    def __init__(self) -> None:
        pass


    def get_r(self, *, Dx: Decimal, Dy: Decimal) -> Decimal:
        r: Decimal = (Dx ** Decimal("2") + Dy ** Decimal("2")).sqrt()
        return r


    def get_Dx(self, *, r: Decimal, Dy: Decimal) -> Decimal:
        Dx: Decimal = (r ** Decimal("2") - Dy ** Decimal("2")).sqrt()
        return Dx


    def get_Dy(self, *, r: Decimal, Dx: Decimal) -> Decimal:
        Dy: Decimal = (r ** Decimal("2") - Dx ** Decimal("2")).sqrt()
        return Dy

#endregion


#region Progressions

class ArithmeticProgressionSumTheorem:
    def __init__(self) -> None:
        pass


    def get_S(self, *, a1: Decimal, an: Decimal, n: Decimal) -> Decimal:
        S: Decimal = ((a1 + an) * n) / Decimal("2")
        return S


    def get_a1(self, *, S: Decimal, n: Decimal, an: Decimal) -> Decimal:
        a1: Decimal = (Decimal("2") * S) / n - an
        return a1


    def get_an(self, *, S: Decimal, n: Decimal, a1: Decimal) -> Decimal:
        an: Decimal = (Decimal("2") * S) / n - a1
        return an


    def get_n(self, *, S: Decimal, a1: Decimal, an: Decimal) -> Decimal:
        n: Decimal = (Decimal("2") * S) / (a1 + an)
        return n


class GeometricProgressionSumTheorem:
    def __init__(self) -> None:
        pass

    
    def get_S(self, *, bn: Decimal, q: Decimal, b1: Decimal) -> Decimal:
        S: Decimal = ((bn * q) - b1) / (q - Decimal("1"))
        return S


    def get_b1(self, *, S: Decimal, q: Decimal, bn: Decimal) -> Decimal:
        b1: Decimal = S * (q - Decimal("1")) - (bn * q)
        return b1


    def get_bn(self, *, S: Decimal, q: Decimal, b1: Decimal) -> Decimal:
        bn: Decimal = (S * (q - Decimal("1")) + b1) / q
        return bn


    def get_q(self, *, S: Decimal, b1: Decimal, bn: Decimal) -> Decimal:
        q: Decimal = (S - b1) / (S - bn)
        return q


class ArithmeticProgressionTermTheorem:
    def __init__(self) -> None:
        pass


    def get_an(self, *, a1: Decimal, d: Decimal, n: Decimal) -> Decimal:
        an: Decimal = a1 + d * (n - Decimal("1"))
        return an


    def get_a1(self, *, an: Decimal, d: Decimal, n: Decimal) -> Decimal:
        a1: Decimal = an - d * (n - Decimal("1"))
        return a1


    def get_d(self, *, an: Decimal, a1: Decimal, n: Decimal) -> Decimal:
        d: Decimal = (an - a1) / (n - Decimal("1"))
        return d


    def get_n(self, *, an: Decimal, a1: Decimal, d: Decimal) -> Decimal:
        n: Decimal = ((an - a1) / d) + Decimal("1")
        return n


class GeometricProgressionTermTheorem:
    def __init__(self) -> None:
        pass


    def get_bn(self, *, b1: Decimal, q: Decimal, n: Decimal) -> Decimal:
        q_is_one: bool = q == Decimal("1")

        if q_is_one:
            bn: Decimal = b1 * q
            return bn
        else:
            bn: Decimal = b1 * (q ** (n - Decimal("1")))
            return bn


    def get_b1(self, *, bn: Decimal, q: Decimal, n: Decimal) -> Decimal:
        b1: Decimal = bn / (q ** (n - Decimal("1")))
        return b1


    def get_q(self, *, bn: Decimal, b1: Decimal, n: Decimal) -> Decimal:
        ratio: Decimal = bn / b1
        steps: Decimal = n - Decimal("1")

        ratio_is_less_than_zero: bool = ratio < Decimal("0")
        steps_amount_is_odd: bool = steps % Decimal("2") != Decimal("0")

        if ratio_is_less_than_zero and steps_amount_is_odd:
            q: Decimal = -((-ratio) ** (Decimal("1") / steps))
            return q
        else:
            q: Decimal = ratio ** (Decimal("1") / steps)
            return q


    def get_n(self, *, bn: Decimal, b1: Decimal, q: Decimal) -> Decimal:
        n: Decimal = decimal_logarithm((bn / b1), q) + Decimal("1")
        return n

#endregion


#region Vectors

class VectorCorrdinatesTheorem:
    def __init__(self) -> None:
        pass


    def get_a(self, *, B: list[Decimal], A: list[Decimal]) -> list[Decimal]:
        a: list[Decimal] = [x2 - x1 for x2, x1 in zip(B, A)]
        return a


    def get_B(self, *, a: list[Decimal], A: list[Decimal]) -> list[Decimal]:
        B: list[Decimal] = [x2 + x1 for x2, x1 in zip(a, A)]
        return B


    def get_A(self, *, a: list[Decimal], B: list[Decimal]) -> list[Decimal]:
        A: list[Decimal] = [x2 - x1 for x2, x1 in zip(B, a)]
        return A


class VectorMagnitudeTheorem:
    def __init__(self) -> None:
        pass


    def get_la(self, *, a: list[Decimal]) -> Decimal:
        la = Decimal("0")

        for Dx in a:
            la += Dx ** Decimal("2")

        la = la.sqrt()
        return la


class VectorDotProductTheorem:
    def __init__(self) -> None:
        pass


    def get_ab(self, *, a: list[Decimal], b: list[Decimal]) -> Decimal:
        ab = Decimal("0")

        for x1i, x1j in zip(a, b):
            ab += x1i * x1j

        return ab


class AngleBetweenVectorsCosinusTheorem:
    def __init__(self) -> None:
        pass


    def get_cosa(self, *, ab: Decimal, la: Decimal, lb: Decimal) -> Decimal:
        cosa: Decimal = ab / (la * lb)
        return cosa


    def get_ab(self, *, cosa: Decimal, la: Decimal, lb: Decimal) -> Decimal:
        ab: Decimal = cosa * la * lb
        return ab


    def get_la(self, *, ab: Decimal, lb: Decimal, cosa: Decimal) -> Decimal:
        la: Decimal = ab / (lb * cosa)
        return la


    def get_lb(self, *, ab: Decimal, la: Decimal, cosa: Decimal) -> Decimal:
        lb: Decimal = ab / (la * cosa)
        return lb

#endregion
