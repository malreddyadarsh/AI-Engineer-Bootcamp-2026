
#Add item.
#Remove item.
#Display cart.
#Calculate total.
#Clear cart.

def add_item(items):
    name=input("Enter name to add :")
    price=int(input("Enter price to add :"))
    item = {
        "name": name,
        "price": price
    }
    items.append(item)
    print("Item added Successfully.")
    return items

def remove_item(items):
    name = input("Enter item name to remove: ")

    for item in items:
        if item["name"].lower() == name.lower():
            items.remove(item)
            print("Item removed successfully.")
            return

def display_cart(items):
    print(items)

def calculate_total(items):
    total=0
    for item in items:
        total+=item['price']
    print("total :",total)

def clear_items(items):
    items.clear()
    print("All items cleared")
    return items

def menu():
    print("Choose below options :")
    print("1. Add item")
    print("2. Remove item")
    print("3. Display cart")
    print("4. Calculate total")
    print("5. Clear items")
    print("6. Exit")

def main():
    items=[]
    while True:
        menu()
        ch=int(input("Enter chooice :"))
        if ch==1:
            add_item(items)
        elif ch==2:
            remove_item(items)
        elif ch==3:
            display_cart(items)
        elif ch==4:
          calculate_total(items)
        elif ch==5:
          clear_items(items)
        elif ch==6:
            print("Thank you ")
            break
        else:
            print("Invalid option ")
            
main()



