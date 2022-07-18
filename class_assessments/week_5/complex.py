class Complex:

    def __init__(self, real: float = 0, imaginary: float = 0) -> None:
        self.real = real
        self.imaginary = imaginary

    @classmethod
    def add(cls, complex_num_1, complex_num_2):
        real_result = complex_num_1.real + complex_num_2.real
        imaginary_result = complex_num_1.imaginary + complex_num_2.imaginary
        return f"{__class__.__name__}({real_result}, {imaginary_result})"

    @staticmethod
    def subtract(complex_num_1, complex_num_2):
        real_result = complex_num_1.real - complex_num_2.real
        imaginary_result = complex_num_1.imaginary - complex_num_2.imaginary
        return f"{__class__.__name__}({real_result}, {imaginary_result})"


complex_1 = Complex(5,4)
complex_2 = Complex(8,9)

print(Complex.add(complex_1, complex_2))
