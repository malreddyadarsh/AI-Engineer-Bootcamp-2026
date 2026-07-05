# Number Guessing Game

secret_num=18

while True:
    guess=int(input("Enter Guessing Number :"))

    if guess<secret_num:
        print("Too Low")
    elif guess>secret_num:
        print("Too High")
    else:
        print("Congratulations! You guessed it.")
        break

    