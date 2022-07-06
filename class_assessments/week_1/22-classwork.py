# ENCODE ENGINE
def encode_text():
    dict_vowels = {"a" : "#", "e" : "$", "i" : "%", "o" : "&", "u" : "*"}
    special_char = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
    dict_int = {"0" : "z", "1" : "y", "2" : "x", "3" : "w", "4" : "v", "5" : "u", "6" : "t", "7" : "s", "8" : "r", "9" : "q"}
    code = ""

    text = list(input("What are we encoding? "))
    for i in range(len(text)):
#       encryption for special char
        if text[i] in list(dict_vowels.values()) or text[i] in special_char:
            code += ("|" + text[i])
            
#       encryption for integers
        elif text[i] in list(dict_int.keys()):
            code += ("^" + dict_int[text[i]])

#       encryption for text generally
#       encryption for vowels
        elif text[i] in list(dict_vowels.keys()):
            code += dict_vowels[text[i]]
#       encryption for consonants
        elif text[i] == text[i].lower():
            code += text[i].upper()
        else:
            code += text[i].lower()
    return code

print(encode_text())


# Abdul-raheem's way of solving:
"""
import string

def encode(data:str):
    digits = string.digits
    sChars = string.punctuations
    alpha_lower = string.ascii_lowercase
    alpha_upper = string.ascii_uppercase
    rev_alpha_lower = alpha_lower[::-1]
    vowels = ["a", "e", "i", "o", "u"]
    vowels_map = ["#", "$", "%", "&", "*"]
    enc = [] // or list()
    for s in data:
        if s.lower() in vowels:
            enc.append(vowels_map[vowels.index(s.lower())])
        elif s in SChars:
            enc.append("|" + s)
        elif s in alpha_lower + alpha_lower:
            enc.append(s.swapcase())
        elif s in digits:
            enc.append("^" + rev_alpha_lower[digits.index(s)])
    
"""


# DECODE ENGINE
def decode_text():
    dict_vowels = {"#" : "a", "$" : "e", "%" : "i", "&" : "0", "*" : "u"}
    special_char = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
    dict_int = {"z" : "0", "y" : "1", "x" : "2", "w" : "3", "v" : "4", "u" : "5", "t" : "6", "s" : "7", "r" : "8", "q" : "9"}
    code = ""
    
    text = list(input("What are we decoding? "))
    for i in range(len(text)):
        
#       decryption for special char
        if text[i] == "|":
            code += text[i+1]

#       decryption for integers
        elif text[i] in special_char and text[i+1] in list(dict_int.keys()):
            code += dict_int[text[i]]

#       decryption for text generally
#       decryption for vowels
        elif text[i] in list(dict_vowels.keys()):
            code += dict_vowels[text[i]]
#       decryption for consonants
        elif text[i] == text[i].lower():
            code += text[i].upper()
        else:
            code += text[i].lower()
            
        return code

# print(decode_text())