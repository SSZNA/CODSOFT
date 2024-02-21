import string
import random
from collections import deque

def CreatePassword(Passwordlength):
    characters = deque()
    characters.extend(string.ascii_lowercase)
    characters.extend(string.ascii_uppercase)
    characters.extend(string.digits)
    characters.extend(string.punctuation)
    print(characters)
    characters = list(characters)
    random.shuffle(characters)
    print("The generated password is: ","".join(characters[0:Passwordlength]))


def main():
    print("     PASSWORD GENERATOR    ")
    try:
        PasswordLength = int(input("Enter the length of password: "))
        assert PasswordLength > 0, "Length of password must be greater than zero!"
        CreatePassword(PasswordLength)
    except ValueError:
        print("Please enter a valid integer for the password!")
        return
    except AssertionError as e:
        print(e)
        return
main()
