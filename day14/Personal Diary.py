# Personal Diary

# Features:

# Write today's note.
# Save it.
# Read old notes.
# Append new entries.

diary="Personal_diary.txt"

def today_note():
    notes=input("Enter today's notes :")

    with open(diary,"a") as file:
        file.write(notes)
    print("Today's Notes Added Successfully.")

def read_old_notes():
    
    with open(diary,"r") as file:
        notes=file.readlines()
    print("\n======Printing Old Notes======")
    print(notes)

def new_entries():
    notes=input("Enter new paragrah to add :")

    with open(diary,"a") as file:
        file.write(notes+"\n")
    print("New Data Added Successfully.")

def menu():
    print("\n=========Personal Diary=========")
    print("1.Write Today's Notes ")
    print("2. Read Old One's ")
    print("3. Append New Entries ")
    print("4. Exit ")

while True:
    menu()
    choice=int(input("Choose your options :"))
    if choice==1:
        today_note()
    elif choice==2:
        read_old_notes()
    elif choice==3:
        new_entries()
    elif choice==4:
        print("Thank You for Choosing !")
        break
    else:
        print("Invalid Option")
