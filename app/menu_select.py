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
