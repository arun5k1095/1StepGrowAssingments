#You are required to create a simple banking system where you can create bank accounts, deposit money,
#and withdraw money. Follow the instructions below to implement the system.

class BankAccount:
    account_number = ""
    account_holder = ""
    balance = 0.0

    def __init__(self,acc_num,acc_holder,bal):
        self.account_number = acc_num
        self.account_holder = acc_holder
        self.balance = bal

    def deposit(self,amount):
        self.balance = self.balance + amount


    def withdraw(self,amount):
        if self.balance > amount:
            self.balance = self.balance - amount
        else:
            print("Sufficient balance not available for withdrawing")

    def get_balance(self):
        return self.balance


b1 = BankAccount('AC12345','Meitheli',5500.65)
b2 = BankAccount("AC3456","Akshay",6000)
b1.deposit(2000)

print("Balance after deposit is: ", b1.get_balance())
b1.withdraw(3000)
print("Balance after withdrawal is: ", b1.get_balance())

b1.withdraw(5000)

#----------------------------------------------Not Working ---------------------------------------------#

class Bank():

    accounts = { }
    count = 0
    def create_account(self,acc_num,acc_holder):
        self.accounts.update({acc_num,acc_holder,'b'+ str(self.count + 1)})

    def find_account(self, acc_num):
        return self.accounts[acc_num]

    def deposit_to_account(self,account_number, amount):
        bank_object = self.find_account(account_number)
        bank_object.deposit(amount)

    def withdraw_from_account(self,account_number, amount):
        bank_object = self.find_account(account_number)
        bank_object.withdraw(amount)

    def get_account_balance(self, account_number):
        bank_object = self.find_account(account_number)
        return bank_object.get_balance()








