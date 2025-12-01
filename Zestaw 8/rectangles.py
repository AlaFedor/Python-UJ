from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Upewnij się że: x1 < x2 oraz y1 < y2.")

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    @classmethod
    def from_points(clas, points):
        if len(points) != 2:
            raise ValueError("Podaj dwa punkty.")
        p1, p2 = points
        return clas(p1.x, p1.y, p2.x, p2.y)

    def __str__(self):  # "[(x1, y1), (x2, y2)]"
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self): # "Rectangle(x1, y1, x2, y2)"
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other): # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    @property
    def top(self):
        return self.pt2.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def right(self):
        return self.pt2.x

    @property
    def width(self):
        return self.pt2.x - self.pt1.x

    @property
    def height(self):
        return self.pt2.y - self.pt1.y

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)

    @property
    def center(self): # zwraca środek prostokąta
        return Point(
            (self.left + self.right) / 2,
            (self.bottom + self.top) / 2
        )

    def area(self): # pole powierzchni
        return self.width * self.height

    def move(self, x, y): # przesunięcie o (x, y)
        return Rectangle(
            self.left + x, self.bottom + y,
            self.right + x, self.top + y
        )

    def intersection(self, other): # część wspólna prostokątów
        x1 = max(self.left, other.left)
        y1 = max(self.bottom, other.bottom)
        x2 = min(self.right, other.right)
        y2 = min(self.top, other.top)

        if x1 >= x2 or y1 >= y2:
            raise ValueError("Prostokąty nie mają części wspólnej.")

        return Rectangle(x1, y1, x2, y2)

    def cover(self, other): # prostąkąt nakrywający oba
        x1 = min(self.left, other.left)
        y1 = min(self.bottom, other.bottom)
        x2 = max(self.right, other.right)
        y2 = max(self.top, other.top)
        return Rectangle(x1, y1, x2, y2)

    def make4(self): # zwraca krotkę czterech mniejszych
        cx = self.center.x
        cy = self.center.y

        return (
            Rectangle(self.left, self.bottom, cx, cy),
            Rectangle(cx, self.bottom, self.right, cy),
            Rectangle(self.left, cy, cx, self.top),
            Rectangle(cx, cy, self.right, self.top)
        ) # zwraca krotkę czterech mniejszych
# A-------B   po podziale  A---+---B
# |       |                |   |   |
# |       |                +---+---+
# |       |                |   |   |
# D-------C                D---+---C
