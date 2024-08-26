import string
import random


def generate_password(length):

    letters = string.ascii_letters
    digits = string.digits
    special_characters = "!@#$%^&*()£"

    length = length

    if length < 3:
        raise ValueError("Password length must be at least 3")

    letters_count = random.randint(1, length - 2)
    digits_count = random.randint(1, length - letters_count - 1)
    special_characters_count = length - letters_count - digits_count

    char_count = letters_count + digits_count + special_characters_count

    if char_count > length:
        raise ValueError(
            "Characters total count is greater than desired password length"
        )

    characters = (
        random.choices(letters, k=letters_count)
        + random.choices(digits, k=digits_count)
        + random.choices(special_characters, k=special_characters_count)
    )

    random.shuffle(characters)
    password = "".join(characters)

    return password


def main():
    length = int(input("Enter password length: "))
    print(generate_password(length))


if __name__ == "__main__":
    main()
