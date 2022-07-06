import math

class Triangle:

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self, base, height):
        self.base = base
        self.height = height
        return 0.5 * base * height

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3


class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def get_area(self):
        return self.length * self.breadth

    def get_perimeter(self):
        return 2 * (self.length + self.breadth)


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius**2)

    def get_perimeter(self):
        return 2 * math.pi * self.radius


class Trapezium:

    def __init__(self, a, b, height):
        self.a = a
        self.b = b
        self.height = height


    def get_area(self):
        return 0.5 * (self.a + self.b) * self.height

    def get_perimeter(self, slant_height):
        self.slant_height = slant_height
        return self.a + self.b + self.height + slant_height


circle = Trapezium(3,5,12)
print(circle.get_area())