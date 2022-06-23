import csv
import string
import sys

def enter_f_name():
    return input("Enter your first name:\n")

def enter_l_name():
    return input("Enter your last name:\n")

def enter_u_name():
    return input("Enter your username(Length must be 8):\n")

def enter_password():
    return input("Enter your password(Length must be 8):\n")

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
    if len(password) < 8:
        print("The password you entered does not meet the requirements. Try again")
        password = input("One more attempt(s) left. Re-enter your password(Length must be 8): \n")

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
            change_password(u_name)
        elif response == 3:
            sys.exit()
        else:
            print("Invalid log in details.")
            return sign_in()


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
    updated_list = []
    for i in data:
        if username == i['Username']:
            i["Phone_number"] = input("Please add your mobile number, preferably with Nigerian callcodes: ")
            i["Address"] = input("Enter your address: ")
            i["Date_of_birth"] = input("Enter your date of birth in this format: ")
            i["Gender"] = input("Enter your gender: ")
        
        updated_list.append(i)

    for data in updated_list:
        with open(r'C:\Users\AwwalOlamideAdeleke\Desktop\python-afex\users.csv', 'w') as file:
            header = ["First_name", "Last_name", "Username", "Password", "Phone_number", "Address", "Date_of_birth", "Gender"]
            handler = csv.DictWriter(file ,fieldnames=header)
            handler.writeheader()
            handler.writerows(updated_list)
    print("Edit is complete!")

def change_password(username):
    updated_list = []
    old_password = input("Enter your old password:\n")
    for i in data:
        if confirm(username, old_password):
            new_password = input("Enter your new password:\n")
            password2 = input("Please confirm your new password:\n")
            if confirm_password(new_password, password2) == True:
                i["Password"] = new_password
                print("Password successfully changed!")
            else:
                return "The passwords do not match!"
        updated_list.append(i)



    for data in updated_list:
        with open(r'C:\Users\AwwalOlamideAdeleke\Desktop\python-afex\users.csv', 'w') as file:
            header = ["First_name", "Last_name", "Username", "Password", "Phone_number", "Address", "Date_of_birth", "Gender"]
            handler = csv.DictWriter(file ,fieldnames=header)
            handler.writeheader()
            handler.writerows(updated_list)



if __name__ == '__main__':
    entry()