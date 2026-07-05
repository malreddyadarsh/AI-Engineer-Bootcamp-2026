# Printing Prime Numbers between 1 And 100

i=1
print("Printing Prime numbers between 1 and 100 :")
while i<=100:
    a=1
    x=0
    for a in range(1,i+1):
        y = i % a
        if y == 0:
            x+=1
    if x==2:
        print(i)
    i+=1