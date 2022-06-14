# def func(x:float) -> float:
#     return x

# print(func("string"))
# the specification does not work on this interpreter but works online.
# It's in the form def func(var : datatype) -> return datatype

# Positional parameters , keyword arguments.
# The order and arrangement is very important in positional parameters.
# Keyword arguments are like name parameters.

# They are in this form:
#     def func(*args, **kwargs)
#                |         |
#            pos-params  named params
# Named parameters
# in the form:
#           def func(x = 0, y = 0)
# datatype specification works in it too i.e
#           def func(x:int = 0, y:int = 0) -> int:

# Use a function and the args keyword:

# def diff(*y):
#     return y * 4

# print(diff(2))

# Using def func(*y) make sit possible to put in infinite number of parameters
# That is,
# def add(*y):
#     sum = 0
#     for i in y:
#         sum += i
#     return sum

# print(add(2,5,4,2,6,7,8,9,24,11))


# Using def func(**y) make sit possible to put in infinite number of key-value parameters
# That is:
def add_value(**students):
    for key, val in students.items():
        print(f"{key} : {val}")

add_value(name = "Ola", age = 18, gender = "male")




# The print function is defined as such:
#       def print(*val, sep="", end="\n")

# To create a function that practically does nothing, we define it as such:
#       def func():
#           pass


# The "return" keyword when invoked, breaks out of the entire block of code.
# That is why it is usually invoked at the end of the block of code.
# The "break" keyword breaks out of the immediate cell and runs the cell again.
# The "continue" keyword skips the immediate cell of the block of code and moves
# to the parent cell.

"""
def func(var1, var2): ---------
    for i in var1:----------  |
        print(i)           |  |
        for j in var2: --  |  |
            print(j)    |  |  |
            break ------   |  |
            continue -------  |
            return------------
"""