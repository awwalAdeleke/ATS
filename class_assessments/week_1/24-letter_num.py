import string

sentence = input("What are we evaluating? ")
alpha_lower = string.ascii_lowercase
alpha_upper = string.ascii_uppercase
new_lower = ""
new_upper = ""
for i in sentence:
    if i in alpha_lower:
        new_lower += i
    elif i in alpha_upper:
        new_upper += i

print(f"The sentence has {len(new_lower)} lowercase characters and {len(new_upper)} uppercase characters.")