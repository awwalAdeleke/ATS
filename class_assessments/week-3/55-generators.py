# Generators are iterables that doesn't store all its values in memory and it can be iterated one at a time.
# Usually bound with functions

def loop():
    l = [1,2,3,4]
    for num in l:
        yield num

f = loop()
# print(type(f))

# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

# for r in f:
#     print(r)
    
# with open(r"C:\Users\AwwalOlamideAdeleke\Desktop\python-afex\class_assessments\week-3\words.txt", "r") as file:
#     print(type(file.readlines()))


dic_ = {"bname": "Awwal", "cname": "Olamide"}
# print(type(dic_.keys()))

def main():
    for value in dic_.values():
        yield value

n = main()
# print(main())

# for i in main():
#     print(i)

# print(next(n))
# print(next(n))

def read_file(name):
    for row in open(name):
        yield row

file = read_file(r"C:\Users\AwwalOlamideAdeleke\Desktop\python-afex\class_assessments\week-3\words.txt")

print(next(file))
print(next(file))
print(next(file))
print(next(file))


