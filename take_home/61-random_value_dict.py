import random
import re
import string

def random_dict():
    letters = string.ascii_uppercase

    keys = list(letters)[:20]

    random_value_dict = {}

    for i in keys:
        random_value_dict[i] = random.randint(1,99)

    def check_duplicate(random_value_dict:dict):
        new_values = set(sorted(list(random_value_dict.values())))
        if len(new_values) != 20:
            return False
        return True

    if check_duplicate(random_value_dict) == True:
        print("The dictionary has no duplicate values.")
        return random_value_dict
    return "The dictionary has duplicate values."


# def check_duplicate(random_value_dict:dict):
#     new_values = set(sorted(list(random_value_dict().values)))
#     if len(new_values) != 20:
#         return False
#     return True

if __name__ == '__main__':
    print(random_dict())