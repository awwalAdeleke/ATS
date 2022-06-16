# FUNCTION TO CHANGE A NUMBER TO WORDS
def numbers_in_words(num:int):
    fixed_numbers = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
               7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
               13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
               18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
               50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
               100: "one hundred", 1000: "one thousand"}

#   T0 CATER FOR THE RANGE OF THE INDEXING
    if len(str(num)) >= 2:
        tens = int(str(num)[-2])
    if len(str(num)) >= 3:
        hundreds = int(str(num)[-3])
    if len(str(num)) >= 4:
        thousands = int(str(num)[-4])
    units = num % 10

#   TO CHECK IF IT IS PART OF THE FIXED NUMBERS, IF NOT DERIVE THE WORD...
    if num in fixed_numbers:
        print(fixed_numbers[num].title())
    elif len(str(num)) == 2 and units != 0:
        print("{}-{}".format(fixed_numbers[tens * 10].title(), fixed_numbers[units]))
    elif len(str(num)) == 3:
        if hundreds >= 1:
            if tens >= 1 and units > 0:
                print("{} hundred and {}-{}".format(fixed_numbers[hundreds].title(), fixed_numbers[tens * 10], fixed_numbers[units]))
            elif tens == 0 and units > 0:
                print("{} hundred and {}".format(fixed_numbers[hundreds].title(), fixed_numbers[units]))
            elif tens == 0 and units == 0:
                print("{} hundred".format(fixed_numbers[hundreds].title()))
    elif len(str(num)) == 4:
        if thousands >= 1:
            if hundreds >= 1 and units > 0:
                if tens >= 1:
                    print("{} thousand, {} hundred and {}-{}".format(fixed_numbers[thousands].title(), fixed_numbers[hundreds], fixed_numbers[tens * 10], fixed_numbers[units]))
                elif tens == 0:
                    print("{} thousand, {} hundred and {}".format(fixed_numbers[thousands].title(), fixed_numbers[hundreds], fixed_numbers[units]))
                
            else:
                if tens >= 1 and units == 0:
                    print("{} thousand and {}".format(fixed_numbers[thousands].title(), fixed_numbers[tens * 10]))
                elif tens == 0 and units == 0:
                    print("{} thousand".format(fixed_numbers[thousands].title()))

numbers_in_words(500)