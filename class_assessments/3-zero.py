num = int(input("Which number are you comparing? "))
if num < 0:
    print(f"The number {num} is less than 0")
elif num > 0:
    print(f"The number {num} is greater than 0")
else:
    print(f"The number {num} is 0")