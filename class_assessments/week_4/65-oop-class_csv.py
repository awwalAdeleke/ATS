import csv
import sys


class User:

    def __init__(self, **kwargs):
        # f_name = input("Enter your first name: ")
        # l_name = input("Enter your last name: ")
        # u_name = input("Enter your username: ")
        # assert len(u_name) >= 8
        # password = input("Enter your password: ")
        # assert len(password) >= 8


        self.first_name = kwargs['f_name']
        self.last_name = kwargs['l_name']
        self.user_name = kwargs['u_name']
        self.password = kwargs['password']

    # def enter_f_name(self):
    #     return input("Enter your first name:\n")

    # def enter_l_name(self):
    #     return input("Enter your last name:\n")

    # def enter_u_name(self):
    #     return input("Enter your username(Length must be 8):\n")

    # def enter_password(self):
    #     return input("Enter your password(Length must be 8):\n")

    def confirm_password(self, password_confirm):
        # password_confirm = input("Enter your password again: ")
        if password_confirm == self.password:
            return True
        return False

    def get_data(self):
        with open(r'C:\Users\AwwalOlamideAdeleke\Desktop\python-afex\class_users.csv', 'r') as file:
            handler = csv.DictReader(file)
            return list(handler)

    def confirm_user(self):
        data = self.get_data()

        for i in data:
            if self.user_name == i["Username"] and self.password == i["Password"]:
                return True
        print('Sign in failed')
        return False

    def edit_profile(self):
        data = self.get_data()
        updated_list = []
        for i in data:
            if self.user_name == i['Username']:
                i["Phone_number"] = input("Please add your mobile number, preferably with Nigerian callcodes: ")
                i["Address"] = input("Enter your address: ")
                i["Date_of_birth"] = input("Enter your date of birth in this format: ")
                i["Gender"] = input("Enter your gender: ")
                break
        for i in data:
            updated_list.append(i)

        for data in updated_list:
            with open(r'C:\Users\AwwalOlamideAdeleke\Desktop\python-afex\class_users.csv', 'w') as file:
                header = ["First_name", "Last_name", "Username", "Password", "Phone_number", "Address", "Date_of_birth", "Gender"]
                handler = csv.DictWriter(file ,fieldnames=header)
                handler.writeheader()
                handler.writerows(updated_list)
        print("Edit is complete!")

    def save_details(self):
        f_name = self.first_name
        l_name = self.last_name
        u_name = self.user_name
        password = self.password
        data = {"First_name": f_name, "Last_name": l_name, "Username": u_name, "Password": password}
        print(data)
        with open(r'C:\Users\AwwalOlamideAdeleke\Desktop\python-afex\class_users.csv', "a") as file:
            headers = ["First_name", "Last_name", "Username", "Password", "Phone_number", "Address", "Date_of_birth", "Gender"]
            handler = csv.DictWriter(file, fieldnames=headers)
            handler.writerow(data)
            return

    def sign_up(self):
        confirm_password = input('To continue, confirm your password: ')

        if self.confirm_password(confirm_password) != True:
            print("The passwords did not match!")
            return
        else:
            self.save_details()
            response = int(input("Press 1 to sign in\nPress 2 to log out\n"))
            if response == 1:
                self.sign_in()
            if response == 2:
                sys.exit()

    def change_password(self):
        data = self.get_data()
        updated_list = []
        for i in data:
            if self.confirm_user():
                new_password = input("Enter your new password:\n")
                password2 = input("Please confirm your new password:\n")
                if new_password == password2:
                    i["Password"] = new_password
                    print("Password successfully changed!")
                    break
                else:
                    return "The passwords do not match!"

        for i in data:
            updated_list.append(i)



        for data in updated_list:
            with open(r'C:\Users\AwwalOlamideAdeleke\Desktop\python-afex\class_users.csv', 'w') as file:
                header = ["First_name", "Last_name", "Username", "Password", "Phone_number", "Address", "Date_of_birth", "Gender"]
                handler = csv.DictWriter(file ,fieldnames=header)
                handler.writeheader()
                handler.writerows(updated_list)


    def sign_in(self):

        # print(confirm(u_name, password))
        if self.confirm_user() == True:
            print("You have signed in.")
            response = int(input("Press 1 to edit your profile\nPress 2 to change password\nPress 3 to log out\n"))
            if response == 1:
                self.edit_profile()
            elif response == 2:
                self.change_password()
            elif response == 3:
                sys.exit()
            else:
                print("Invalid log in details.")
                return self.sign_in()


    def entry(self):
        welcome_message = int(input("Welcome to THE Mobile App.\nPress 1 to sign in\nPress 2 to sign up\n"))
        if welcome_message == 1:
            self.sign_in()
        elif welcome_message == 2:
            self.sign_up()
        else:
            print("Invalid selection.")

if __name__  == '__main__':
    user = User(**{'f_name':'Olamie','l_name':'Adeyanju','u_name':'ademide2','password':'password'})
    user.entry()
