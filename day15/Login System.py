#Login System

#Features:

#Validate username and password.
#Handle invalid input.
#Limit incorrect attempts.
#Display meaningful feedback.

login={
    "username":"Adarsh7222",
    "password":"Reddy@0811"
}

attempts=0
while attempts<5:
    check_username=input("Enter Username :").lower()
    check_password=input("Enter Password :")
    if login["username"].lower()==check_username and login["password"].lower()==check_password:
        print("Login Successful.")
        break
    else:
        print("\nIncorrect Username or Password.")
        print("\nMore Attempts Left is :",(4-attempts))
        attempts+=1
    if attempts==4:
        print("Maximum login attempts Reached.")
        break

                

