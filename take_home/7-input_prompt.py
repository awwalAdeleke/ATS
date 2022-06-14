f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
username = input("Enter your username: ")
password = input("Enter your password: ")
print("All details saved. Now sign in with your details.")

name_request = input("Username: ")
password_request = input("Password: ")

if name_request == username and password_request == password:
    print(f"You have successfully logged in, {username}!")
else:
    print("Incorrect. Please check your details and try again.")