import random
import string


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    password = []
    character_pool = ""

    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
        character_pool += string.ascii_uppercase

    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
        character_pool += string.ascii_lowercase

    if use_digits:
        password.append(random.choice(string.digits))
        character_pool += string.digits

    if use_symbols:
        password.append(random.choice(string.punctuation))
        character_pool += string.punctuation

    if character_pool == "":
        return "Please select at least one character type."

    while len(password) < length:
        password.append(random.choice(character_pool))

    random.shuffle(password)

    return "".join(password)


# Main Program
print("========== PASSWORD GENERATOR ==========")

length = int(input("Enter Password Length: "))

upper = input("Include Uppercase? (Y/N): ").upper() == "Y"
lower = input("Include Lowercase? (Y/N): ").upper() == "Y"
digits = input("Include Digits? (Y/N): ").upper() == "Y"
symbols = input("Include Symbols? (Y/N): ").upper() == "Y"

selected = sum([upper, lower, digits, symbols])

if selected == 0:
    print("Error: Select at least one character type.")

elif length < selected:
    print(f"Error: Password length should be at least {selected}.")

else:
    password = generate_password(length, upper, lower, digits, symbols)

    print("\nGenerated Password:", password)

    if length < 8:
        print("Strength: Weak")
    elif length < 12:
        print("Strength: Medium")
    else:
        print("Strength: Strong")