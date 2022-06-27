def prime(num):
    isCheckPrime = True
    i = 2
    while i < num:
        if num % i == 0:
            isCheckPrime = False
            break
        i += 1
    return isCheckPrime

# def prime_list(num):
#     prime_list = []
#     for i in range(2, num + 1):
#         if prime(i) == True:
#             prime_list.append(i)
#     for i in prime_list:
#         print(i)
#     print(len(prime_list))


def extra_prime(num):
    extra_prime_list = []
    root = round(num ** 0.5)

    for i in range(2, root + 1):
        if prime(i) == True:
            extra_prime_list.append(i)
    isCheckPrime = True
    for i in extra_prime_list:
        if num % i == 0:
            isCheckPrime = False
            break
    return isCheckPrime

def prime_list(num):
    prime_list = []
    for i in range(2, num + 1):
        if extra_prime(i) == True:
            prime_list.append(i)
    for i in prime_list:
        print(i)
    print(len(prime_list))

if __name__ == '__main__':
    print(prime_list(1000))

