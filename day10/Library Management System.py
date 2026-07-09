def add_book(library):
    name=input("Enter book name :").lower()

    for book in library:
        if book["name"]==name:
            print("Book already exists. ")
            return 
    library.append({
        "name":name,
        "available": True
    })
    print("Book added Successfully.")
    return library

def borrow_book(library):
    name=input("Enter book name to borrow :").lower()

    for book in library:
        if book['name']==name:
            if book["available"]==True:
                print("Book Borrowed Successfully.")
                book["available"]=False
                return library
            else:
                print("Print Book already borrowed.")
    print("Book not found.")

def return_book(library):
    name=input("Enter name of the book to return :").lower()

    for book in library:
        if book["name"]==name:
            if book["available"]==False:
                print("Book returned successfully")
                book["available"]=True
                return library
            else:
                print("Book Not borrowed.")
    print("Book not Found.")

def search_book(library):
    name=input("Enter book name to search :").lower()
    for book in library:
        if book["name"]==name:
            print("Book Found Successfully.")
            print("Availability of the book :",book['available'])
            return
    print("Book Not Found.")

def display_all(library):
    print(library)

def menu():
    print("\n \n=====Library Management System=====")
    print("1. Add book")
    print("2. Borrow book")
    print("3. Return book")
    print("4. Search book")
    print("5. Display all books ")
    print("6. Exit ")

def main():
    library=[]

    while True:
        menu()
        ch=int(input("Enter your choice :"))
        if ch==1:
            add_book(library)
        elif ch==2:
            borrow_book(library)
        elif ch==3:
            return_book(library)
        elif ch==4:
            search_book(library)
        elif ch==5:
            display_all(library)
        elif ch==6:
            print("Thank you for choosing !")
            break
        else:
            print("Invalid Option. ")

main()
