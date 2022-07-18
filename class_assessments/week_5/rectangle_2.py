class Rectangle:
    def __init__(self, upper_left: tuple, lower_right: tuple) -> None:

        """
        The first value for the upper_left tuple is the x1 value.
        The second value for the upper_left tuple is the y1 value.
        The first value for the lower right tuple is the x2 value.
        The second value for the lower right tuple is the y2 value.
        """
        self.upper_left = upper_left
        self.lower_right = lower_right

        assert all(upper_left) >= 0.0 and len(upper_left) == 2, "The two coordinates have to be in the first quadrant, i.e positive!"
        assert all(lower_right) >= 0.0 and len(lower_right) == 2, "The two coordinates have to be in the first quadrant, i.e positive!"

    def __str__(self):
        return f"{__class__.__name__}{self.upper_left}{self.lower_right}"

    @property
    def length(self):
        part_1 = self.lower_right[0] - self.upper_left[0]
        part_2 = self.upper_left[1] - self.lower_right[1]
        return max([part_1,part_2])


    @property
    def width(self):
        part_1 = self.lower_right[0] - self.upper_left[0]
        part_2 = self.upper_left[1] - self.lower_right[1]
        return min([part_1,part_2])

    def perimeter(self):
        return (2 * self.width) + (2 * self.length)

    def area(self):
        return self.width * self.length

    def isSquare(self):
        if self.length == self.width:
            return "This rectangle is a square, funny!"
        return "This rectangle is not a square, obviously!"


rec = Rectangle((3,6),(7,2))
print(rec)
print(rec.perimeter())
