# list_of_palindromes = []
# for i in range(10000,100000):
#     figure = str(i)
#     if figure[0] == figure [-1] and figure[1] == figure[-2]:
#         list_of_palindromes.append(figure)
# print(list_of_palindromes)

# num = input("What number are we checking? ")
# if num >= 10000 and num < 100000:
#     if num in list_of_palindromes:
#         print(f"{num} is a palindrome")
#     else:
#         print(f"{num} is not a palindrome")

# End of list procedure

# num = input("What number are we checking? ")
# reverse_num = "".join(list(reversed(num)))
# if num == reverse_num:
#     print(f"{num} is a palindrome")
# else:
#     print(f"{num} is not a palindrome")

# End of reversed function

def check(num):
    reverse_num = 0
    while num > 0:
        reverse_num = reverse_num * 10 + num % 10
        num = num // 10
    return reverse_num

num_request = int(input("What number are we checking? "))

if num_request == check(num_request):
    print(f"{num_request} is a palindrome")
else:
    print(f"{num_request} is not a palindrome")