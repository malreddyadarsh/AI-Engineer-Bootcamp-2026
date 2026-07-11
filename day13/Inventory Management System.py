# Add product.
# Update stock.
# Remove product.
# Search product.
# Display inventory.


inventory={}
def add_product(inventory):
    name=input("Enter product name :")
    if name in inventory:
        print("Same Product Already Exists.")
        return
    stock=int(input("Enter stock quantity :"))
    price=int(input("Enter price for each :"))
    inventory[name]={
        "stock":stock,
        "price":price
    }
    print("Product Added Successfully.")

def update_stock(inventory):
    name=input("Enter product name to update stock :")
    if name not in inventory:
        print("No Product to Update Stock.")
        return
    new_stock=int(input("Enter  new stock quantity :"))
    inventory[name]["stock"]=new_stock
    print("Stock Updated Successfully.")

def remove_product(inventory):
    name=input("Enter product name to delete :")
    if name not in inventory:
        print("No Product to delete.")
        return
    del inventory[name]
    print("Product Deleted Successfully.")

def search_product(inventory):
    name=input("Enter Name to Search :")
    if name not in inventory:
        print("Product Not Found in the Inventory.")
        return
    print("Product Found in the inventory.")
    print("Name :",name,"\nStock Available :",inventory[name]["stock"],"\nPrice :",inventory[name]["price"])

def display(inventory):
    if not inventory:
        print("No Products Found.")
    print("\n===Product Details===")
    for name in inventory:
        print("Product :",name)
        print("Stock :",inventory[name]["stock"])
        print("Price :",inventory[name]["price"])
        print("---------------")

while True:
    
    print("\n1. Add Product")
    print("2. Update stock")
    print("3. Remove product")
    print("4. Search product")
    print("5. Display inventory")
    print("6. Exit")

    choice =int(input("Enter your choice: "))
    if choice== 1:
        add_product(inventory)
    elif choice== 2:
        update_stock(inventory)
    elif choice== 3:
        remove_product(inventory)
    elif choice== 4:
        search_product(inventory)
    elif choice==5:
        display(inventory)
    elif choice==6:
        print("Thank you for choosing !")
        break
    else:
        print("Invalid Option")