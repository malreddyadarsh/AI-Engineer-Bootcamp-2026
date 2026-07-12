# Online Shopping Bill Generator
# 
# Create a program that
# Asks the user to enter the price of 5 products
# Calculates the total bill
# Uses exception handling to
# Reject non-numeric input
# Reject negative prices
# Continue asking until valid input is entered
#try:
print("\nEnter the price of 5 products :")
product=[]
for i in range(1,6):
    while True:
        try:
            price=float(input(f"Enter Price of {i} product :"))
            
            if price<0:
                raise ValueError("\nPrice cannot be negative.")
            else:
                product.append(price)
                break
        except ValueError as e:
            print(e)

total=sum(product)
print("Total Bill is :",round(total,2))

        


