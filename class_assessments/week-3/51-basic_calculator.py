def add(lis_):
    result = lis_[0]
    for i in range(1, len(lis_)):
        result += lis_[i]
    return result

def diff(lis_):
    result = lis_
    for i in range(1, len(lis_)):
        result -= lis_[i]
    return result

def multiply(lis_):
    result = lis_[0]
    for i in range(1, len(lis_)):
        result *= lis_[i]
    return result

def divide(lis_):
    result = lis_[0]
    for i in range(1, len(lis_)):
        if 0 in lis_[1:]:
            return "Infinity"
        result /= lis_[i]
    return result


def calculator():
    list_num = []
    length = int(input("How many numbers are you working for each operator: "))
    for i in range(length):
        num = int(input("Enter the number you are operating: "))
        list_num.append(num)
    response = input("Which operator are you using:\n +\n -\n *\n /\n")
    if response == "+":
        print(add(list_num))
    elif response == "-":
        print(diff(list_num))
    elif response == "*":
        print(multiply(list_num))
    elif response == "/":
        print(divide(list_num))


if __name__ == '__main__':
    calculator()