# Check whether the password is strong, weak and medium

password=input("Enter password :")
length=len(password)
uppercase=0
lowercase=0
digit=0
special=0
if length>=5:
 for each in password:
     if each.isupper():
         uppercase=1
     if each.islower():
         lowercase=1
     if each.isdigit():
         digit=1
     if  not each.isalnum():
         special=1

 score=uppercase+lowercase+digit+special
 if score>=4:
     print("Strong Password")
 elif score < 4 and score >= 2:
     print("Medium Password")
 else:
     print("Weak Password")

else:
    print("The minimum length of the password is : 5 ")