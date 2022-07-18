class Rectangle:
    def __init__(self, length = 1, width = 1) -> None:
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def __length(self, value):
        if value < 0.0 or value > 20.0:
            raise ValueError("Value can not be less than 0.0 or greater than 20.0")
        self.__length = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def __width(self, value):
        if value < 0.0 or value > 20.0:
            raise Exception("Value can not be less than 0.0 or greater than 20.0")
        self.__width = value


    def perimeter(self):
        return (2 * self.__length) + (2 * self.__width)

    def area(self):
        return self.__length * self.__width

rec = Rectangle(20,40)
# rec.length = 20
# print(rec.length)