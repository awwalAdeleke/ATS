import random

me = {"account_balance": 2345662.58}
they = {}

def write_pin():
    return input("Set your pin: ")

def transfer_airtime(person:dict, amount:int):
    person["airtime_balance"] += amount
    me["account_balance"] -= amount

def transfer_data(person:dict, data:int, amount:int):
    person["data_balance"] += data
    me["account_balance"] -= amount

def transfer_cash(person:dict, amount:int):
    person["account_balance"] += amount
    me["account_balance"] -= amount

def generate_otp():
    return random.randint(1000,9999)

def check_balance():
    return me["account_balance"]

def input_pin():
    pin_entry = input("Please enter your pin: ")
    if pin_entry == pin:
        return True
    else:
        return False

# def response(start:int, finish:int):
#     for i in range(start, finish + 1):
#         return responses[i]

def ussd():
    pin = write_pin()
    print("Welcome to One Bank USSD Banking. Please note that #5.00 network charge will be applied to your bank account for services on this channel. \n1. Accept \n2. Cancel")
    response = int(input("Enter response: "))
    if response == 2:
        print("The service has ended. Thank you.")
    elif response == 1:
        print("1. Airtime-Self\n2. Airtime-Others\n3. Data\n4. Transfer-OneBank\n5. Transfer-Others\n6. Check balance\n7. Generate Token\n8. Change PIN")
        account_balance -= 5
        response = int(input("Enter response: "))
        if response == 1:
            my_

