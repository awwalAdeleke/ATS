def fib(n):
    numbers = []
    for i in range(n):
        if i == 0 or i == 1:
            numbers.append(i)
        else:
            numbers.append(numbers[i-1] + numbers[i-2])
    print(numbers)
    
fib(10)


def fib2(n):
    if n == 0 or n == 1:
        return n
    return fib2(n-1) + fib2(n-2)

print(fib2(10))