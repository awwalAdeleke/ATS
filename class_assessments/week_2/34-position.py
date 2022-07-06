import string

alphabets = string.ascii_lowercase
alpha_dict = {}
for i,j in enumerate(alphabets):
    alpha_dict[i + 1] = j
    
print(alpha_dict)