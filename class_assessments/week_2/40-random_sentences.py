# FUNCTION TO GENERATE A SPECIFIED NUMBER OF UNIQUE RANDOM SENTENCES
import random

def print_unique_random_sentences(num):
    subjects = ["The men", "You", "We", "They", "The group"]
    verbs = ["eat", "drive", "are", "slapped", "sip"]
    objects = ["drinks", "painters", "cars", "them", "food"]

    sentences = []
    i = num
    while i > 0:
        sentence = f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}."
        if sentence not in sentences or len(sentences) != len(subjects) * len(verbs) * len(objects):
            print(sentence)
            sentences.append(sentence)
            i -= 1
        else:
            print("There are no more unique random sentences to generate.")
            break


    print(len(sentences))
print_unique_random_sentences(125)