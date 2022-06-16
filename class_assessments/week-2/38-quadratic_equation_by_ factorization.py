def solve_quadratic_equation(a:int, b:int, c:int):
    product = a * c
    factors = [i for i in range(-abs(product), abs(product) + 1) if i != 0 and product % i == 0]
    
    working_factors = [factor for factor in factors for i in range(len(factors)) if factor + factors[i] == b and factor * factors[i] == product]

    if len(working_factors) == 0:
        print("This equation has no working factors, hence it can not solved by factorisation method.")
    elif a == 1 or a < 0 and len(working_factors) == 1:
        print(f"x = {-(working_factors[0])} two times")
    elif a == 1 and len(working_factors) == 2:
        print(f"x = {-(working_factors[0])} and {-(working_factors[1])}")
    elif a > 1 or a < 0 and len(working_factors) == 2:
        print(f"x = {-(working_factors[0])/a} and {-(working_factors[1])/a}")

solve_quadratic_equation(5,2,1)