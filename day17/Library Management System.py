class LibraryItem:
    def __init__(self, item_id, title, author):
        self.item_id = item_id
        self.title = title
        self.author = author
        self.__available = True

    def borrow(self):
        if self.__available:
            self.__available = False
            print(f'"{self.title}" has been borrowed successfully.')
        else:
            print(f'"{self.title}" is currently unavailable.')

    def return_item(self):
        if not self.__available:
            self.__available = True
            print(f'"{self.title}" has been returned successfully.')
        else:
            print(f'"{self.title}" was not borrowed.')

    def is_available(self):
        return self.__available

    def display_details(self):
        status = "Available" if self.__available else "Borrowed"
        print(f"ID        : {self.item_id}")
        print(f"Title     : {self.title}")
        print(f"Author    : {self.author}")
        print(f"Status    : {status}")


class Book(LibraryItem):
    def __init__(self, item_id, title, author, genre, pages):
        super().__init__(item_id, title, author)
        self.genre = genre
        self.pages = pages

    def display_details(self):
        print("\n===== BOOK =====")
        super().display_details()
        print(f"Genre     : {self.genre}")
        print(f"Pages     : {self.pages}")


class Magazine(LibraryItem):
    def __init__(self, item_id, title, author, issue):
        super().__init__(item_id, title, author)
        self.issue = issue

    def display_details(self):
        print("\n===== MAGAZINE =====")
        super().display_details()
        print(f"Issue No. : {self.issue}")


class DVD(LibraryItem):
    def __init__(self, item_id, title, author, duration):
        super().__init__(item_id, title, author)
        self.duration = duration

    def display_details(self):
        print("\n===== DVD =====")
        super().display_details()
        print(f"Duration  : {self.duration} minutes")


class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print("Item added successfully.")

    def display_all_items(self):
        if not self.items:
            print("Library is empty.")
            return

        for item in self.items:
            item.display_details()
            print("-" * 40)

    def search_item(self, keyword):
        found = False

        for item in self.items:
            if (str(item.item_id) == keyword or
                item.title.lower() == keyword.lower() or
                item.author.lower() == keyword.lower()):
                item.display_details()
                found = True

        if not found:
            print("Item not found.")

    def borrow_item(self, item_id):
        for item in self.items:
            if str(item.item_id) == str(item_id):
                item.borrow()
                return

        print("Item not found.")

    def return_item(self, item_id):
        for item in self.items:
            if str(item.item_id) == str(item_id):
                item.return_item()
                return

        print("Item not found.")


def menu():
    print("\n====== LIBRARY MANAGEMENT SYSTEM ======")
    print("1. Add Book")
    print("2. Add Magazine")
    print("3. Add DVD")
    print("4. Display All Items")
    print("5. Search Item")
    print("6. Borrow Item")
    print("7. Return Item")
    print("8. Exit")


def main():
    library = Library()

    while True:
        menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            item_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            genre = input("Enter Genre: ")
            pages = int(input("Enter Number of Pages: "))

            book = Book(item_id, title, author, genre, pages)
            library.add_item(book)

        elif choice == "2":
            item_id = input("Enter Magazine ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            issue = input("Enter Issue Number: ")

            magazine = Magazine(item_id, title, author, issue)
            library.add_item(magazine)

        elif choice == "3":
            item_id = input("Enter DVD ID: ")
            title = input("Enter Title: ")
            author = input("Enter Director/Author: ")
            duration = int(input("Enter Duration (minutes): "))

            dvd = DVD(item_id, title, author, duration)
            library.add_item(dvd)

        elif choice == "4":
            library.display_all_items()

        elif choice == "5":
            keyword = input("Enter ID, Title, or Author: ")
            library.search_item(keyword)

        elif choice == "6":
            item_id = input("Enter Item ID to Borrow: ")
            library.borrow_item(item_id)

        elif choice == "7":
            item_id = input("Enter Item ID to Return: ")
            library.return_item(item_id)

        elif choice == "8":
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


main()