# Fibonacci Series of n terms

n=int(input("Enter how many no. of terms which should be greater than 2 :"))

a=1
b=1
print("=====Fibonacci Series=====")
for i in range (n-2):
    if b==1:
        print(a)
        print(b)
    c=a+b
    print(c)
    a=b
    b=c

