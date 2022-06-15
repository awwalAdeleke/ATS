import string

letters = string.ascii_lowercase

print(f"The first ten letters of the alphabets are {list(letters[:10])}")
print(f"The last ten letters of the alphabets are {list(letters[-10:])}")
vowels = []
consonants = []

for i in letters:
    if i in ["a","e","i","o","u"]:
        vowels.append(i)
    else:
        consonants.append(i)

print(vowels)
print(consonants)