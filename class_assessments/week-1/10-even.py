num_list = [1,2,3,4,5,6,7,8,9,10]
# for i in num_list:
#     if i % 2 == 0:
#         print(i)
        
# i = 0
# while i < len(num_list):
#     if num_list[i] % 2 == 0:
#         print(num_list[i])
#     i += 1
    
# for i in num_list:
#     if i % 2 == 0 and i < 5:
#         print(i)
        
# for i in num_list:
#     if i < 5:
#         if i % 2 == 0:
#             print(i)
#     else:
#         break
    
for i in num_list:
    if i % 2 != 0:
        continue
    print(i)
    
for i in range(0, 10, 2):
    print(i)