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

num_request = int(input("Find the factorial of: "))

print(factorial(num_request))


