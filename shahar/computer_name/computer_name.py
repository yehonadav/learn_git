import os
def print_computer_name():
    name = input("Please enter your name:")
    print(f"{name}, your computer name is {os.environ['COMPUTERNAME']}")

print_computer_name()