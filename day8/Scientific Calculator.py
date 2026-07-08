# Features
# Add
# Subtract
# Multiply
# Divide
# Square Root
# Power
# Factorial
# Percentage

def addition(a,b):
    return (a+b)

def subtract(a,b):
    return a-b

def multipy(a,b):
    return a*b

def divide(a,b):
    return a/b

def square_root(a):
    import math
    return math.sqrt(a)

def power_num(a,b):
    import math
    return math.pow(a,b)

def factorial_num(a):
    import math
    return math.factorial(a)

def percentage(a,b):
    return (a/b)*100


def menu():
    print("\nCalculator Features ")
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Division")
    print("5. Square root")
    print("6. Power ")
    print("7. Factorial ")
    print("8. Percentage")
    print("9. Exit")

def main():
    while True:
        menu()
        choice=int(input("Enter your choice :"))
        if choice==1:
            a=int(input("Enter value of a :"))
            b=int(input("Enter value of b :"))
            print("Addition is :",addition(a,b))
        elif choice==2:
            a=int(input("Enter value of a :"))
            b=int(input("Enter value of b :"))
            print("Subtraction is :",subtract(a,b))
        elif choice==3:
            a=int(input("Enter value of a :"))
            b=int(input("Enter value of b :"))
            print("Multiplication is :",multipy(a,b))
        elif choice==4:
            a=int(input("Enter value of a :"))
            b=int(input("Enter value of b :"))
            print("Division is :",divide(a,b))
        elif choice==5:
            a=int(input("Enter value of a :"))
            print("Square Root is :",square_root(a))
        elif choice==6:
            a=int(input("Enter value  :"))
            b=int(input("Enter Exponent :"))
            print("Power is :",pow(a,b))
        elif choice==7:
            a=int(input("Enter value of a :"))
            print("Factorial is :",factorial_num(a))
        elif choice==8:
            a=int(input("Enter value of a :"))
            b=int(input("Enter value of b :"))
            print("Percentage is :",percentage(a,b),"%")
        elif choice==9:
            print("Thank you for choosing !")
            break
        else:
            print("Invalid option")

main()