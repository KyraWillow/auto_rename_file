from app.rename_files import rename_files
from app.guide_book import guide_book
from app.menu_select import menu_select

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
    options_main_menu = ["Rename Files", "Guide Books", "Exit"]

    while True:

        print(""" █████  ██    ██ ████████  ██████      ██████  ███████ ███    ██  █████  ███    ███ ███████     ███████ ██ ██      ███████ ███████ 
██   ██ ██    ██    ██    ██    ██     ██   ██ ██      ████   ██ ██   ██ ████  ████ ██          ██      ██ ██      ██      ██      
███████ ██    ██    ██    ██    ██     ██████  █████   ██ ██  ██ ███████ ██ ████ ██ █████       █████   ██ ██      █████   ███████ 
██   ██ ██    ██    ██    ██    ██     ██   ██ ██      ██  ██ ██ ██   ██ ██  ██  ██ ██          ██      ██ ██      ██           ██ 
██   ██  ██████     ██     ██████      ██   ██ ███████ ██   ████ ██   ██ ██      ██ ███████     ██      ██ ███████ ███████ ███████ 
                                                                                                                                   """)

        print("Main Menu")
        for i, opt in enumerate(options_main_menu):
            print(f"{i+1}. {opt}")

        maxopt = len(options_main_menu)
        user_input = menu_select(maxopt)

        # Validations
        if user_input == 1:
            rename_files()
        elif user_input == 2:
            guide_book()
        elif user_input == maxopt:
            print("Thank you, and goodbye!")
            break

if __name__ == "__main__":
    main_menu()
