import csv
import string
import sys

def enter_f_name():
    return input("Enter your first name:\n")

def enter_l_name():
    return input("Enter your last name:\n")

def enter_u_name():
    return input("Enter your username(Length must be 8, it must include at least one number):\n")

def enter_password():
    return input("Enter your password(Length must be 8 and it must contain at least one number and a special character):\n")

def confirm_password(password, password_input):
    if password_input == password:
        return True
    return False

def confirm(username, password):
    data = get_data()
    for i in data:
        if username == i["Username"] and password == i["Password"]:
            return True
    return False

def check_length(args, num=8):
    if len(args) == num:
        return True
    return False

def get_data():
    with open(r'C:\Users\AwwalOlamideAdeleke\Desktop\python-afex\users.csv', 'r') as file:
        handler = csv.DictReader(file)
        return list(handler)



def sign_up():
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    numbers = string.digits
    special_char = string.punctuation
    f_name = enter_f_name()
    l_name = enter_l_name()

    u_name = enter_u_name()
    if any(item in u_name for item in lower_letters) == False and any(item in u_name for item in numbers) == False and check_length(u_name) == False:
        u_name = input("Invalid username, one more attempt(s) left. Try again.\n")

    password = enter_password()
    if any(item in password for item in (upper_letters + lower_letters)) == False and any(item in password for item in (numbers + special_char)) == False and len(password) != 8:
        print("The password you entered does not meet the requirements. Try again")
        password = input("One more attempt(s) left. Re-enter your password(Length must be 8 and it must contain at least one number or a special character): \n")

    def save_details():
        with open(r"C:\Users\AwwalOlamideAdeleke\Desktop\python-afex\users.csv", "a") as file:
            headers = ["First_name", "Last_name", "Username", "Password"]
            handler = csv.DictWriter(file, fieldnames=headers)
            handler.writerow({"First_name": f_name, "Last_name": l_name, "Username": u_name, "Password": password})
        return

    password_input = input("Enter your password again:\n")
    if confirm_password(password, password_input) != True:
        return "The passwords did not match!"
    else:
        save_details()
        response = int(input("Press 1 to sign in\nPress 2 to log out\n"))
        if response == 1:
            sign_in()
        if response == 2:
            sys.exit()



def sign_in():
    u_name = enter_u_name()
    password = enter_password()
    # print(confirm(u_name, password))
    if confirm(u_name, password) == True:
        print("You have signed in.")
        response = int(input("Press 1 to edit your profile\nPress 2 to change password\nPress 3 to log out\n"))
        if response == 1:
            edit_profile(u_name)
        elif response == 2:
            old_password = input("Enter your old password:\n")
            new_password = input("Enter your new password:\n")
            password2 = input("Please confirm your new password:\n")
            if confirm_password(new_password, password2) != True:
                return "The passwords did not match!"
            print(change_password(old_password, new_password))
        elif response == 3:
            sys.exit()
    else:
        return "Invalid log in details."


def entry():
    welcome_message = int(input("Welcome to THE Mobile App.\nPress 1 to sign in\nPress 2 to sign up\n"))
    if welcome_message == 1:
        print(sign_in())
    elif welcome_message == 2:
        print(sign_up())
    else:
        print("Invalid selection.")

def edit_profile(username):
    data = get_data()
    for i in data:
        if username == i['Username']:
            phone_no = input("Please add your mobile number, preferably with Nigerian callcodes: ")
            address = input("Enter your address: ")
            dob = input("Enter your date of birth in this format: ")
            gender = input("Enter your gender: ")
            with open(r'C:\Users\AwwalOlamideAdeleke\Desktop\python-afex\users.csv', 'w+') as file:
                header = ["First_name", "Last_name", "Username", "Password", "Phone_number", "Address", "Date_of_birth", "Gender"]
                handler = csv.DictWriter(file ,fieldnames=header)
                handler.writeheader()
                handler.writerow({"First_name": i["First_name"], "Last_name": i["Last_name"], "Username": i["Username"], "Password": i["Password"], "Phone_number": phone_no, "Address": address , "Date_of_birth": dob, "Gender": gender})
    return "Edit is complete!"

def change_password(old_password, new_password):
    data = get_data()
    for i in data:
        if old_password in i['Password']:
            i["Password"] = new_password
        else:
            return "Password is incorrect!"


if __name__ == '__main__':
    entry()