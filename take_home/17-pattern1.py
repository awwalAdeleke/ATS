# A program to give this
"""
|\
| \
|  \
|   \
|____\
"""
def pattern(num):
    start = 1
    while start <= num:
        print("* " * start)
        start += 1

pattern(10)
