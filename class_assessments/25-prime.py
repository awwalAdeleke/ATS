def check_prime(num):
    isNotPrime = False
    if num > 0:
        for i in range(2,num):
            if num % i == 0:
                isNotPrime = True
                break
    if isNotPrime:
        print(f"{num} is not a prime number.")
    else:
        print(f"{num} is a prime number.")
        
check_prime(12)