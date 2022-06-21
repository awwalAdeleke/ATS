import csv
import string

def sign_up():
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    numbers = string.digits
    special_char = string.punctuation
    f_name = input("Enter your first name: ").title()
    l_name = input("Enter your last name: ").title()

    def save_details():
        with open("users.csv", "w+") as file:
            headers = ["First_name", "Last_name", "Username", "Password"]
            handler = csv.DictWriter(file, fieldnames=headers)
            handler.writeheader()
            handler.writerow({"First_name": f_name, "Last_name": l_name, "Username": u_name, "Password": password})
        return

    u_name = input("Enter your username(Length must be 8, all letters must be in lowercase and it must include at least one number): ")
    if any(item in u_name for item in lower_letters) == False and any(item in u_name for item in numbers) == False and len(u_name) != 8:
        u_name = input("Invalid username, one more attempt(s) left. Try again.\n")

    password = input("Enter your password(Length must be 8 and it must contain at least one number and a special character):\n")
    if any(item in password for item in (upper_letters + lower_letters)) == False and any(item in password for item in (numbers + special_char)) == False and len(password) != 8:
        print("The password you entered does not meet the requirements. Try again")
        password = input("One more attempt(s) left. Re-enter your password(Length must be 8 and it must contain at least one number or a special character): \n")

    password_confirmation = input("Enter your password again: ")
    if password_confirmation != password:
        print("The password you entered does not match.")
    else:
        save_details()
    return



def sign_in():
    u_name = input("Enter your username: ")
    password = input("Enter your password: ")
    with open("users.csv", "r") as file:
        headers = ["First_name", "Last_name", "Username", "Password"]
        handler = csv.DictReader(file, fieldnames=headers)
        for row in handler:
            if u_name in row["Username"] and password in row["Password"]:
                print("You have signed in.")
            else:
                print("Invalid log in details. Forgotten details? You should sign up.")
                sign_up()
    return

welcome_message = int(input("Welcome to THE Mobile App.\nPress 1 to sign in\nPress 2 to sign up\n"))
if welcome_message == 1:
    sign_in()
elif welcome_message == 2:
   sign_up()
else:
    print("Invalid selection.")
