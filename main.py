import sys
from pathlib import Path

# User input menu
def main_menu():
    """
    Displays the main menu and handles user interaction.

    This function shows a simple menu with three options:
    1. Rename Files
    2. Guide Books
    3. Exit

    Based on the user's choice:
    - Option 1 calls the rename_files() function.
    - Option 2 calls the guide_book() function.
    - Option 3 exits the program.

    The menu will keep looping until the user selects "Exit".
    :return:
        none.
    """
    options = ["Rename Files", "Guide Books", "Exit"]

    while True:

        print(""" █████  ██    ██ ████████  ██████      ██████  ███████ ███    ██  █████  ███    ███ ███████     ███████ ██ ██      ███████ ███████ 
██   ██ ██    ██    ██    ██    ██     ██   ██ ██      ████   ██ ██   ██ ████  ████ ██          ██      ██ ██      ██      ██      
███████ ██    ██    ██    ██    ██     ██████  █████   ██ ██  ██ ███████ ██ ████ ██ █████       █████   ██ ██      █████   ███████ 
██   ██ ██    ██    ██    ██    ██     ██   ██ ██      ██  ██ ██ ██   ██ ██  ██  ██ ██          ██      ██ ██      ██           ██ 
██   ██  ██████     ██     ██████      ██   ██ ███████ ██   ████ ██   ██ ██      ██ ███████     ██      ██ ███████ ███████ ███████ 
                                                                                                                                   """)

        print("Main Menu")
        for i, opt in enumerate(options):
            print(f"{i+1}. {opt}")

        maxopt = len(options)
        user_input = menu_select(maxopt)

        # Validations
        if user_input == 1:
            rename_files()
        elif user_input == 2:
            guide_book()
        elif user_input == maxopt:
            print("Thank you, and goodbye!")
            break

def menu_select(maxopt):
    """
    Prompts the user to select a menu option within a valid range.

    This function keeps asking for input until the user enters
    a valid integer between 1 and the specified maximum option (inclusive).
    If the input is invalid (non-integer or out of range), it prompts again.

    maxopt (int): The highest valid menu option number.

    :return:
        int: The user's validated menu selection.
    """
    while True:
        try:
            user_input = int(input("Select options: "))
            if 1 <= user_input <= maxopt:
                return user_input
        except ValueError:
            pass

        print("Please enter a valid input.")

def rename_files():
    """
    Renames all files in a specified directory with a new base name.

    This function asks the user for a folder path and a new base filename.
    It then renames each file in that folder to follow the format:
    [new_name]-[index].[original_extension]. The process continues
    until the user chooses to return to the main menu.

    Exits the program if the provided path is not valid.
    :return:
        New files name.
    """
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

        user = input("Press Y to continue renaming, or N to go back to the menu: ").lower()
        if user == "y":
            continue
        elif user == "n":
            break


def guide_book():
    """
    Displays a guide book menu to help users understand how to use the program.

    Users can select to read the guide in Indonesian or English, or return to the main menu.
    The guide provides important tips about input correctness, path validation, error handling,
    and disclaimers about responsibility for errors.
    :return:
        none.
    """
    options = ["Indonesian", "English", "Back to menu"]
    while True:
        print("Guide Book menu")
        for i, opt in enumerate(options):
            print(f"{i + 1}. {opt}")

        user = int(input("Select a menu [1, 2, 3]:"))

        if user == 1:
            print("""
            GUIDE BOOK
            1. Bacalah setiap output yang dikeluarkan oleh program agar tidak salah memasukkan input.
            2. Pastikan sebelum menekan Enter, Anda sudah memeriksa apakah nama path sudah benar.
            3. Jika terjadi error, saran saya adalah memindahkan folder yang ingin Anda ganti namanya ke lokasi yang sama dengan program ini.
            4. Jangan khawatir, jika di dalam folder Anda terdapat folder lain, hal tersebut tidak akan mempengaruhi penggantian nama karena kode ini hanya untuk mengubah nama file.
            5. Segala kesalahan bukan menjadi tanggung jawab kami. Dengan meng-clone repository ini, berarti Anda telah memahami dan mengetahui isi kode yang akan dijalankan.
            """)
            user = input("Press any key to exit: ").lower()
            if user:
                break

        elif user == 2:
            print("""GUIDE BOOK
            1. Please read every output shown by the program carefully to avoid incorrect inputs.
            2. Before pressing Enter, make sure to verify that the path name is correct.
            3. If an error occurs, I recommend moving the folder you want to rename to the same location as this program.
            4. Don’t worry—if your folder contains subfolders, it won’t affect the renaming process since this code only renames files.
            5. We are not responsible for any mistakes. By cloning this repository, you acknowledge that you understand and are aware of the code you are running.
            """)
            user = input("Press any key to exit: ").lower()
            if user:
                break
        elif user == 3:
            return
        else:
            print("Please enter a valid input.")

if __name__ == "__main__":
    main_menu()
