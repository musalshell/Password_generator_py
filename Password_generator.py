import random
import string

# password generator setup


def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    character = letters
    if numbers:
        character += digits

    if special_characters:
        character += special

    pwd = ""
    meet_criteria = False
    has_number = False
    has_special = False

# criteria for if there is Numbers or special charaters

    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(character)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria + meet_criteria and has_special

    return pwd

# returning generated password


min_length = int(input("Enter the minimum length: "))
has_number = input(
    "Do you want your password to comtain numbers(y/n)? ").lower() == "y"
has_special = input(
    "Do you want your password to contain special characters (y/n)? ").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print("The generated password is: ", pwd)
