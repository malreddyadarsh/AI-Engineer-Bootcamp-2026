# Safe Calculator

# Features:

# Addition.
# Subtraction.
# Multiplication.
# Division.
# Handles invalid input.
# Prevents division by zero.

def addition(a,b):
    print("Addition is :", a + b)

def substraction(a,b):
    print("Substraction is :",a-b)

def multiplication(a,b):
    print("Multiplication is :",a*b)

def division(a,b):
    try:
        result=a/b
        print("Division is:",result)
    except ZeroDivisionError:
        print("Cannot Divide By Zero")

def menu():
    print("\n\n========Safe Calculator========")
    print("1. Addition ")
    print("2. Substraction")
    print("3. Multiplication ")
    print("4. Division")
    print("5. Exit")

def get_numbers():
    while True:
        try:
            x = float(input("Enter first value: "))
            y = float(input("Enter second value: "))
            return x, y
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def main():
    while True:
        menu()
        choice=input("Enter your Choice :")
        
        if choice=="1":
            a,b=get_numbers()
            addition(a,b)
        elif choice=="2":
            a,b=get_numbers()
            substraction(a,b)
        elif choice=="3":
            a,b=get_numbers()
            multiplication(a,b)
        elif choice=="4":
            a,b=get_numbers()
            division(a,b)
        elif choice=="5":
            print("Thank Your For Choosing.")
            break
        else:
            print("Invalid option.")


main()