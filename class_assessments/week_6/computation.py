

class Computation:

    def __init__(self) -> None:
        pass

    def factorial(self, num: int):
        if num == 0 or num == 1:
            return 1
        return num * self.factorial(num - 1)

    def sum(self, num):
        result = 0
        for i in range(1, num + 1):
            result += i
        return result

    def testPrim(self, num: int):
        isPrime = True
        if num == 0 or num == 1:
            isPrime = False
            return isPrime
        for i in range(2, num):
            if num % i == 0:
                isPrime = False
                break
        return isPrime

    def tableMult(self, num: int):
        print(f"Multiplication Table for {num}".center(60, '='))
        for multiple in range(1,13):
            print(f"{num} * {multiple} = {num * multiple}")

    def allTableMult(self):
        for i in range(1,10):
            self.tableMult(i)

    @staticmethod
    def listDiv(num):
        Ldiv = []
        for i in range(1, num + 1):
            if num % i == 0:
                Ldiv.append(i)
        return Ldiv

    def listPrimDiv(self,num):
        Ldiv = Computation.listDiv(num)
        return [fig for fig in Ldiv if self.testPrim(fig) == True]


num = Computation()
print(num.listPrimDiv(9))