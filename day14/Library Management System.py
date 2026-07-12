# Library Record System

# Features:

# Save books.
# Borrow book.
# Return book.
# Display available books.
# Store everything in a file.

library="Library.txt"

def save_book():
    name=input("Enter Book Name :")
    available= True
    with open(library,"a") as file:
        file.write(f"{name},{available}\n")
    print("Book Added Successfully.")

def borrow_book():
    b_name=input("Enter Book Name to borrow :")

    borrow=False

    with open(library,"r") as file:
        books=file.readlines()

    with open(library,"w") as file:
        for book in books:
            name,available=book.strip().split(",")
            if name==b_name and available=="True":
                print("Book is borrowed.")
                available=False
                borrow=True
                file.write(f"{name},{available}\n" )
            else:
                file.write(book)
    if not borrow:
        print("Book is Not Available to Borrow")

def return_book():
    r_name=input("Enter Book Name to return :")

    borrow=False

    with open(library,"r") as file:
        books=file.readlines()

    with open(library,"w") as file:
        for book in books:
            name,available=book.strip().split(",")
            if name==r_name and available=="False":
                print("Book is Returned.")
                available=True
                borrow=True
                file.write(f"{name},{available}\n" )
            else:
                file.write(book)
    if not borrow:
        print("Book is Not Available to Return.")

# Display available books
def display_available():
    found = False
    with open(library,"r") as file:
        books=file.readlines()
    print("\n Printing Available Books :")
    for book in books:
        name,available=book.strip().split(",")
        if available== "True":
            print("------------")
            print("Book Name :",name)
            print("Book Availability :",available)
            found =True
    if not found :
        print("Books Not Available fo Borrowing.")


def menu():
    print("\n=====Library Management System=====")
    print("1. Save books")  
    print("2. Borrow book")
    print("3. Return book")      
    print("4. Display available books")
    print("5. Exit")

while True:
    menu()
    choice=input("Enter your choice :")
    if choice=="1":
        save_book()
    elif choice=="2":
        borrow_book()
    elif choice=="3":
        return_book()
    elif choice=="4":
       display_available() 
    elif choice=="5":
        print("Thank You for Choosing")
        break
    else:
        print("Invalid Option.")