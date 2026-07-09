def add_product(inventory):
    name=input("Enter product name :").lower()
    for product in inventory:
        if name==product['name']:
            print("Product already exists.")
            return
    quantity=int(input("Enter product quantity :"))
    inventory.append({
        "name": name,
        "quantity": quantity
                })
    print("Product Added successfully.")
    return inventory

def update_quantity(inventory):
    name=input("Enter product name for modifying quantity :").lower()

    for product in inventory:
        if product['name']==name:
            quantity=int(input("Enter new quantity to update :"))
            product["quantity"]=quantity
            print("Product Quantity updated successfully.")
            return inventory
    
    print("Product Not found. ")

def delete_product(inventory):
    name=input("Enter product name to delete :").lower()

    for product in inventory:
        if product["name"]==name:
            inventory.remove(product)
            print("Product deleted successfully.")
            return inventory
    
    print("Product Not Found. ")

def search_product(inventory):
    name=input("Enter product name to search :").lower()

    for product in inventory:
        if product['name']==name:
            print("Product Found in the inventory. ")
            return
    print("Product not found in the inventory. ")

def display(inventory):
    print("Products list ")
    print(inventory)

def menu():
    print("=====Inventory Management System=====")
    print("1. Add Product")
    print("2. Update Quality")
    print("3. Delete Product")
    print("4. Search Product")
    print("5. Display ")
    print("6. Exit ")

def main():
    inventory=[]

    while True:
        menu()
        ch=int(input("Enter your choice :"))
        if ch==1:
            add_product(inventory)
        elif ch==2:
            update_quantity(inventory)
        elif ch==3:
            delete_product(inventory)
        elif ch==4:
            search_product(inventory)
        elif ch==5:
            display(inventory)
        elif ch==6:
            print("Thank you for choosing !")
            break
        else:
            print("Invalid Option. ")

main()


   