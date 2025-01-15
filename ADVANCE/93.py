class Account:
    def __init__(self, balance=0):
        self.__balance = balance 

   
    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative.")

account = Account(1000)
print(f"Initial Balance: {account.get_balance()}")

account.set_balance(1500)
print(f"Updated Balance: {account.get_balance()}")

account.set_balance(-500)  
