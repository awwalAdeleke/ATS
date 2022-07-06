def max_():
    num_list = []
    add_num = int(input("How many values do you want to add into the list? "))
    for i in range(add_num):
        num_list.append(int(input("Enter value: ")))

    max_num = num_list[0]
    for i in num_list:
        if i > max_num:
            max_num = i

    print(f"{max_num} is the maximum number.")

max_()