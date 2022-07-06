# with open("C:\\Users\\AwwalOlamideAdeleke\\Desktop\\python-afex\\class_assessments\\week-3\\star_poem.txt", "r") as file:
#     print(file.readlines())
    
with open("new_poem.txt", "w") as file:
    file.write("I am a big boy now. I don't read poems no more.")

with open("C:\\Users\\AwwalOlamideAdeleke\\Desktop\\python-afex\\class_assessments\\week-3\\star_poem.txt", "r+") as file:
    file.writelines("I am a bigger girl now. I don't read poems no more.")