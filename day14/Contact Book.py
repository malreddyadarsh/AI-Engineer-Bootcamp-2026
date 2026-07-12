# Contact Book (File Version)

# Features:

# Save contacts to a file.
# Read contacts.
# Search contacts.
# Delete contacts.

contacts_file="Contacts.txt"

def save_contact():
    name=input("Enter contact name :")
    number=input("Enter Mobile Number :")

    with open(contacts_file,"a") as file:
        file.write(f"{name},{number}\n")
    print("\nContact Added Successfully.")

def read_contacts():
    print("\nContact Lists is :")

    with open(contacts_file,"r") as file:
        contact=file.read()
    print(contact)

def search_contact():
    s_name = input("Enter Name to Search: ")

    found = False

    with open(contacts_file, "r") as file:
        for contact in file:
            name, number = contact.strip().split(",")

            if name.lower() == s_name.lower():
                print("Contact Found Successfully.")
                print(f"Name   : {name}")
                print(f"Number : {number}")
                found = True
                break

    if not found:
        print("Contact Not Found.")

def delete_contact():
    del_name=input("Enter Contact Name to Delete :")
     
    with open(contacts_file,"r") as file:
        contacts=file.readlines()

    with open(contacts_file,"w") as file:
        found = False

        for contact in contacts:
            name,number=contact.strip().split(",")
            if name!=del_name:
                file.write(contact)
            else:
                found=True
        
        if found:
            print("Contact Deleted Successfull.")
        else:
            print("Contact Not Found.")

def menu():
    print("\n======Contact Book======")
    print("1. Save contacts")
    print("2. Read contacts")
    print("3. Search contacts")
    print("4. Delete contacts")
    print("5. Exit")

while True:
    menu()
    choice=input("Enter your choice :")
    if choice=="1":
        save_contact()
    elif choice=="2":
        read_contacts()
    elif choice=="3":
        search_contact()
    elif choice=="4":
       delete_contact() 
    elif choice=="5":
        print("Thank You for Choosing")
        break
    else:
        print("Invalid Option.")