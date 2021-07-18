class Account:
    def __init__(self,title = None, balance=0):
        self.__title = title
        self.__balance = balance
    
    def getBalance(self):
        return self.__balance
    
    def deposit(self,amount):
        self.__balance += amount
    
    def withdrawal(self,amount):
        self.__balance -= amount

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0,interest_rate=0.0):
        super().__init__(title=title, balance=balance)
        self.__interest_rate = interest_rate
    
    def interestAmount(self):
        return (self.__interest_rate * self.getBalance())/100


account1 = Account("Mark",5000)
account1.deposit(8000)
account1.withdrawal(3000)
print("\n balance of account 1 =>",account1.getBalance())
account2 = SavingsAccount("Mark",5000,5)
account2.deposit(10000)
account2.withdrawal(2500)
print("\n balance of account 2 => ",account2.getBalance())
print("\n Interest Amount for account 2 => ",account2.interestAmount())





