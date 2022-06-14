def isPerfect(num):
    sum = 0
    for i in range(1, num + 1):
        if num % i == 0:
            sum += i
    if sum/2 == num:
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")

isPerfect(10)