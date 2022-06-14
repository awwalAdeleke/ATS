def check(bin):
    power = 0
    num = 0
    while bin > 0:
        num = num + ((bin % 10) * 2**power)
        bin = bin // 10
        power += 1
    return num

bin_request = int(input("Enter your binary number: "))

print(check(bin_request))


# 110