from pathlib import Path

def smart_rename_files():
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
            break

        directory = Path(directory_input)

        # New name files
        file_name = input("Enter the new file name: ")

        # Get all file
        files = directory.glob("*.*")

        extension_files = directory.suffix

        # Rename files
        # for i, file in enumerate(files, start=1):
        #     exstension = file.suffix
        #     new_name_file = f"{file_name}-{i}{exstension}"
        #     file.rename(directory / new_name_file)
        #     print(f"Rename: {file.name} -> {new_name_file}")

        print("Program succes!")

        user = input("Press Y to continue renaming, or N to go back to the menu: ").lower()
        if user == "y":
            continue
        elif user == "n":
            break