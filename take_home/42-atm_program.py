# Write a program that simulates a bank USSD application.
# A user interacting with your program should be able to
# a) Check balance
# b) Transfer cash
# c) Load airtime
# d) Load data
# e) Generate a four-digit otp
# Note: All action must authorize with a pin.

# The user must set a transaction pin initially

import random

account_balance = 23045.56
phone_balance = 374.56
data_balance = 30.87
data_balance_two = 1.38
phone_balance_two = 0.95
ussd = "*121#"
pin = "1234"
input_ussd = input("Enter USSD: ")

if input_ussd != ussd:
    print("Connection problem or invalid MMI code.")
else:
    print("Welcome to One Bank USSD Banking. Please note that #5.00 network charge will be applied to your bank account for services on this channel. \n1. Accept \n2. Cancel")
    response = int(input("Enter response: "))
    if response == 2:
        print("The service has ended. Thank you.")
    elif response == 1:
        print("1. Airtime-Self\n2. Airtime-Others\n3. Data\n4. Transfer-OneBank\n5. Transfer-Others\n6. Check balance\n7. Generate Token\n8. Change PIN")
        account_balance -= 5
        response = int(input("Enter response: "))
        if response == 1:
            pin_input = input("Enter your pin: ")
            if pin_input == pin:
                top_up = int(input("Please enter amount: "))
                phone_balance += top_up
                account_balance -= top_up
                print("Processed successfully. Your mobile number has been topped up.")
                print(f"Your new account balance is N{account_balance}.")
            else:
                print("Incorrect details entered. Please try again later.")
        elif response == 2:
            phone_number_two = input("Enter 3rd party mobile number: ")
            pin_input = input("Enter your pin: ")
            if pin_input == pin:
                top_up = int(input("Please enter amount: "))
                phone_balance_two += top_up
                account_balance -= top_up
                print(f"Processed successfully. {phone_number_two} has been topped up.")
                print(f"Your new account balance is N{account_balance}.")
            else:
                print("Incorrect details entered. Please try again later.")
        elif response == 3:
            print("1. Self\n2. 3rd party number")
            response = int(input("Enter response: "))
            if response == 1:
                pin_input = input("Enter your pin: ")
                if pin_input == pin:
                    print("1. 50MB for N100\n2. 100MB for N200\n3. 200MB for N400\n4. 500MB for N750\n5. 1GB for N1000")
                    response = int(input("Enter response: "))
                    if response == 1:
                        data_top_up = 50
                        account_balance -= 100
                    elif response == 2:
                        data_top_up = 100
                        account_balance -= 200
                    elif response == 3:
                        data_top_up = 200
                        account_balance -= 400
                    elif response == 4:
                        data_top_up = 500
                        account_balance -= 750
                    elif response == 5:
                        data_top_up = 1024
                        account_balance -= 1000
                    data_balance += data_top_up
                    print(f"Processed successfully. You have purchased {data_top_up}MB.")
                    print(f"Your new account balance is N{account_balance}.")
                else:
                    print("Incorrect details entered. Please try again later.")
            elif response == 2:
                phone_number_two = input("Enter 3rd party mobile number: ")
                pin_input = input("Enter your pin: ")
                if pin_input == pin:
                    print("1. 50MB for N100\n2. 100MB for N200\n3. 200MB for N400\n4. 500MB for N750\n5. 1GB for N1000")
                    response = int(input("Enter response: "))
                    if response == 1:
                        data_top_up = 50
                        account_balance -= 100
                    elif response == 2:
                        data_top_up = 100
                        account_balance -= 200
                    elif response == 3:
                        data_top_up = 200
                        account_balance -= 400
                    elif response == 4:
                        data_top_up = 500
                        account_balance -= 750
                    elif response == 5:
                        data_top_up = 1024
                        account_balance -= 1000
                    data_balance_two += data_top_up
                    print(f"Processed successfully. You have sent {data_top_up}MB to {phone_number_two}.")
                    print(f"Your new account balance is N{account_balance}.")
                else:
                    print("Incorrect details entered. Please try again later.")
        elif response == 4:
            trsf_amount = int(input("Please enter amount more than N50: "))
            trsf_account = input("Please enter account number: ")
            pin_input = input("Enter your pin: ")
            if pin_input == pin and trsf_amount > 50 and (len(trsf_account)) == 10:
                print(f"You have sent N{trsf_amount} to {trsf_account}, One Bank successfully.")
                account_balance -= trsf_amount
                print(f"Your new account balance is N{account_balance}.")
            else:
                print("Incorrect details entered. Please try again later.")
        elif response == 5:
            print("1. Wema Bank\n2. Sterling Bank\n3. GTB\n4. First Bank\n5. Fidelity Bank\n6. Kuda Bank")
            response = int(input("Enter response: "))
            if response == 1:
                trsf_amount = int(input("Please enter amount more than N50: "))
                trsf_account = input("Please enter account number: ")
            elif response == 2:
                trsf_amount = int(input("Please enter amount more than N50: "))
                trsf_account = input("Please enter account number: ")
            elif response == 3:
                trsf_amount = int(input("Please enter amount more than N50: "))
                trsf_account = input("Please enter account number: ")
            elif response == 4:
                trsf_amount = int(input("Please enter amount more than N50: "))
                trsf_account = input("Please enter account number: ")
            elif response == 5:
                trsf_amount = int(input("Please enter amount more than N50: "))
                trsf_account = input("Please enter account number: ")
            elif response == 6:
                trsf_amount = int(input("Please enter amount more than N50: "))
                trsf_account = input("Please enter account number: ")
            pin_input = input("Enter your pin: ")
            if pin_input == pin and trsf_amount > 50 and (len(str(trsf_account))) == 10:
                print(f"You have sent N{trsf_amount} to {trsf_account}, Wema Bank successfully.")
                account_balance -= trsf_amount
                print(f"Your new account balance is N{account_balance}.")
            else:
                print("Incorrect details entered. Please try again later.")
        elif response == 6:
            print(f"Your account balance is N{account_balance}.")
        elif response == 7:
            token = random.randint(1000,9999)
            print(f"Your Token/4-digit OTP is {token}")
        elif response == 8:
            old_pin = input("Please enter your old PIN: ")
            if old_pin == pin:
                pin = input("Please enter your new PIN: ")
                print(f"Your new PIN is {pin}")
    else:
        print("Connection problem or invalid MMI code.")