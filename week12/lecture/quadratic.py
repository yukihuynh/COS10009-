import math


def solve(a, b, c):
    # return the two roots of ax^2 + bx + c = 0
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        raise ValueError("No real roots")

    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return x1, x2
