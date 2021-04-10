class Account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        print('Account created for ' + self.name)

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print('The amount must be grater than zero and more then account balance')
        self.show_balance()

    def show_balance(self):
        print(f"balance is {self.balance}")


if __name__ == '__main__':
    ashu = Account('Ashu',0)
    ashu.show_balance()

    ashu.deposit(1000)
    # ashu.show_balance()
    ashu.withdraw(500)
    # ashu.show_balance()
    ashu.withdraw(2000)
    ashu.deposit(5555555555555555)
    










