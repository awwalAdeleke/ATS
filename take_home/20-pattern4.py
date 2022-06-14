# A program to give this
"""
    /|
   / |
  /  |
 /   |
/    |
------

"""
def pattern(num):
    space = num - 1
    stop = 1
    while stop <= num and space >= 0:
        print("  " * space, "* " * stop)
        stop += 1
        space -= 1

pattern(10)