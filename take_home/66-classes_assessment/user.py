from wallet import Wallet
import random

class User(Wallet):

    def __init__(self, f_name, l_name):
        super().__init__()
        self.__f_name = f_name
        self.__l_name = l_name
        self.__pin = random.randint(1000,9999)

        User.all.append(self)

    def __eq__(self, other):
        return self._id == other._id and self.__pin == other.__pin

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.__f_name}', '{self.__l_name}', '{self._wallet_balance}', '{self._id}', '{self.__pin}')"

    @property
    # Property Decorator = Read-Only Attribute
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if len(value) > 10:
            raise Exception("The ID is too long!")
        if self._id == value:
            raise Exception("The ID is the same as before!")
        print("ID has been set!")
        self._id = value

    @property
    # Property Decorator = Read-Only Attribute
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, value):
        if self.__pin == value:
            raise Exception("The password is the same as before!")
        print("Pin has been set!")
        self.__pin = value
        

    # def __delattr__(self, _id: str):
    #     return super().__delattr__(_id)