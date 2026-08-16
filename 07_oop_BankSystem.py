class BalanceException(Exception): 
    pass

class BankAccount:
    def __init__(self,initial_amount , account_name):
        self.balance=initial_amount
        self.name=account_name
        print(f"\nAccount '{self.name}' created. \n Balnce= ${self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self,amount):
        self.balance= self.balance + amount
        print(f"\nDepist complete.")
        self.get_balance()

    def viable_transaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry account '{self.name}' only has a balance of ${self.balance:.2f}")


    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance=self.balance - amount
            print("\nWithdraw compelet.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw intrrupted: {error}")


    def transfer(self,amount,account):
        try:
            print("\n**********\n\nBeginning transfer... 🚀")
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete! ✅")
        except BalanceException as error:
            print(f"\nTransfer intrrupted. ❌ {error}")

class IntrestRewardAcc(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance +(amount * 1.05)
        print(f"\nDeposit complete.")
        self.get_balance()


class SavingAcct(IntrestRewardAcc):
    def __init__(self, initial_amount, account_name):
        super().__init__(initial_amount, account_name)
        self.fee= 5

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance=self.balance - (amount + self.fee)
            print(f"\nWihdraw Complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw intrrupted: {error}")



Dave= BankAccount(1000,"Dave")
Sara= BankAccount(2000,"Sara")
Blaze=SavingAcct(3000,"Blaze")

Blaze.deposit(200)
Blaze.transfer(2000,Sara)
