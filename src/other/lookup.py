import os
import shutil

def print_line():
    terminal_width = shutil.get_terminal_size().columns
    print("_" * terminal_width)

def lookup_pass():
    password = input("Enter a password: ")

    with open("password-data.txt", "r") as file:
        data = file.read()
        if password in data:
            print("\nPassword leaked in data breach!")
            print_line()
            lookup_pass()
        else:
            print("\nPassword is not in any known breach.")
            print_line()
            lookup_pass()

directory = os.path.dirname(os.path.realpath(__file__))

os.chdir(directory)

print("Password Lookup | Created by: itswhiteboard")
print_line()

lookup_pass()