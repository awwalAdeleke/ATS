import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self) -> None:
        pass

    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass


class Two_D(Shape):
    def __init__(self) -> None:
        super().__init__()

    def area(self):
        return super().area()

    def perimeter(self):                # This over-rode the abstract method.
        return super().perimeter()

two = Two_D()
print(two.perimeter())


class Three_D(Shape):
    def __init__(self) -> None:
        super().__init__()

    def area(self):
        return super().area()

    def perimeter(self):
        return super().perimeter()


class Circle(Two_D):
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Two_D):
    def __init__(self, length: int = 0) -> None:
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2

    def perimeter(self):
        return self.length * 4


class Triangle(Two_D):
    def __init__(self, side_1, side_2, side_3) -> None:
        super().__init__()
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def area(self):
        key = (self.perimeter())/2
        diff_1 = key - self.side_1
        diff_2 = key - self.side_2
        diff_3 = key - self.side_3

        return (key * diff_1 * diff_2 * diff_3) ** 0.5

    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3


class Sphere(Three_D):
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius

    def area(self):
        return 4 * math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Cube(Three_D):
    def __init__(self, length) -> None:
        super().__init__()
        self.length = length

    def area(self):
        return 6 * (self.length ** 2)

    def perimeter(self):
        return 12 * self.length


class R_Tetrahedron(Three_D):
    """
    It represents a regular tetrahedron

    Args:
        Three_D (Shape): Six equal edges in length
    """

    def __init__(self, length) -> None:
        super().__init__()
        self.length = length

    def area(self):
        resp = int(input("Which area are you measuring?\n1 for Lateral Surface Area\n2 for Total Surface Area\n"))
        if resp == 1:
            return self.lateral_area()
        elif resp == 2:
            return self.total_area()
        else:
            return "You have entered an incorrect response!"

    def lateral_area(self):
        return 3 * (3 ** 0.5)/4 * (self.length ** 2)

    def total_area(self):
        return (3 ** 0.5) * (self.length ** 2)
    
    def perimeter(self):
        return 6 * self.length




# cir = Circle(5)
# print(cir.area())
# print(cir.perimeter())

# squ = Square(5)
# print(squ.area())
# print(squ.perimeter())

# tri = Triangle(6,6,6)
# print(tri.area())
# print(tri.perimeter())

# cube = Cube(3)
# print(cube.area())
# print(cube.perimeter())

# sphere = Sphere(5)
# print(sphere.area())
# print(sphere.perimeter())

# tetra = R_Tetrahedron(3)
# print(tetra.area())
# print(tetra.lateral_area())
# print(tetra.total_area())
# print(tetra.perimeter())


# NVC
# Code Architecture in Python
# Import: Relative and Absolute

# Django is NVT more than NVC