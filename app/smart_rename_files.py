from pathlib import Path
from datetime import datetime


def smart_rename_files_ui():
    path_files = ["/"]

    while True:
        directory_input = input("Enter the folder path containing files to rename (or type 'back' to return): ").strip()
        if directory_input == "back":
            break

        # Validation
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

        print(f"\nScanning folder for smart rename: {directory.resolve()}")

        files_to_process = []
        for item in directory.iterdir():
            if item.is_file():
                files_to_process.append(item)

        if not files_to_process:
            print(f"No files found in '{directory}'.")

        rename_count = 0
        skipped_count = 0
        no_date_pattern_count = 0

        for older_files_path in files_to_process:
            oriignal_name = older_files_path.stem
            original_extension = older_files_path.suffix

            parts = oriignal_name.split("_")
            new_name_parts = []
            date_found_and_converted = False

            for part in parts:
                if len(part) == 8 and part.isdigit():
                    try:
                        date_obj = datetime.strptime(part, '%Y%m%d')  # Try parsing with the YYYYMMDD format
                        formated_date = date_obj.strftime('%d%b%Y')  # Change the date format to DDMonYYY
                        new_name_parts.append(formated_date)
                        date_found_and_converted = True
                    except ValueError:
                        new_name_parts.append(part)  # If you fail to use real name
                else:
                    new_name_parts.append(part)  # If not a date candidate then enter here directly

            if date_found_and_converted:
                new_filename_stem = '_'.join(new_name_parts)
                new_filename_str = f"{new_filename_stem}{original_extension}"
                new_file_path = directory / new_filename_str

                # Error handling
                if older_files_path.resolve() == new_file_path.resolve():
                    print(f"Info: Target name for '{older_files_path.name}' is identical after processing. Skipped.")
                    no_date_pattern_count += 1
                    continue

                if new_file_path.exists():
                    print(
                        f"Error: Target smart name '{new_filename_str}' already exists. Skipping '{older_files_path.name}'.")
                    skipped_count += 1
                    continue

                try:
                    older_files_path.rename(new_file_path)
                    print(f"Smart Renamed: '{older_files_path.name}' -> '{new_filename_str}'")
                    rename_count += 1
                except OSError as e:
                    print(f"Error smart renaming '{older_files_path.name}': {e}. Skipping.")
                    skipped_count += 1
                    continue

            else:
                no_date_pattern_count += 1

        if rename_count > 0:
            print(f"\nSuccessfully smart renamed {rename_count} file(s).")
        if skipped_count > 0:
            print(f"Skipped {skipped_count} file(s) due to naming conflicts or errors during smart rename.")
        if no_date_pattern_count > 0:
            print(
                f"{no_date_pattern_count} file(s) did not match the expected date pattern or were already in target format.")
        if rename_count == 0 and skipped_count == 0 and no_date_pattern_count == 0 and not files_to_process:
            pass
        elif rename_count == 0 and skipped_count == 0 and files_to_process and no_date_pattern_count == len(
                files_to_process):
            print(
                "\nNo files were smart renamed (no matching date patterns found or all names would be duplicates/unchanged).")

        while True:
            user_choice = input(f"Do you want to perform smart renaming in another folder? (y/n): ").lower().strip()
            if user_choice in ["y", "n"]:
                break
            print("Invalid input. Please enter 'y' or 'n'.")

        if user_choice == "n":
            print("Returning to the main menu.")
            break
