# 1 Deposit. 2 Withdraw. 3 Check balance.4 Exit.

def deposit(balance):
    amount=int(input("Enter amount to deposit :"))

    if amount <= 0:
        print("Invalid option")
    else:
        balance+=amount
        print("$",amount," deposited successfully")
    return balance

def withdraw(balance):
    amount=int(input("Enter amount to withdraw :"))
    
    if amount <= 0:
        print("Invalid option")
    elif amount > balance:
        print("Insufficients Balance")
    else:
        balance-=amount
        print("$",amount,"withdrawl successful")
    return balance

def check_balance(balance):
    print(" Current Balance :",balance)
    return balance

def menu():
    print("\nBanking Details :")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Exit")

def main():
    balance=0
    while True:
        menu()
        choice=int(input("Enter above options :"))
        if choice==1:
            balance=deposit(balance)
        elif choice==2:
            balance=withdraw(balance)
        elif choice==3:
            balance=check_balance(balance)
        elif choice==4:
            print("Thank you for choosing ")
            break
        else:
            print("Invalid option")

main()
    