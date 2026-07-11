# Add contact.
# Search contact.
# Update contact.
# Delete contact.
# Display all contacts.


contacts={}
def add_contact(contacts):
    name=input("Enter contact name to add:")
    if name not in contacts:
        number=int(input("Enter phone number to add:"))
        contacts[name]={
            "phone_number":number
        }
        print("Contact Name & Number added successfully")
        return
    print("Same Name already exists , enter different name to add.")


def search_contact(contacts):
    name=input("Enter contact name to search :")
    if name in contacts:
        print("Contact Found ")
        print("Contact Name :",name,"\tContact Number :",contacts[name]["phone_number"])
        return
    print("No name found for searching")

def update_contact(contacts):
    name=input("Enter name to update contact :")
    if name not in contacts:
        print("No Contact Name to Update.")
        return
    
    new_number=int(input("Enter New number to update :"))
    contacts[name]["phone_number"]=new_number
    print("Contact Updated Successfully.")

def delete_contact(contacts):
    name=input("Enter name to delete contact :")
    if name not in contacts:
        print("No Contact Name found to delete.")
        return
    del contacts[name]
    print("Contact Name deleted successfully.")

def display_all(contacts):
    if  len(contacts)<=0:
        print("No Contacs Found to Display.")
        return
    print("\n=====Contact=====\n")
    for name,details in contacts.items():
        print("-----------------------------")
        print("Name :",name)
        print("Phone Number :",details['phone_number'])


while True:

    print("\n===== Contact Book =====")
    print("1. Add Contact ")
    print("2.Search Contact")
    print("3. Update Contact ")
    print("4. Delete Contact ")
    print("5.Display Contact ")
    print("6. Exit")

    choice =int(input("Enter your choice: "))
    if choice== 1:
        add_contact(contacts)
    elif choice== 2:
        search_contact(contacts)
    elif choice== 3:
        update_contact(contacts)
    elif choice== 4:
        delete_contact(contacts)
    elif choice==5:
        display_all(contacts)
    elif choice==6:
        print("Thank you for choosing !")
        break
    else:
        print("Invalid Option")