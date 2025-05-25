from app.menu_select import get_menu_choice

def guide_book_ui():
    """
    Displays a guide book menu to help users understand how to use the program.

    Users can select to read the guide in Indonesian or English, or return to the main menu.
    The guide provides important tips about input correctness, path validation, error handling,
    and disclaimers about responsibility for errors.
    :return:
        none.
    """
    options_guide_book = ["Indonesian", "English", "Back to menu"]
    while True:
        print("\nGuide Book menu")
        for i, opt in enumerate(options_guide_book):
            print(f"{i + 1}. {opt}")

        maxopt = len(options_guide_book)
        user_input = get_menu_choice("Select guide option: ", maxopt)

        if user_input == 1:
            print("""
            GUIDE BOOK
            1. Bacalah setiap output yang dikeluarkan oleh program agar tidak salah memasukkan input.
            2. Pastikan sebelum menekan Enter, Anda sudah memeriksa apakah nama path sudah benar.
            3. Jika terjadi error, saran saya adalah memindahkan folder yang ingin Anda ganti namanya ke lokasi yang sama dengan program ini.
            4. Jangan khawatir, jika di dalam folder Anda terdapat folder lain, hal tersebut tidak akan mempengaruhi penggantian nama karena kode ini hanya untuk mengubah nama file.
            5. Segala kesalahan bukan menjadi tanggung jawab kami. Dengan meng-clone repository ini, berarti Anda telah memahami dan mengetahui isi kode yang akan dijalankan.
            """)
            input("Press Enter to exit: ").lower()

        elif user_input == 2:
            print("""GUIDE BOOK
            1. Please read every output shown by the program carefully to avoid incorrect inputs.
            2. Before pressing Enter, make sure to verify that the path name is correct.
            3. If an error occurs, I recommend moving the folder you want to rename to the same location as this program.
            4. Don’t worry—if your folder contains subfolders, it won’t affect the renaming process since this code only renames files.
            5. We are not responsible for any mistakes. By cloning this repository, you acknowledge that you understand and are aware of the code you are running.
            """)
            input("Press Enter to exit: ").lower()

        elif user_input == 3:
            return