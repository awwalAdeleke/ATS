from transactions import Transactions
from user import User
from wallet import Wallet

if __name__ == '__main__':
    # To create a user account
    user1 = User("Awwal", "Adeleke")
    user2 = User("Lukman", "Abisoye")
    # print(user1)
    # print(user2)

    # To fund the user wallet
    # user1.fund_wallet()

    # user2.fund_wallet()


    # To withdraw from a user wallet
    # user1.withdraw_from_wallet()
    # user2.withdraw_from_wallet()

    # To get the transactions log
    # trans = Transactions()
    # print(trans.transaction_log())

    # To check if the methods have been effected
    # print(user1)
    # print(user2)
    # user1.id = 51
    print(user1.id)
    

    # To delete a user account
    # del user1

    #To check again if the methods have been effected
    # print(user1)