"""Math operators."""
import math


def add(x: int, y: int) -> int:
    """Add x to y."""
    return x + y


def sub(x: int, y: int) -> int:
    """Subtract y from x."""
    return x - y


def multiply(x: int, y: int) -> int:
    """Multiply x by y."""
    return x * y


def div(x: int, y: int) -> float:
    """Divide x by y."""
    return x / y


def modulus(x: int, y: int) -> int:
    """Divide x by y and return remainder. Use an arithmetic operator."""
    return x % y


def floor_div(x: int, y: int) -> int:
    """Divide x by y and floor the value. Use an arithmetic operator."""
    return math.floor(x / y)


def exponent(x: int, y: int) -> int:
    """Calculate x raised to the power of y."""
    return x ** y


def first_greater_or_equal(x: int, y: int) -> int:
    """If x is greater or equal than y then return True. If not then return False."""
    return True if x >= y else False


def second_less_or_equal(x: int, y: int) -> int:
    """If y is less or equal than x then return True. If not then return False."""
    return True if y <= x else False


def x_is_y(x: int, y: int) -> int:
    """If x value is the same as y value then return True. If not then return False."""
    return True if x == y else False


def x_is_not_y(x: int, y: int) -> int:
    """If x value is not the same as y value then return True. If not then return False."""
    return True if x != y else False


def if_else(a: int, b: int, c: int, d: int) -> int:
    """
    Create a program that has 4 numeric parameters.

    Multiply parameters 1-2 (multiply a by b) by each other and divide parameters 3-4 (divide c by d) by each other.
    Next check and return the greater value. If both values are the same then return 0 (number zero).
    """
    val_1 = a * b
    val_2 = c / d
    return max([val_1, val_2]) if val_1 != val_2 else 0


def surface(a: int, b: int) -> int:
    """Add the missing parameters to calculate the surface of a rectangle. Calculate and return the value of the
    surface. """
    return a * b


def volume(a: int, b: int, c: int) -> int:
    """Add the missing parameters to calculate the volume of a cubiod. Calculate and return the value of the volume."""
    return a * b * c


def clock(days: int, hours: int, minutes: int, seconds: int) -> float:
    return days / 1440 + hours / 60 + minutes + seconds * 60


def calculate(operator: int, operand_1: int, operand_2: int) -> float:

    if operator == 0:
        return operand_1 + operand_2
    elif operator == 1:
        return operand_1 - operand_2
    elif operator == 2:
        return operand_1 * operand_2
    elif operator == 3:
        return operand_1 / operand_2


if __name__ == '__main__':
    print(add(1, -2))  # -1
    print(sub(5, 5))  # 0
    print(multiply(5, 5))  # 25
    print(div(15, 5))  # 3
    print(modulus(9, 3))  # 0
    print(floor_div(3, 2))  # 1
    print(exponent(5, 5))  # 3125
    print(first_greater_or_equal(1, 2))  # False
    print(second_less_or_equal(5, 5))  # True
    print(x_is_y(1, 2))  # False
    print(x_is_not_y(1, 2))  # True
    print(if_else(1, 3, 5, 99))  # 3
    print(if_else(2, 1, 10, 5))  # 0
    print(surface(1, 2)) # 2
    print(volume(5, 5, 5)) # 125
    print(clock(0, 0, 1, 15))  # 1.25
    print(clock(0, 1, 5, 0))  # 65
    print(calculate(2, 5, 4))
