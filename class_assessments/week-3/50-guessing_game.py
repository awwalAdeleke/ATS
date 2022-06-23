import random

def generate_random():
    return random.randint(0,10)


def game():
    i = 1
    correct_num = generate_random()
    while i <= 5:
        num = int(input("Guess the number from 0 to 10: "))
        if num == correct_num:
            return f"{num} is the correct number!"
        print("Wrong!")
        i += 1
    return "You lose! The correct number is {correct_num}"


if __name__ == '__main__':
    print(game())