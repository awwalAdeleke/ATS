from wallet import Wallet


class Transactions(Wallet):
    def __init__(self, wallet_balance=0):
        super().__init__(wallet_balance)

    def transaction_log(self):
        return Wallet.log

