
todo_list = {
    "Belajar Python": "belum",
    "Cuci baju": "selesai"
}

def tambah_tugas():
    tugas = input("Masukkan nama tugas baru: ")
    if tugas not in todo_list:
        todo_list[tugas] = "belum"
        print(f"Tugas '{tugas}' berhasil ditambahkan.")
    else:
        print(f"Tugas '{tugas}' sudah ada.")

def ubah_status():
    tugas = input("Masukkan nama tugas yang ingin diubah: ")
    if tugas in todo_list:
        status = input("Masukkan status baru (belum/selesai): ")
        todo_list[tugas] = status
        print(f"Status tugas '{tugas}' diubah menjadi '{status}'.")
    else:
        print(f"Tugas '{tugas}' tidak ditemukan.")

def tampilkan_tugas():
    if not todo_list:
        print("Belum ada tugas.")
    else:
        print("\nDaftar Tugas:")
        for tugas, status in todo_list.items():
            print(f"- {tugas}: {status}")

def menu():
    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Tambah Tugas")
        print("2. Ubah Status Tugas")
        print("3. Lihat Daftar Tugas")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tambah_tugas()
        elif pilihan == "2":
            ubah_status()
        elif pilihan == "3":
            tampilkan_tugas()
        elif pilihan == "4":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")


menu()