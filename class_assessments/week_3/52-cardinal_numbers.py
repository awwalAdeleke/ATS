def numbers_to_cardinals(num:int):
    fixed_numbers = {1 : "st", 2 : "nd", 3 : "rd", 11 : "th", 12 : "th" , 13: "th"}

    cardinal_units = num % 10
    cardinal_tens = num % 100

    if cardinal_tens in fixed_numbers and cardinal_tens < 20:
        return f"{num}{fixed_numbers[cardinal_tens]}"
    elif cardinal_units in fixed_numbers:
        return f"{num}{fixed_numbers[cardinal_units]}"
    return f"{num}th"


print(numbers_to_cardinals(1113))