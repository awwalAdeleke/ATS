list_num = [1,2,3,4,5]

num = int(input("How many numbers are you adding? "))
for i in range(num):
    input_num = int(input("Enter :"))
    list_num.append(input_num)
    

for i in list_num:
    if i % 2 != 0:
        list_num.remove(i)
        
print(list_num)