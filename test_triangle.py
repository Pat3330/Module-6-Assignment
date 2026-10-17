import math
from triangle import classify_triangle


def test_invalid_negative_side():
    assert classify_triangle(-1, 2, 3) == "Invalid"
    assert classify_triangle(1, 0, 3) == "Invalid"


def test_invalid_triangle_inequality():
    assert classify_triangle(2, 3, 6) == "Invalid"


def test_invalid_degenerate_boundary():
    assert classify_triangle(4, 5, 9) == "Invalid"


def test_equilateral():
    assert classify_triangle(5, 5, 5) == "Equilateral"


def test_isosceles():
    assert classify_triangle(5, 5, 3) == "Isosceles"
    assert classify_triangle(3, 5, 5) == "Isosceles"
    assert classify_triangle(5, 3, 5) == "Isosceles"


def test_scalene():
    assert classify_triangle(4, 5, 6) == "Scalene"


def test_right_scalene_integer():
    assert classify_triangle(3, 4, 5) == "Right Scalene"


def test_right_isosceles_non_integer():
    hypotenuse = 5 * math.sqrt(2)
    result = classify_triangle(5, 5, hypotenuse)
    assert result == "Right Isosceles"
