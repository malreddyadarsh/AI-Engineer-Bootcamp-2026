# File Reader Utility

# Features:

# Ask for a file name.
# Read and display the file.
# Handle missing files gracefully.
# Display a success message when the read completes.

file_name=input("Enter File name :")

try:
    with open(file_name,"r") as file:
        content=file.read() # Reading a file
    print("File Read Successfully.")
    if content=="":
        print("No Content in the File To Display")
    else:
        print("\n=====Displaying File content=====\n")
        print(content)

except FileNotFoundError :
    print("Error : File Not Found.")
    
