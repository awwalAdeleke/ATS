# A program to give this
"""
------
\    |
 \   |
  \  |
   \ |
    \|

"""
def pattern(num):
    space = 0
    stop = num
    while stop > 0 and space < num:
        print("  " * space, "* " * stop)
        stop -= 1
        space += 1

pattern(10)