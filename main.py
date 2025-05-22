import sys
import time
from pathlib import Path

# User input menu
def get_user_input():
    print(""" █████  ██    ██ ████████  ██████      ██████  ███████ ███    ██  █████  ███    ███ ███████     ███████ ██ ██      ███████ ███████ 
██   ██ ██    ██    ██    ██    ██     ██   ██ ██      ████   ██ ██   ██ ████  ████ ██          ██      ██ ██      ██      ██      
███████ ██    ██    ██    ██    ██     ██████  █████   ██ ██  ██ ███████ ██ ████ ██ █████       █████   ██ ██      █████   ███████ 
██   ██ ██    ██    ██    ██    ██     ██   ██ ██      ██  ██ ██ ██   ██ ██  ██  ██ ██          ██      ██ ██      ██           ██ 
██   ██  ██████     ██     ██████      ██   ██ ███████ ██   ████ ██   ██ ██      ██ ███████     ██      ██ ███████ ███████ ███████ 
                                                                                                                                   """)

    print("Main Menu")
    print("1. Rename Files")
    print("2. Guide Book")
    print("3. Exit")

    while True:
        try:

            # Input for user's
            user_input = int(input("Select a menu [1, 2, 3]: "))

            # Validations
            if user_input in [1, 2]:
                return user_input
            elif user_input == 3:
                print("Thank you, and goodbye!")
                sys.exit(0)
            else:
                print("Please enter the correct input.")
        except ValueError:
            print("Invalid input, please enter a number.")

# Loading function
def loading():
    for i in range(4):
        print("Loading" + "." * i)
        time.sleep(i + 1)

def rename_files():
    while True:
        # Add new path folder
        directory_input = input("Enter the file directory to rename: ").replace("\\", "/")
        if not any(scan in directory_input for scan in ["\\", "/"]):
            print("ENTER A VALID PATH. ANY MISTAKES ARE YOUR RESPONSIBILITY!")
            sys.exit(0)

        directory = Path(directory_input)

        # New name files
        file_name = input("Enter the new file name: ")

        # Get all file
        files = directory.glob("*.*")

        # Rename files
        for i, file in enumerate(files, start=1):
            exstension = file.suffix
            new_name_file = f"{file_name}-{i}{exstension}"
            file.rename(directory / new_name_file)
            print(f"Rename: {file.name} -> {new_name_file}")

        print("Program succes!")
        try:
            user = input("Would you like to rename another file: ").lower()

            if user == "y":
                rename_files()
            elif user == "t":
                main()
            else:
                print("Please enter a valid input.")
        except ValueError:
            print("Invalid input, Please choose y or n.")


def guide_book():
    pass

def main():
    user = get_user_input()
    loading()

    if user == 1:
        rename_files()
    elif user == 2:
        guide_book()
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()






















