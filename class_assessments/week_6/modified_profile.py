import csv


class Person:

    file_path = r"C:\Users\AwwalOlamideAdeleke\Desktop\python-afex\modified_profile.csv"

    def __init__(self,username) -> None:

        if username not in self.previous_data():
            raise ValueError(f"This username, {username} is not in the database!")
        else:
            self.username = username
            self.profile = self.previous_data().get(username, f"{username} can not be found!")
            self.first_name = self.profile["First_name"]   # type: ignore
            self.last_name = self.profile["Last_name"]   # type: ignore
            self.password = self.profile["Password"]   # type: ignore
            self.phone_number = self.profile["Phone_number"]   # type: ignore
            self.home_address = self.profile["Address"]   # type: ignore
            self.dob = self.profile["Date_of_birth"]   # type: ignore
            self.gender = self.profile["Gender"]   # type: ignore

    @classmethod
    def get_data(cls):
        with open(Person.file_path, 'r') as file:
            handler = csv.DictReader(file)
            return list(handler)

    def previous_data(self):
        self.all_members = {}
        data = self.get_data()
        for i in range(len(data)):
            key = data[i]["User_name"]
            del data[i]["User_name"]
            self.all_members[key] = data[i]
        return self.all_members


    def update_names(self):
        f_name = input("What is your first name?\n")
        l_name = input("What is your last name?\n")

        data = self.get_data()
        updated_list = []
        for i in data:
            if self.username == i["User_name"]:
                i["First_name"] = f_name
                i["Last_name"] = l_name
            updated_list.append(i)

        for data in updated_list:
            with open(Person.file_path, 'w') as file:
                header = ["First_name", "Last_name", "User_name", "Password", "Phone_number", "Address", "Date_of_birth", "Gender"]
                handler = csv.DictWriter(file ,fieldnames=header)
                handler.writeheader()
                handler.writerows(updated_list)
    
    def change_password(self):
        old_password = input("Enter your old password:\n")
        data = self.get_data()
        updated_list = []
        for i in data:
            if old_password == i["Password"]:
                new_password = input("Enter your new password:\n")
                i["Password"] = new_password
            else:
                print("The password is incorrect!")

            updated_list.append(i)

        for data in updated_list:
            with open(Person.file_path, 'w') as file:
                header = ["First_name", "Last_name", "User_name", "Password", "Phone_number", "Address", "Date_of_birth", "Gender"]
                handler = csv.DictWriter(file ,fieldnames=header)
                handler.writeheader()
                handler.writerows(updated_list)



user = Person("awwal231")
print(user.profile)
user.change_password()
