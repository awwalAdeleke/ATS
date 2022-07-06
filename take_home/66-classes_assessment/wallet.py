import random
import string

class Wallet:

    all = []
    log = []
    letters = string.ascii_uppercase
    numbers = string.digits

    def __init__(self, wallet_balance = 0):
        assert wallet_balance >= 0, f"Wallet balance is not greater than or equal to zero!"

        self.__id = "".join(random.sample(Wallet.letters, 4) + random.sample(Wallet.numbers, 6))
        self._wallet_balance = wallet_balance



    def fund_wallet(self):
        amount = int(input(f"{self.__id}, Please input the amount you are adding to the wallet: "))
        # Validation
        if amount > 0:
            self._wallet_balance += amount
            Wallet.log.append(f"{self.__id} just funded his wallet with #{amount}!")
            return f"Your new wallet balance is {self._wallet_balance}!"
        return "The amount is invalid!"

    def withdraw_from_wallet(self):
        amount = int(input(f"{self.__id}, Please input the amount you are withdrawing from the wallet: "))
        # Validation
        if amount > self._wallet_balance:
            return "The amount is over the wallet balance!"
        self._wallet_balance -= amount
        Wallet.log.append(f"{self.__id} just withdrew #{amount} from his wallet!")
        return f"Your new wallet balance is {self._wallet_balance}!"





