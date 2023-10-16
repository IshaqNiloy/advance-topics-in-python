'''
Simple implementation of Encapsulation
'''


class BankAccount:
    def __init__(self, balance):
        super(BankAccount, self).__init__()
        # private attribute
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print(f'Amount must be greater than 0 (zero).')

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print(f'You do not have sufficient balance. Current Balance: {self.__balance}')

    def get_balance(self):
        return self.__balance


if __name__ == '__main__':
    customer_1 = BankAccount(500)
    customer_1.deposit(0)
    customer_1.withdraw(600)

    current_balance = customer_1.get_balance()

    print(f'Current balance is {current_balance}')
