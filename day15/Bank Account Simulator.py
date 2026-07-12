# Bank Account Simulator

# Features:

# Deposit.
# Withdraw.
# Prevent overdrawing.
# Validate numeric input.
# Show appropriate messages instead of crashing.

def deposit(bank_balance):
    try:
        balance=float(input("Enter Amount to Deposit in to Bank Account :"))
        if balance<0:
            raise ValueError("The Amount should be greater than 0 to deposit into bank.")
        bank_balance=bank_balance + balance
        print("Amount Deposited Successfully.")
        return bank_balance
    except ValueError as e:
        print("Error : ",e)
        return bank_balance

def withdraw(bank_balance):
    try:
        withd_balance=float(input("Enter Amount to Withdraw From Bank Account :"))
        if withd_balance>bank_balance :
            raise ValueError("Insufficient Funds.")
        if withd_balance<0:
            raise ValueError("Amount should be greater than 0.")
        bank_balance-=withd_balance
        print("Withdraw is Successfully Done.")
        return bank_balance
    except ValueError as e:
        print("Error :",e)
        return bank_balance


def display(bank_balance):
    print("Bank Balance is :",bank_balance)  

def menu():
    print("\n\n======Bank Account Simulator======")
    print("1. Deposit ")
    print("2. Withdraw")
    print("3. Bank Balance ")
    print("4. Exit")

def main():
    bank_balance=0
    while True:
        menu()
        choice=input("Enter Your Choice :")
        if choice=="1":
            bank_balance=deposit(bank_balance)
        elif choice=="2":
            bank_balance=withdraw(bank_balance)
        elif choice=="3":
           display(bank_balance)
        elif choice=="4":
            print("Thank You For Choosing.")
            break
        else:
            print("Invalid Option.")
          
main()