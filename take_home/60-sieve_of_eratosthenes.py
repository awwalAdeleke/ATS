def sieve_eratosthenes(num):
    list_prime = [True for i in range(num+1)]
    i = 2
    while (i * i <= num):
        if (list_prime[i] == True):
            for factor in range(i * i, num+1, i):
                list_prime[factor] = False
        i += 1

    for i in range(2, num+1):
        if list_prime[i] == True:
            print(i)

sieve_eratosthenes(1000)