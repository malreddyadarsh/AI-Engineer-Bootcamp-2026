#Library Management System

#Features:

# Add book.
# Borrow book.
# Return book.
# Search by title.
# Display all books.

books={}
def add_book(books):
    name=input("Enter Book name :")
    if name in books:
        print("Book Already Exists.")
        return
    books[name]={
        "borrow":False
    }
    print("Booked Added Successfully.")

def borrow_book(books):
    name=input("Enter Book Name to borrow :")
    if name not in books:
        print("No Book Found.")
        return
    for name,details in books.items():
        if details["borrow"]==True:
            print("Book is Already Borrowed !")
            return
        else:
            print("Book is marked as Borrowed !")
            details["borrow"]=True
            return
        
def return_book(books):
    name=input("Enter book name to return :")
    for names,details in books.items():
        if names==name and details["borrow"] != False:
            print("Book Returned Successfully !")
            details["borrow"]=False
            return
        else:
            print("Book Not Found to be Returned !")
            return
        
def search_book(books):
    name=input("Enter Book Name to Search :")

    if name in books:
        print("Book Found ")
        if books[name]["borrow"]==False:
            print("Book is Available to borrow ")
            return
        else:
            print("Book is Not Available to borrow ")
            return
    else:
        print("Book Not Found for Searching ")   

def display(books):
    print("\n===Dispalying All Books===")
    for book,details in books.items():
        print("Book name :",book)
        print("Book Borrowed :",details["borrow"])

while True:

    print("\n===== Contact Book =====")
    print("1. Add book")
    print("2. Borrow book")
    print("3. Return book")
    print("4. Search by title ")
    print("5.Display all books ")
    print("6. Exit")

    choice =int(input("Enter your choice: "))
    if choice== 1:
        add_book(books)
    elif choice== 2:
        borrow_book(books)
    elif choice== 3:
        return_book(books)
    elif choice== 4:
        search_book(books)
    elif choice==5:
        display(books)
    elif choice==6:
        print("Thank you for choosing !")
        break
    else:
        print("Invalid Option")