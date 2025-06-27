class Person :
    def __init__(self):
        self.name = None
        self.age = None
        self.__balance = 10000
    @property
    def balance(self):
        return self.__balance
    @balance.
obj=Person()
print(obj.balance)
