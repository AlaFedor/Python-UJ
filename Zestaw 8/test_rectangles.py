import pytest
from rectangles import Rectangle
from points import Point


def test_from_points():
    p1 = Point(0, 0)
    p2 = Point(5, 10)
    r = Rectangle.from_points((p1, p2))
    assert r == Rectangle(0, 0, 5, 10)


def test_numbers():
    r = Rectangle(1, 2, 3, 4)
    assert r.left == 1
    assert r.right == 3
    assert r.bottom == 2
    assert r.top == 4
    assert r.width == 2
    assert r.height == 2


def test_points():
    r = Rectangle(1, 2, 3, 4)
    assert r.bottomleft == Point(1, 2)
    assert r.topright == Point(3, 4)
    assert r.topleft == Point(1, 4)
    assert r.bottomright == Point(3, 2)


def test_center():
    r = Rectangle(0, 0, 2, 2)
    assert r.center == Point(1, 1)

def test_area():
    assert Rectangle(0, 0, 1, 2).area() == 2


def test_move():
    r = Rectangle(1, 1, 2, 2)
    r2 = r.move(3, 4)
    assert r2 == Rectangle(4, 5, 5, 6)


def test_intersection():
    r1 = Rectangle(0, 0, 4, 4)
    r2 = Rectangle(2, 2, 6, 6)
    r3 = r1.intersection(r2)
    assert r3 == Rectangle(2, 2, 4, 4)

    with pytest.raises(ValueError):
        Rectangle(0, 0, 1, 1).intersection(Rectangle(2, 2, 3, 3))


def test_cover():
    r1 = Rectangle(0, 0, 2, 2)
    r2 = Rectangle(1, 1, 3, 3)
    assert r1.cover(r2) == Rectangle(0, 0, 3, 3)


def test_make4():
    r = Rectangle(0, 0, 2, 2)
    r1, r2, r3, r4 = r.make4()

    assert r1 == Rectangle(0, 0, 1, 1)
    assert r2 == Rectangle(1, 0, 2, 1)
    assert r3 == Rectangle(0, 1, 1, 2)
    assert r4 == Rectangle(1, 1, 2, 2)
