username = "bestcoder05"
password = "password05"

name_request = input("Enter your username: ")
password_request = input("Enter your password: ")

if name_request == username and password_request == password:
    print("Login successful!")
else:
    print("Incorrect Login Credentials. Check your details and try again.")