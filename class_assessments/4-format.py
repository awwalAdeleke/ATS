l_name = input("Enter your last name: ")
f_name = input("Enter your first name: ")
message1 = "His name is {}".format(f_name)
message2 = f"His name is {l_name}"
message3 = "His name is {0} {1}".format(f_name, l_name)
message4 = "His name is {1} {0}".format(f_name, l_name)
print(message3)