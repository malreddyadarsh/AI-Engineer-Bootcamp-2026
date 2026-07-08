import random


def play_game():
    print("\n========== NUMBER GUESSING GAME ==========")

    print("\nSelect Difficulty")
    print("1. Easy (1-10, 5 Attempts)")
    print("2. Medium (1-50, 7 Attempts)")
    print("3. Hard (1-100, 10 Attempts)")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        start = 1
        end = 10
        attempts = 5
    elif choice == 2:
        start = 1
        end = 50
        attempts = 7
    elif choice == 3:
        start = 1
        end = 100
        attempts = 10
    else:
        print("Invalid Choice!")
        return

    secret = random.randint(start, end)
    score = 100

    print(f"\nGuess a number between {start} and {end}")

    while attempts > 0:

        print("\nAttempts Left:", attempts)

        guess = int(input("Enter your guess: "))

        if guess == secret:
            print("\n Congratulations!")
            print("You guessed the correct number.")
            print("Your Score:", score)
            return

        elif guess < secret:
            print("Too Low!")

        else:
            print("Too High!")

        attempts -= 1
        score -= 10

    print("\nGame Over!")
    print("The Correct Number was:", secret)


while True:

    play_game()

    again = input("\nDo you want to play again? (Y/N): ").upper()

    if again != "Y":
        print("\nThank you for playing!")
        break