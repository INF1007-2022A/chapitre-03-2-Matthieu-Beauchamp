#!/usr/bin/env python


def dissipated_power(voltage: float, resistance: float) -> float:
    """P = V**2 / R"""
    return voltage**2 / resistance


def dot(v1, v2) -> float:
    if len(v1) != len(v2):
        raise ValueError("Inconsistent vector sizes")

    scalar = 0.0
    for i in range(len(v1)):
        scalar += v1[i] * v2[i]

    return scalar


def isEqual(value, reference, epsilon=1e-6) -> bool:
    return reference-epsilon <= value and value <= reference+epsilon


def orthogonal(v1, v2) -> bool:
    return isEqual(dot(v1, v2), 0.0)


def average(values) -> float:
    # TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
    avg = 0
    nElements = 0
    for v in values:
        if (v >= 0):
            nElements += 1
            avg += v

    return avg / nElements


def bills(value: int) -> tuple:
    # TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
    register = [0, 0, 0, 0]

    for i, bill in enumerate([20, 10, 5, 1]):
        nBills = value // bill
        value -= bill * nBills
        register[i] = nBills

    return (register[0], register[1], register[2], register[3])


def format_base(value: int, base: int, digit_letters: str) -> str:
    # Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
    # `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
    
    result = "-" if value < 0 else ""

    abs_value = abs(value)

    exp = 0
    while abs_value > base * (base ** exp) - 1:
        exp += 1

    while abs_value != 0:
        weigth = base ** exp
        nTimes = abs_value // weigth

        if (nTimes >= base):
            raise ArithmeticError("Internal failure")

        result += digit_letters[nTimes]
        abs_value -= nTimes * weigth
        exp -= 1

    return result


if __name__ == "__main__":
    print(dissipated_power(69, 420))
    print(orthogonal((1, 1), (-1, 1)))
    print(average([1, 4, -2, 10]))
    print(bills(137))
    print(format_base(-42, 16, "0123456789ABCDEF"))
