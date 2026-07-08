# Add contact.
# Search contact.
# Update contact.
# Delete contact.
# Display all contacts.

contacts=[]

def add_contact():
    name=input("Enter name :")
    phone=input("Enter phone number :")

    contact={
        "name":name,
        "phone":phone
    }

    contacts.append(contact)
    print("Contact added successfully")
    

def search_contact():
    name=input("Enter name for searching :")
    for contact in contacts:
        if contact["name"].lower()==name.lower():
            print("\nContact Found")
            print("Name         :",contact["name"])
            print("Phone number :",contact["phone"])
            return
    
    print("Contact not found")

def update_contact():
    upname=input("Enter contact name to update :") 
     
    for contact in contacts:
        if contact["name"].lower()==upname.lower() :
            name=input("Enter new name :")
            phone=input("Enter new phone number :")
            contact["name"]=name
            contact["phone"]=phone
            print("New contact updated successfully")
            return 
        
    print("No name found to update")

def delete_contact():
    name=input("Enter contact name to be deleted")
    for contact in contacts:
        if contact["name"].lower()==name.lower():
            contacts.remove(contact)
            print("Contact Deleted Successfully")
            return 
        
    print("No contact found for deleting")

def display_contact():
    if contacts != []:
        for contact in contacts:
            print("-------------------------")
            print("Contact name :",contact["name"],"\nPhone number :",contact["phone"])
            print("-------------------------")
    else:
        print("No contacts found ")

def menu():
    print("\nContact Details :")
    print("1.Add contact ")
    print("2. Search contact")
    print("3. Update contact")
    print("4.Delete contact")
    print("5.Display all contacts")
    print("6.Exit")


def main():

    while True:
        menu()
        choice=int(input("Enter your choice :"))
        if choice==1:
            contacts=add_contact()
        elif choice==2:
            contacts=search_contact()
        elif choice==3:
            contacts=update_contact()
        elif choice==4:
            contacts=delete_contact()
        elif choice==5:
            contacts=display_contact()
        elif choice==6:
            print("Thankyou for choosing")
            break
        else:
            print("Invalid option")

main()