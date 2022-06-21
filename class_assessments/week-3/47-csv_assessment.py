import csv
from re import search

f_name = input("Enter your first name: ").title()
l_name = input("Enter your last name: ").title()
m_name = input("Enter your middle name: ").title()

age = input("Enter your age: ")
if age.isdigit() == False:
    age = input("Wrong input. Please re-enter your age: ")

occupation = input("Enter your occupation: ")

dob = input("Enter your date of birth in this format dd-mm-yyyy: ").split("-")
if (2022 - int(dob[2])) != int(age):
    dob = input("Wrong input. Please re-enter your date of birth in this format dd-mm-yyyy: ")

genders = ["Male", "Female"]
gender = input("Enter your gender: ").title()
if gender not in genders:
    gender = input("Wrong input. Please re-enter your gender: ").title()

statuses = ["Married", "Single", "Divorced"]
m_status = input("Enter your marital status; Single, Married or Divorced: ").title()
if m_status not in statuses:
    m_status = input("Wrong input. Please re-enter your marital status; Single, Married or Divorced: ")


email = input("Enter your email: ").lower()
if "@" not in email and ".com" not in email:
    email = input("Wrong input. One attempt left, please re-enter your email: ")
    if "@" not in email and ".com" not in email:
        print("Sorry, you have exceeded the number of attempts")

with open("details.csv", "w") as file:
    headers = ["First_name", "Last_name", "Middle_name", "Age", "Occupation", "Date_of_Birth", "Gender", "Marital_Status", "E_mail"]
    handler = csv.DictWriter(file, fieldnames=headers)
    handler.writeheader()
    handler.writerow({"First_name": f_name, "Last_name": l_name, "Middle_name": m_name, "Age": age, "Occupation": occupation, "Date_of_Birth": dob, "Gender": gender, "Marital_Status": m_status, "E_mail": email})
response = int(input("Do you want to save and add more info or search for a term?\nFor save and add, press 1\nFor search, press 2\n"))
if response == 1:
    print("Your file has been saved successfully. Thank you for your time.")
    age = input("Enter your age: ")
    if age.isdigit() == False:
        age = input("Wrong input. Please re-enter your age: ")

    occupation = input("Enter your occupation: ")

    dob = input("Enter your date of birth in this format dd-mm-yyyy: ").split("-")
    if (2022 - int(dob[2])) != int(age):
        dob = input("Wrong input. Please re-enter your date of birth in this format dd-mm-yyyy: ")

    genders = ["Male", "Female"]
    gender = input("Enter your gender: ").title()
    if gender not in genders:
        gender = input("Wrong input. Please re-enter your gender: ").title()

    statuses = ["Married", "Single", "Divorced"]
    m_status = input("Enter your marital status; Single, Married or Divorced: ").title()
    if m_status not in statuses:
        m_status = input("Wrong input. Please re-enter your marital status; Single, Married or Divorced: ")


    email = input("Enter your email: ").lower()
    if "@" not in email and ".com" not in email:
        email = input("Wrong input. One attempt left, please re-enter your email: ")
        if "@" not in email and ".com" not in email:
            print("Sorry, you have exceeded the number of attempts")
    with open("details.csv", "a") as file:
        headers = ["First_name", "Last_name", "Middle_name", "Age", "Occupation", "Date_of_Birth", "Gender", "Marital_Status", "E_mail"]
        handler = csv.DictWriter(file, fieldnames=headers)
        handler.writeheader()
        handler.writerow({"First_name": f_name, "Last_name": l_name, "Middle_name": m_name, "Age": age, "Occupation": occupation, "Date_of_Birth": dob, "Gender": gender, "Marital_Status": m_status, "E_mail": email})
elif response == 2:
    with open("details.csv", "r") as file:
        handler = csv.DictReader(file)
        search_term = input("Enter the search term: ")
        for row in handler:
            if search_term in row["First_name"] or search_term in row["Last_name"] or search_term in row["Middle_name"] or search_term in row["E_mail"]:
                print("You have found the info.")
            else:
                print("The info requested can not be found.")
