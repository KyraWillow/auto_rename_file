from pathlib import Path
import os


def rename_files_ui():
    """
    Handles the user interface for renaming files in a specified directory
    with a new base name and an incremental counter.
    """
    while True:
        # Add new path folder
        directory_input = input("Enter the folder path containing files to rename (or type 'back' to return): ").strip()
        if directory_input == "back":
            break

        # Validation directory_input
        if not directory_input:
            print("Path cannot be empty. Please try again.")
            continue

        directory = Path(directory_input)

        # Path validation, what if the path does not exist then this error message appears
        if not directory.exists():
            print(f"Error: The path '{directory}' does not exist. Please check and try again.")
            continue

        # Path validation, what if it's not a folder then this error message appears
        if not directory.is_dir():
            print(f"Error: The path '{directory}' is not a folder. Please enter a path to a folder.")
            continue

        # New name files
        file_name_base = input("Enter the new base name for the files: ").strip()

        # Error validation, what is displayed if the name is empty
        if not file_name_base:
            print("File base name cannot be empty. Please try again.")
            continue

        print(f"\nScanning folder: {directory.resolve()}")

        files_to_rename = []
        for item in directory.iterdir(): # -> .iterdir() to access all contents (file)
                files_to_rename.append(item)

        if not file_name_base:
            print(f"No files found in '{directory}'.")

        rename_count = 0
        skipped_count = 0

        for i, old_file_name in enumerate(files_to_rename):
            original_extension = old_file_name.suffix
            safe_file_name_base = "".join(c if c.isalnum() or c in ['-', '_', ' '] else '_' for c in file_name_base).strip()
            if not safe_file_name_base:
                safe_file_name_base = "renamed_file"

            new_filename_str = f"{safe_file_name_base}-{i}{original_extension}"
            new_file_path = directory / new_filename_str

            # Handler Name Conflict File (Very Important!)
            # Case 1: Old name and new name are the same after normalization (no changes)
            if old_file_name.resolve() == new_file_path.resolve():
                print(f"Skipped: '{old_file_name.name}' already has the target name.")
                skipped_count += 1
                continue

            # Case 2: A new name already exists as another file
            if new_file_path.exists():
                print(f"Error: Target name '{new_filename_str}' already exists in the directory. Skipping '{old_file_name.name}'.")
                skipped_count += 1
                continue

            try:
                old_file_name.rename(new_file_path)
                print(f"Renamed: '{old_file_name.name}' -> '{new_filename_str}'")
                rename_count += 1
            except OSError as e:
                print(f"Error renaming '{old_file_name.name}': {e}. Skipping.")
                skipped_count += 1

        if rename_count > 0:
            print(f"\nSuccessfully renamed {rename_count} file(s).")
        if skipped_count > 0:
            print(f"Skipped {skipped_count} file(s) due to naming conflicts or errors.")
        if rename_count == 0 and skipped_count == 0 and not files_to_rename:
            pass
        elif rename_count == 0 and skipped_count == 0 and files_to_rename:
            print("\nNo files were renamed (e.g., all names would have been duplicates or unchanged).")

        while True:
            user_choice = input("Do you want to rename more files in another folder? (y/n): ").lower().strip()
            if user_choice in ["y", "n"]:
                break
            print("Invalid input. Please enter 'y' or 'n'.")

        if user_choice == "n":
            print("Returning to the main menu.")
            break