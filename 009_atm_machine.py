# create a program that simulates a basic ATM machine. The user should be able to check their balance, deposit and withdraw money. Use functions to handle each operation

class ATM():
    def __init__(self, balance):
        self._balance = balance

    def deposit(self):
        amount_deposit = float(input("Type the amount you would like to deposit? "))
        if amount_deposit > 0:
            self._balance += amount_deposit
            return f"{amount_deposit}e was deposit into your account. \n"
        else: 
            return f"Error, invalid operation. \n"
        # return self.money

    def withdraw(self):
        transaction = False
        while not transaction:
            withdraw_money = float(input("Type the amount you would you like to withdraw? "))
            if withdraw_money > self._balance:
                print(f"Operation failed, Your credential are not sufficient for this transaction. Please select a lower amount.")
            else:
                self._balance -= withdraw_money
                transaction = True
                return f"{withdraw_money}e was withdrawn from your account. \n"

    def check_balance(self):
        return f"You have a balance of {self._balance}euros in your account. \n"
        

Marc = ATM(100)

print(Marc.deposit())

print(Marc.deposit())

print(Marc.check_balance())
print(Marc.withdraw())
print(Marc.deposit())

print(Marc.check_balance())





# better with print statement or call the function ?
# what are the different impacts ?

# surely better calling the function and use print statement instead.
# just would like to figure  a way so that balance cannot be modified..