def factorial(num):
    product = num
    if num == 0:
        product = 1
    while num > 0:
        if num != 1:
            product *= (num - 1)

        else:
            product *= 1
        num -= 1
    
    return product

def evaluate_e(num):
    e = 1
    while num > 0 :
        e += 1/(factorial(num))
        num -= 1
    return e

stop = int(input("We should stop at number: "))
print(evaluate_e(stop))