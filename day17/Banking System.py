# Banking System (Advanced)
# 
# Features:
# 
# Create account.
# Deposit.
# Withdraw.
# Transaction history.
# Private balance.
# Validation.
# 
# Concepts: Encapsulation + Classes.

class BankAccount:
    def __init__(self,balance,transactions):
        self.__balance=balance
        self.__transactions=transactions
    
    def deposit(self,amount):
        if amount < 0:
            print("Amount Must Be Greater Than Zero.")
        else:
            self.__balance+=amount
            print("Deposit Done Successfully.")
            self.__transactions.append(("Deposited",amount))
    
    def withdraw(self,amount):
        if amount < 0:
            print("Amount Must Be Greater Than Zero.")
        elif amount>self.__balance:
            print("Insufficient Balance.")
        else:
            self.__balance-=amount
            print("Withdraw Done Successfully.")
            self.__transactions.append(("Withdraw",amount))

    def transactions_history(self):
        if len(self.__transactions)==0:
            print("No Transactions Found.")
        else:
            for transactions in self.__transactions:
                print(transactions)

    def check_balance(self):
        print("Balance :",self.__balance)

def menu():
    print("\n\n======Banking System======")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transactions History")
    print("4. Check Balance")
    print("5. Exit ")

def main():
    transactions=[]
    balance=0
    bank=BankAccount(balance,transactions)
    print("Opening New Bank Account !")
    while True:
        menu()
        choice=input("Enter your Choice :")
        if choice=="1":
            amount=int(input("Enter Amount To Deposit :"))
            bank.deposit(amount)
        elif choice=="2":
            amount=int(input("Enter Amount To Withdraw :"))
            bank.withdraw(amount)
        elif choice=="3":
            bank.transactions_history()
        elif choice=="4":
            bank.check_balance()
        elif choice=="5":
            print("Thank You For Choosing.")
            break
        else:
            print("Invalid Option.")

main()
