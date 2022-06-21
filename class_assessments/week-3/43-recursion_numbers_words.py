def numbers_in_words(num:int):
    fixed_numbers = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
               7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
               13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
               18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
               50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
               100: "one hundred", 1000: "one thousand"}

    units = num % 10
    tens = ((num // 10) % 10) * 10
    hundreds = (num // 100) % 10
    thousands = (num // 1000)

    if num in fixed_numbers:
        return fixed_numbers[num].title()
    elif num > 20 and num < 100:
        return f"{fixed_numbers[tens]}-{fixed_numbers[units]}".title()
    elif (num > 100 and num < 1000) and num % 100 == 0:
        return f"{fixed_numbers[hundreds]} hundred".title()
    elif (num > 100 and num < 1000):
        return f"{fixed_numbers[hundreds]} hundred and {numbers_in_words(tens + units)}".title()
    elif (num > 1000) and num % 1000 == 0:
        return f"{fixed_numbers[thousands]} thousand".title()
    elif num > 1000:
        return f"{numbers_in_words(thousands)} thousand, {numbers_in_words(num % 1000)}".title()


print(numbers_in_words(506003))