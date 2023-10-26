class BankAccount:
    def __init__(self, balance):
        super(BankAccount, self).__init__()
        self.__balance = balance  # name mangling / This is how you define private attribute in python

    def _deposit(self, amount):  # protected method / The same thing can be applied to class as well
        if amount > 0:
            self.__balance += amount
        else:
            print(f'amount must be greater than 0. balance: {self.__balance}')

        return self.__balance

    def _withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        elif amount > self.__balance:
            print(f'amount exceeds your current balance. balance: {self.__balance}')
        elif amount < 0:
            print(f'amount must be greater than 0. balance: {self.__balance}')

        return self.__balance

    def _print(self):
        print(f'current account balance: {self.__balance}')


if '__main__' == __name__:
    customer1 = BankAccount(500)
    customer2 = BankAccount(200)

    current_balance = customer1._deposit(500)
    customer1._print()
    print(customer1._BankAccount__balance)  # This is how you access a private attribute of a class.
    # But it is not recommended to access the private attribute directly.
    # That is why the concept of name mangling comes in.
    # We should use getter/ setter in this regard.

