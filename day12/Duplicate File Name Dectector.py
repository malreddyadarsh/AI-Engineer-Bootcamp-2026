# Features:

# Input a list of file names.
# Detect duplicates.
# Display unique file names.
# Count duplicates.

n=int(input("How many no.of files name you want to enter :"))
file_names=[]
print("\nEnter All List of File Names :")
for i in range(n):
    name=input()
    file_names.append(name)

unique_file_names=set()
count=0
dupliactes_files=set()
# Dectecting duplicates 
for name in file_names:
    if name in unique_file_names:
        count+=1
        dupliactes_files.add(name)
    else:
        unique_file_names.add(name)
        

print("\n====Displaying Unique File====")
for file in unique_file_names:
    print(file)

print("\n\nNo.of Duplicates :",count)    
print("Duplicates File Names :")
for file in dupliactes_files:
    print(file)