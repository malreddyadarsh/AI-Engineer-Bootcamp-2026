# File Data Analyzer
# 
# Create a program that:
# 
# Ask the user for a filename.
# Open the file safely.
# Display:
# Number of lines.
# Number of words.
# Number of characters.
# Handle:
# File not found.
# Empty file.
# Permission errors (if encountered).

try:
    sam_file="sample.txt"
    with open(sam_file,"r") as file:
        content=file.readlines()
    if len(content)==0:
        print("\nFile is Empty.")
       
    else:
        no_lines=len(content)
        no_words=0
        no_char=0

        for data in content:
            no_words += len(data.split())

        for data in content:
            no_char += len(data)
        print("\n==========File Data Analyzer==========\n")
        print("Number of Lines           :",no_lines)
        print("Number of words are       :",no_words)
        print("Number of characters are  :",no_char)

except FileNotFoundError as e:
    print(e)
except PermissionError:
    print("Permission denied.")

    
   

        
    