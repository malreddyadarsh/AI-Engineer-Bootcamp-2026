# Library Management System
# 
# Features:
# 
# Add books.
# Borrow books.
# Return books.
# Search books.

class Library:
    def __init__(self,books):
        self.books=books

    def add_book(self,name,available):
        book={
            "name":name,
            "available":available
        }
        self.books.append(book)
        print("New Book Added Successfully.")


    def borrow_book(self,name):
        for book in self.books:
            if book["name"]==name and book["available"]=="True":
                print("\nBook is Borrowed Successfully.")
                book["available"]="False"
                return
        print("\nBook is Not Available to Borrow.")

    def return_book(self,name):
        for book in self.books:
            if book["name"]==name and book["available"]=="False":
                print("\nBook is Returned Successfully.")
                book["available"]="True"
                return
        print("\nBook is Not Available To Return. ")

    def search_book(self,name):
        for book in self.books:
            if book["name"]==name:
                print("\nBook Found Successfully.")
                print("Book Name      :",book["name"])
                print("Book Available :",book["available"])
                return
        print("\nBook Not Available to Search.")

    def display(self):
        if len(self.books)==0:
            print("No Books Found.")
        else:
            print("\n=====Displaying All Books=====")
            for book in self.books:
                print("Book Name         :",book["name"])
                print("Book Available is :",book["available"])

def menu():
    print("\n=====Library Management System=====\n")
    print("1. Add Books")
    print("2. Borrow Books")
    print("3. Return Books ")
    print("4. Search Books ")
    print("5. Display All Books")
    print("6. Exit ")

def main():
    books=[]
    book=Library(books)
    while True:
        menu()
        choice=input("Enter your Choice :")
        if choice=="1":
            name=input("Enter Book Name :")
            available=input("Enter True or False only :")
            book.add_book(name,available)
        elif choice=="2":
            name=input("Enter Book Name To Borrow :")
            book.borrow_book(name)
        elif choice=="3":
            name=input("Enter Book Name to Return :")
            book.return_book(name)
        elif choice=="4":
            name=input("Enter Book Name to Serach :")
            book.search_book(name)
        elif choice=="5":
            book.display()
        elif choice=="6":
            print("Thank You For Choosing.")
            break
        else:
            print("Invalid Option.")
 
main()