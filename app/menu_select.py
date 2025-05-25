def get_menu_choice(promt: str, maxopt: int):
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
            user_input_str = input(promt)
            user_input = int(user_input_str)
            if 1 <= user_input <= maxopt:
                return user_input
            else:
                print(f"Please enter a number between 1 and {maxopt}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

        print("Please enter a valid input.")
