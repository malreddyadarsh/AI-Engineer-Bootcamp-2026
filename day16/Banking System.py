# Banking System

# Features:

# Create account.
# Deposit.
# Withdraw.
# Check balance.
# Transaction history (basic).

class Account:
    def __init__(self,balance,transaction):
        self.balance=balance
        self.transaction=transaction
    
    def deposit(self,deposit):
        if deposit<=0:
            print("\nDeposit Must Be Greater Than 0.\n")
        else:
            self.balance+=deposit
            print("\nDeposit Done Successfully.\n")
            self.transaction.append(("Deposited",deposit))
           
    
    def withdraw(self,withdraw):
        if withdraw<=0:
            print("\nWithdraw Must Be Greater than Zero.\n")
        elif withdraw>self.balance:
            print("\nInsufficient Balance.\n")
        else:
            self.balance-=withdraw
            print("\nWithdraw Done Successfully.\n")
            self.transaction.append(("Withdrawal",withdraw))

    def check_balance(self):
        print("Balance in your Account :",self.balance)

    def transactions(self):
        print("\n====DISPLAYING TRANSACTIONS====\n")
        if not self.transaction:
            print("No transactions found.")
        else:
            for t in self.transaction:
                print(f"{t[0]} : {t[1]}\n")

    

def menu():
    print("\n======Banking System=======\n")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transactions ")
    print("5. Exit ")


def main():
    print("\nOpening Bank Account \n")
    balance=0
    transaction=[]
    bank=Account(balance,transaction)
    while True:
        menu()
        choice=input("Enter your Choice :")
        if choice=="1":
            deposit=int(input("Enter Deposit Amount :"))
            bank.deposit(deposit)
        elif choice=="2":
            withdraw=int(input("Enter Withdraw Amount :"))
            bank.withdraw(withdraw)
        elif choice=="3":
            bank.check_balance()
        elif choice=="4":
            bank.transactions()
        elif choice=="5":
            print("\nThank you for choosing !")
            break
        else:
            print("Invalid Option")

main()