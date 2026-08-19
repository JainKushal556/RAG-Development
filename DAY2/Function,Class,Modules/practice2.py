# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self):
        self.account_no = 0
        self.balance = 1000.00
        print(".....Account Created.....\nInitial Balance: 1000")
    def debit(self,amount):
        if(self.balance > amount+500):
            self.balance -= amount
            return True
        else:
            return False
    def credit(self,amount):
        self.balance += amount
        return True
    def get_balance(self):
        return self.balance
    def start(user):
        while True:
            print("\n..................................\nDebit: 1      Credit: 2")
            choice = int(input("Enter Ur Choice: "))
            if(choice ==1):
                amount = float(input("Enter Amount: "))
                if user.debit(amount):
                    print(amount,"Debited.\nCurrent Balance: ",f"{user.get_balance():.2f}")
                else:
                    print("Insufficient Balance")
            elif choice ==2:
                amount = float(input("Enter Amount: "))
                if user.credit(amount):
                    print(amount,"Credited.\nCurrent Balance: ",f"{user.get_balance():.2f}")
            else:
                print("Invalid Input..\nRestrat Program")
                break 


    
user = Account()
user.start()


