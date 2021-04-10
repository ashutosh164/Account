import datetime
import pytz


class Account:

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print('Account created for ' + self.name)

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()),amount))

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print('The amount must be grater than zero and more then account balance')
        self.show_balance()

    def show_balance(self):
        print(f"balance is {self.balance}")

    def show_transaction(self):
        for date, amount in self.transaction_list:
            if amount >= 0:
                tran_type = 'deposited'
            else:
                tran_type = 'withdrawn'
                amount *= -1
            print(f"{amount} {tran_type} on {date} (local time was {date.astimezone()})")
            # print("{} {} on {} (local time was {})".format(amount,tran_type,date,date.astimeone()))


if __name__ == '__main__':
    ashu = Account('Ashu',0)
    ashu.show_balance()

    ashu.deposit(1000)
    ashu.withdraw(100)
    ashu.deposit(2)
    ashu.show_transaction()











