import string

def pangram(word):
    word = list(word.lower())
    for i in word:
        if i not in (string.ascii_lowercase):
            word.remove(i)
    word_set = set(word)
    letter_set = set(string.ascii_lowercase)
    if word_set == letter_set:
        print("This word is a pangram.")
    else:
        print("This word is not a pangram.")

pangram("The quick brown fox jumps over the lazy dog.")
