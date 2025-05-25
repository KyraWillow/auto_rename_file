# 📁 File Renamer Pro - Console Application v1.1.1 ✨

A simple, yet powerful and efficient tool to batch rename files, written in Python. This tool is designed to help users organize their files quickly with clean, structured names and smart date recognition through a terminal-based interface.

---

## 🚀 What's New in v1.1.1 - The "Smart Date" Update!

This version brings significant enhancements focusing on smarter renaming capabilities, improved user experience, and robustness:

* **🆕 New Feature: Smart Date Rename!** 🧙‍♂️
    * Intelligently detects date strings formatted as `YYYYMMDD` within filenames (e.g., `MeetingNotes_20230115_Agenda.pdf`).
    * Automatically converts these dates to a more readable `DDMonYYYY` format (e.g., `MeetingNotes_15Jan2023_Agenda.pdf`).
    * Perfect for organizing photos, documents, or any file where the date is part of the name!
* **🛠️ Enhanced "Standard Rename" Feature:**
    * More robust renaming with a base name and an incremental counter (e.g., `ProjectAlpha-1.docx`, `ProjectAlpha-2.docx`).
    * Basic sanitization for base names: invalid characters are replaced with underscores.
* **🛡️ Improved Input Validation & Error Handling:**
    * Stronger path validation: checks if the path exists and is a directory.
    * Graceful handling of non-existent paths or non-directory paths.
    * Users can now type `back` at path prompts to return to the previous menu.
* **💥 Advanced Conflict Resolution:**
    * Prevents crashes and data loss if the new filename is identical to the old one.
    * Avoids overwriting if the target filename already exists; problematic files are skipped with a notification.
* **📖 Updated Guide Book:**
    * Comprehensive instructions for all features, including the new "Smart Date Rename".
    * Clearer explanations and examples in both Indonesian and English.
* **🎨 UI & UX Tweaks:**
    * Cleaner main menu presentation.
    * More informative feedback messages during operations.
    * ASCII art banner now displays only once at startup.
* **🧹 Code Optimizations:**
    * Refactored codebase for better readability, maintainability, and modularity.
    * Consistent function naming and improved docstrings.

---

## ✨ Core Features

* 📂 **Standard Batch Rename**: Rename all files in a selected folder with a custom prefix and auto-incremented numbering.
* 🗓️ **Smart Date Rename**: Automatically find and reformat `YYYYMMDD` date patterns in filenames to `DDMonYYYY`.
* 🖥️ **Fully Terminal-Based**: Easy to use in any command-line environment.
* 🔒 **Safe Operations**: Includes checks for filename conflicts and path validity.
* 🌐 **Multilingual Guide**: In-app guide available in Indonesian and English.

---

## 🛠 How to Run

1.  Ensure you have Python 3 installed.
2.  Navigate to the project directory in your terminal.
3.  Run the application using:

    ```bash
    python3 main.py
    ```
4.  Follow the on-screen prompts to select an option and rename your files!

---

## 🗒️ Known Issues / Future Enhancements (TODO)

* [ ] Undo functionality (restore original filenames).
* [ ] Support for renaming folders (currently files only).
* [ ] Option to skip specific files or use regex for more advanced matching/renaming.
* [ ] Advanced sanitization options for filenames.
* [ ] Potentially a GUI version in the far future.

---

## 🙏 Acknowledgements

A big thank you to all users for their feedback, which helps in continuously improving this tool!

---
