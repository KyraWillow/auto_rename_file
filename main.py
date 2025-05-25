from app.menu_select import get_menu_choice
from app.rename_files import rename_files_ui
from app.guide_book import guide_book_ui
from app.smart_rename_files import smart_rename_files_ui


def display_welcome_banner():
    print("""
╔══════════════════════════════════════════════════════════════════╗
║                    AUTO RENAME FILES TOOL                        ║
║                         Welcome User!                            ║
╚══════════════════════════════════════════════════════════════════╝
    """)


# User input menu
def main_menu():
    """
    Displays the main menu and handles user interaction.

    This function shows a menu with options for renaming files,
    accessing the guide book, using smart rename, or exiting.
    It loops until the user chooses to exit.
    """
    options_main_menu = ["Rename Files", "Smart Rename File", "Guide Books", "Exit"]

    display_welcome_banner()

    while True:
        print("\nMain Menu")
        for i, opt in enumerate(options_main_menu):
            print(f"{i + 1}. {opt}")

        maxopt = len(options_main_menu)
        user_input = get_menu_choice("Select options: ", maxopt)

        # Validations
        if user_input == 1:
            rename_files_ui()
        elif user_input == 2:
            smart_rename_files_ui()
        elif user_input == 3:
            guide_book_ui()
        elif user_input == maxopt:
            print("Thank you, and goodbye!")
            break


if __name__ == "__main__":
    main_menu()
