# Checking a Palindrome Number 

num=int(input("ENter a number :"))
a=num
rev=0

while a>0:
    s=0
    s=a%10
    rev=(rev*10)+s
    a=a//10

if rev==num:
    print(num," is a palindrome number ")
else:
    print(num," is not a palindrome number ")