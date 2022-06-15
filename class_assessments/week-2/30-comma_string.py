vowels = ["a", "e", "i" , "o", "u"]
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

vowels.extend(consonants)
ordered_letters = ",".join(sorted(vowels))
print(ordered_letters)