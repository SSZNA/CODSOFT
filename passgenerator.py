import string
import random

def CreatePassword(Passwordlength):
    characters = []
    characters.extend(string.ascii_lowercase)
    characters.extend(string.ascii_uppercase)
    characters.extend(string.digits)
    characters.extend(string.punctuation)
    random.shuffle(characters)
    print("The generated password is: ","".join(characters[0:Passwordlength]))


def main():
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
