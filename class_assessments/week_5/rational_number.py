class RationalNumber:
    def __init__(self, numerator: int = 0, denominator: int = 1) -> None:
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def max_denominator(rational_num_1, rational_num_2):
        max_denominator = 0
        if rational_num_1.denominator < rational_num_2.denominator:
            max_denominator = rational_num_2.denominator
        else:
            max_denominator = rational_num_1.denominator
        return max_denominator

    @staticmethod
    def min_denominator(rational_num_1, rational_num_2):
        min_denominator = 0
        if rational_num_1.denominator < rational_num_2.denominator:
            min_denominator = rational_num_1.denominator

        else:
            min_denominator = rational_num_2.denominator
        return min_denominator

    def highest_common_factor(self):
        max_num = 0
        for i in range(1,self.denominator+1):
            if self.denominator % i == 0 and self.numerator % i == 0:
                max_num = i
        return max_num

    def __str__(self) -> str:
        return f" {int(self.numerator/self.highest_common_factor())}\n —\n {int(self.denominator/self.highest_common_factor())}"

    @staticmethod
    def lowest_common_multiple(rational_num_1, rational_num_2) -> int:          # type: ignore
        max_num = RationalNumber.max_denominator(rational_num_1, rational_num_2)
        min_num = RationalNumber.min_denominator(rational_num_1, rational_num_2)
        for i in range(max_num, (max_num*min_num) + 1):
            if i % max_num == 0 and i % min_num == 0:
                return i


    def __add__(self, other):
        lcm = RationalNumber.lowest_common_multiple(self, other)
        part_1 = (lcm/self.denominator)*self.numerator
        part_2 = (lcm/other.denominator)*other.numerator
        sum_of_parts = part_1 + part_2
        return RationalNumber(sum_of_parts, lcm)

    def __sub__(self, other):
        lcm = RationalNumber.lowest_common_multiple(self, other)
        part_1 = (lcm/self.denominator)*self.numerator
        part_2 = (lcm/other.denominator)*other.numerator
        diff_of_parts = part_1 - part_2
        return RationalNumber(diff_of_parts, lcm)

    def __mul__(self, other):
        numerator_product = self.numerator * other.numerator
        denominator_product = self.denominator * other.denominator
        return RationalNumber(numerator_product, denominator_product)

    def __truediv__(self, other):
        numerator_product = self.numerator * other.denominator
        denominator_product = self.denominator * other.numerator
        return RationalNumber(numerator_product, denominator_product)

    def print_float(self):
        return self.numerator/self.denominator

num1 = RationalNumber(18,9)
num2 = RationalNumber(3,9)

print(num1 + num2)
