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
    while True:
        try:
            print("1. Indonesian")
            print("2. English")
            print("3. Back to menu")
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
                user = input("Back to main menu [y or n]: ").lower()
                if user == "y":
                    main()
                elif user == "n":
                    break
                else:
                    print("Please enter a valid input.")

            elif user == 2:
                print("""GUIDE BOOK
                1. Please read every output shown by the program carefully to avoid incorrect inputs.
                2. Before pressing Enter, make sure to verify that the path name is correct.
                3. If an error occurs, I recommend moving the folder you want to rename to the same location as this program.
                4. Don’t worry—if your folder contains subfolders, it won’t affect the renaming process since this code only renames files.
                5. We are not responsible for any mistakes. By cloning this repository, you acknowledge that you understand and are aware of the code you are running.
                """)
                user = input("Back to main menu [y or n]: ").lower()
                if user == "y":
                    main()
                elif user == "n":
                    sys.exit(0)
                else:
                    print("Please enter a valid input.")
            elif user == 3:
                main()
            else:
                print("Please enter a valid input.")
        except ValueError:
            print("Invalid input, Please choose 1 or 2.")


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






















