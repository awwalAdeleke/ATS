import random
random_values = random.sample(range(100), 20)

def find_duplicates(random_list: list):
    random_set = set(random_list)
    if len(random_set) < 20:
        print("Duplicates exist!")

find_duplicates(random_values)

random_dict = {}
for value in random_values:
    random_dict[str(value)] = value

print(random_dict)

# from operator import index
# import random
# random_values = random.sample(range(100), 20)
# counter = 0
# while counter < 20:
#     duplicates = []
#     for random_values[counter] in random_values:
#         duplicates.append(random_values[counter])
#     if len(duplicates) > 1:
#         print(f"{random_values[counter]} has a duplicates")
# random_dict = {}
# for value in random_values:
#     random_dict[str(value)] = value
