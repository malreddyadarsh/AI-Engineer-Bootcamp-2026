#For Loop examples
# Printing Multiplication Table
num=int(input("Enter a number for multiplication :"))
n=int(input("How many rows :"))
i=1
print("=====Multiplication Table=====")
for i in range (n+1):
    print(num,"*",i,"=",(num*i))


