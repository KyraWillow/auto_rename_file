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
                       ==================================================
                       PANDUAN PENGGUNAAN PROGRAM PENGGANTI NAMA FILE
                       ==================================================

                       Selamat datang di Panduan Penggunaan! Program ini membantu Anda mengganti nama file
                       secara massal dengan mudah melalui beberapa fitur.

                       1.  MEMAHAMI MENU UTAMA:
                           --------------------
                           Saat program dimulai, Anda akan melihat Menu Utama dengan opsi:
                           * Rename Files: Mengganti nama semua file di folder tertentu dengan
                                             nama dasar baru dan nomor urut (misal: Laporan-1.pdf, Laporan-2.pdf).
                           * Smart Rename Files: Mengganti nama file secara cerdas dengan mencari
                                                   pola tanggal 'YYYYMMDD' (misal: 20230115) dalam nama file
                                                   dan mengubahnya menjadi format 'DDMonYYYY' (misal: 15Jan2023).
                                                   Contoh: 'Dokumen_20230520_Penting.docx' menjadi 'Dokumen_20May2023_Penting.docx'.
                           * Guide Books: Menampilkan panduan ini.
                           * Exit: Keluar dari program.

                       2.  MEMASUKKAN PATH (LOKASI FOLDER):
                           --------------------------------
                           * Validitas: Pastikan Anda memasukkan path yang benar menuju folder
                                          yang berisi file-file yang ingin Anda ubah namanya.
                                          Program akan memeriksa apakah path tersebut ada dan merupakan sebuah folder.
                           * Contoh Path:
                               * Windows: C:/Users/NamaAnda/Documents/FolderGambar
                               * Linux/Mac: /home/NamaAnda/Documents/FolderGambar
                           * Relatif Path: Anda juga bisa menggunakan path relatif jika program
                                             dijalankan dari lokasi tertentu.
                           * Kembali: Saat diminta memasukkan path, Anda dapat mengetik 'back' (tanpa tanda kutip)
                                        dan menekan Enter untuk kembali ke menu sebelumnya.

                       3.  FITUR "RENAME FILES":
                           --------------------
                           * Fungsi: Mengganti nama semua file di folder target.
                           * Input:
                               1.  Path Folder: Lokasi folder file.
                               2.  Nama Dasar Baru: Teks utama untuk nama file baru (misal: "DokumenRapat").
                           * Proses: File akan diubah namanya menjadi "[NamaDasarBaru]-[NomorUrut].[EkstensiAsli]".
                                      Contoh: Jika nama dasar "FotoLiburan", file akan menjadi FotoLiburan-1.jpg, FotoLiburan-2.png, dst.
                           * Penting: Karakter selain huruf, angka, spasi, tanda hubung (-), atau garis bawah (_)
                                        pada nama dasar akan diganti dengan garis bawah (_).

                       4.  FITUR "SMART RENAME FILES":
                           ---------------------------
                           * Fungsi: Mencari file yang namanya mengandung segmen tanggal dengan format
                                       'YYYYMMDD' (contoh: 'Laporan_20240115_data.pdf') dan mengubah segmen
                                       tanggal tersebut menjadi format 'DDMonYYYY' (contoh: 'Laporan_15Jan2024_data.pdf').
                           * Input:
                               1.  Path Folder: Lokasi folder file.
                           * Proses: Program akan memindai nama file yang dipisahkan oleh garis bawah ('_').
                                       Jika salah satu bagian adalah angka 8 digit yang valid sebagai tanggal YYYYMMDD,
                                       bagian tersebut akan diformat ulang.
                           * Contoh: 'Invoice_20231231_ClientA.xlsx' menjadi 'Invoice_31Dec2023_ClientA.xlsx'.

                       5.  PENANGANAN KONFLIK DAN KESALAHAN:
                           -----------------------------------
                           * Nama Sama: Jika nama baru yang dihasilkan sama dengan nama file lama,
                                          file tersebut akan dilewati.
                           * Target Sudah Ada: Jika nama baru yang akan diberikan ternyata sudah digunakan
                                                 oleh file lain di folder yang sama, file tersebut akan dilewati
                                                 untuk mencegah penimpaan data.
                           * Tidak Ada File: Jika folder yang dituju tidak memiliki file, Anda akan diberitahu.
                           * Error Lain: Jika terjadi error saat penggantian nama (misal: masalah izin),
                                           file tersebut akan dilewati dan pesan error akan ditampilkan.

                       6.  TIPS PENTING:
                           -------------
                           * Periksa Kembali: Selalu periksa kembali path folder dan input lainnya
                                              sebelum menekan Enter.
                           * Backup Data: Sangat disarankan untuk membuat cadangan (backup) dari file-file penting
                                            Anda sebelum menjalankan operasi penggantian nama massal.
                           * Lokasi Program: Jika mengalami kesulitan dengan path, coba pindahkan folder
                                               yang ingin diubah namanya ke lokasi yang relatif mudah dijangkau
                                               atau gunakan path absolut yang lengkap dan benar.
                           * Hanya File: Program ini hanya akan mengubah nama file, bukan folder di dalamnya.

                       7.  DISCLAIMER:
                           -----------
                           Program ini disediakan apa adanya. Pengembang tidak bertanggung jawab atas
                           kehilangan atau kerusakan data akibat kesalahan penggunaan atau bug yang mungkin ada.
                           Gunakan dengan bijak dan risiko Anda sendiri.""")
            input("Press Enter to exit: ").lower()

        elif user_input == 2:
            print("""
                        ======================================
                        FILE RENAMER PROGRAM - USER GUIDE
                        ======================================

                        Welcome to the User Guide! This program helps you batch rename files
                        easily with several features.

                        1.  UNDERSTANDING THE MAIN MENU:
                            --------------------------
                            When the program starts, you'll see the Main Menu with these options:
                            * Rename Files: Renames all files in a specific folder with a new
                                              base name and a sequential number (e.g., Report-1.pdf, Report-2.pdf).
                            * Smart Rename Files: Intelligently renames files by looking for
                                                    a 'YYYYMMDD' date pattern (e.g., 20230115) in the filename
                                                    and converting it to 'DDMonYYYY' format (e.g., 15Jan2023).
                                                    Example: 'Document_20230520_Important.docx' becomes 'Document_20May2023_Important.docx'.
                            * Guide Books: Displays this guide.
                            * Exit: Exits the program.

                        2.  ENTERING THE PATH (FOLDER LOCATION):
                            ------------------------------------
                            * Validity: Ensure you enter the correct path to the folder
                                          containing the files you want to rename.
                                          The program will check if the path exists and is a directory.
                            * Path Examples:
                                * Windows: C:/Users/YourName/Documents/ImageFolder
                                * Linux/Mac: /home/YourName/Documents/ImageFolder
                            * Relative Paths: You can also use relative paths if the program
                                                is run from a specific location.
                            * Go Back: When prompted for a path, you can type 'back' (without quotes)
                                         and press Enter to return to the previous menu.

                        3.  "RENAME FILES" FEATURE:
                            -----------------------
                            * Function: Renames all files in the target folder.
                            * Inputs:
                                1.  Folder Path: The location of the files.
                                2.  New Base Name: The main text for the new filenames (e.g., "MeetingNotes").
                            * Process: Files will be renamed to "[NewBaseName]-[SequenceNumber].[OriginalExtension]".
                                       Example: If base name is "VacationPhoto", files become VacationPhoto-1.jpg, VacationPhoto-2.png, etc.
                            * Important: Characters other than letters, numbers, spaces, hyphens (-), or underscores (_)
                                         in the base name will be replaced with an underscore (_).

                        4.  "SMART RENAME FILES" FEATURE:
                            -----------------------------
                            * Function: Scans filenames for date segments in 'YYYYMMDD' format
                                        (e.g., 'Report_20240115_data.pdf') and converts that date segment
                                        to 'DDMonYYYY' format (e.g., 'Report_15Jan2024_data.pdf').
                            * Input:
                                1.  Folder Path: The location of the files.
                            * Process: The program will scan filenames that are split by underscores ('_').
                                        If a part is an 8-digit number that's a valid YYYYMMDD date,
                                        that part will be reformatted.
                            * Example: 'Invoice_20231231_ClientA.xlsx' becomes 'Invoice_31Dec2023_ClientA.xlsx'.

                        5.  CONFLICT AND ERROR HANDLING:
                            ----------------------------
                            * Same Name: If the new generated name is identical to the old filename,
                                           the file will be skipped.
                            * Target Exists: If the new intended filename already exists as another
                                               file in the same folder, the current file will be skipped
                                               to prevent data overwriting.
                            * No Files Found: You will be notified if the target folder contains no files.
                            * Other Errors: If an error occurs during renaming (e.g., permission issues),
                                              that file will be skipped, and an error message will be shown.

                        6.  IMPORTANT TIPS:
                            ---------------
                            * Double-Check: Always double-check the folder path and other inputs
                                            before pressing Enter.
                            * Backup Data: It is highly recommended to back up your important files
                                             before performing any batch renaming operations.
                            * Program Location: If you encounter path difficulties, try moving the folder
                                                  you want to rename to an easily accessible location or use
                                                  the full, correct absolute path.
                            * Files Only: This program will only rename files, not folders within them.

                        7.  DISCLAIMER:
                            -----------
                            This program is provided as-is. The developer is not responsible for
                            any data loss or damage resulting from misuse or potential bugs.
                            Use wisely and at your own risk.""")
            input("Press Enter to exit: ").lower()

        elif user_input == 3:
            return
