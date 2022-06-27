import random

num_list = []
i = 1

while True:
    # num = int(input("Enter a number: "))
    num = random.randint(1,50)
    
    if num in num_list:
        print(f"This number {num} already exists!")
    elif num not in num_list :
        num_list.append(num)
        print(num)
        
    if len(num_list) == 20:
        print("This function is no longer taking inputs!")
        break
    i += 1

