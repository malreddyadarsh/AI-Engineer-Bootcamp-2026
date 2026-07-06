# Email Validator
# Contains @
# Contains .
# Doesn't start with @
# Doesn't end with .

email=input("Enter email adress:")
c1=0 # c1 as contains @
c2=0 # c2 as contains .
if email[0]=='@' or email[-1]=='.':
    print("The email start with @ or .")
else:
    for each in email:
        if each=='@':
            c1=1
        elif each=='.':
            c2=1
        
        
    if c1==1 and c2==1:
        print("Correct Email Address")
    else:
        print("Email doesn't contain @ or .")