#Reverse a number.

num=int(input("Enter a number :"))
a=num
rev=0
while a>0 :
    s=0
    s=a%10
    rev=(rev*10)+s
    a=a//10

print("The reversed number is :",rev)
