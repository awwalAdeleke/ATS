# From a list of words, get a random word and give dashes of length of the word and try to guess each character in the word.

import re
import sys
from random import randint


def get_word():
    with open(r"C:\Users\AwwalOlamideAdeleke\Desktop\python-afex\class_assessments\week-3\words.txt", "r") as file:
        file = file.readlines()
        index = randint(0, len(file))
        result = file[index][0:-1]
        result = result.lower()
        return result

def dashing(word):
    return ["_" for i in range(len(word))]

def enter_letter():
    return input("Which letter are you guessing? ")

def find_index(letter, word):
    indices_object = re.finditer(pattern=letter, string=word)
    indices = [index.start() for index in indices_object]
    return indices

def fill_gaps(letter, word):
    filler = find_index(letter, word)
    dash = dashing(word)
    for i in filler:
        dash = dash[:i] + [letter] + dash[i+1:]
    return dash

def come_back():
    response = input("Press 1 to come back!\nTo hell with them! Press any key to exit the game.\n")
    if response == "1":
        hangman()
    elif response != "1":
        sys.exit()


def hangman():
    word = get_word()
    print("Hello and welcome to Hangman game! This will be a very interesting ride.\n\tYou have 8 tries till the man in the bottom left corner of the screen hangs himself.\n\tGuess the correct letters to fill the dashes and you have saved his life.\n\tDon't and uh-oh!\nBegin!")
    filled = dashing(word)
    dash = ",".join(filled)
    print(dash)
    i = 0

    while i < 8:
        if filled == list(word):
            print("You have saved his life!🏋️‍♂️ He will forever thank you! Come back again to save another man in death row!\n")
            return come_back()
        letter = enter_letter()
        if find_index(letter, word) != []:
            print("Correct! The man might live because of you!")
            filler = find_index(letter, word)
            for i in filler:
                filled = filled[:i] + [letter] + filled[i+1:]
            print(",".join(filled))
        elif find_index(letter, word) == []:
            print(",".join(filled))
            print("Wrong letter! Try Again!")
        i += 1
    print("He is dead! Do not worry, you can save someone else!")
    return come_back()


if __name__ == "__main__":
    hangman()