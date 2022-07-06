def check_case(word):
    if word.islower():
        print(f"{word} is in lowercase.")
    elif word.isupper():
        print(f"{word} is in uppercase.")
    else:
        print(f"{word} is mixed.")
        
check_case("DEn")