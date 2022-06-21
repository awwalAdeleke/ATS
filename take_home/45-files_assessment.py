# A program that asks for your username, first name, last name,
# password, password confirmation and saves it in a text file with name as username.

username = input("What is your username? ")
f_name = input("What is your first name? ")
l_name = input("Enter your last name? ")
password = input("Enter your password: ")
password_confirmation = input("Enter your password again: ")
if password_confirmation == password:
    with open(f"{username}.txt", "w") as file:
        file.write(f"Username is {username}.\nFirst name is {f_name}.\nLast name is {l_name}.\nPassword is {password}")
else:
    print("These passwords didn't match.")