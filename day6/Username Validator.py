# Username Validator 

username=input("Enter username :")
length=len(username)

if length>=5 and length <=10 :
    if username.isalnum():
        if username[0].isalpha():
            print("Valid Username")
            
        else:
            print("First character should start with alphabet")
    else:
        print("The Username contains Special characters\nPlease try without special characters")
        
else:
    print("The minimum & maximum lengths of username are 5 & 10")

        