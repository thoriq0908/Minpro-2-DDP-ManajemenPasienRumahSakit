import pwinput
from prettytable import PrettyTable
import os

os.system("cls" if os.name == "nt" else "clear")

# DATA (DICTIONARY)
# nomor_rm pada akun pasien menyimpan data milik akun tersebut (None = belum punya data)
akun_pengguna = {
    "admin": {"password": "123", "role": "admin"},
    "pasien": {"password": "123", "role": "user", "nomor_rm": None},
}

# nomor RM -> {nama, umur, ruangan}
data_pasien = {}


# FUNCTION VALIDASI
def input_angka(nomor):
    while True:
        teks = input(nomor)
        try:
            angka = int(teks)         
            if angka < 0:             
                print("Input tidak boleh negatif, silahkan input kembali")
            else:
                return angka
        except ValueError:             
            print("Input harus berupa angka, silahkan input kembali")

def input_teks(pesan, nama_field):
    while True:
        teks = input(pesan)
        if teks != "":
            return teks
        else:
            print(f"{nama_field} tidak boleh kosong, silahkan input kembali")


# FUNCTION LOGIN
def login():
    print("================================")
    print("            LOGIN ")
    print("================================")
    username = input("Username: ")
    password = pwinput.pwinput("Password: ")

    if username in akun_pengguna and akun_pengguna[username]["password"] == password:
        print(f"Login berhasil. Selamat datang, {username}.")
        return username
    else:
        print("Username atau password salah.")
        return None


# FUNCTION ADMIN
def tambah_pasien():
    print()
    print("--Tambah data pasien--")
    nomor_rm = input_angka("Masukkan nomor rekam medis pasien: ")

    if nomor_rm in data_pasien:
        print(f"Nomor rekam medis {nomor_rm} sudah ada. Silakan masukkan nomor yang berbeda.")
    else:
        nama = input_teks("Masukkan nama pasien: ", "Nama")
        umur = input_angka("Masukkan umur pasien: ")
        ruangan = input_teks("Masukkan ruangan pasien: ", "Ruangan")
        data_pasien[nomor_rm] = {"nama": nama, "umur": umur, "ruangan": ruangan}
        print("Data pasien berhasil ditambahkan.")


def tampil_pasien():
    print()
    print("--Tampilkan seluruh data pasien--")
    if len(data_pasien) == 0:
        print("Belum ada data pasien yang tersimpan.")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["No. RM", "Nama", "Umur", "Ruangan"]
        for nomor_rm, data in data_pasien.items():
            tabel.add_row([nomor_rm, data["nama"], data["umur"], data["ruangan"]])
        print(tabel)
        print(f"Jumlah pasien Opname saat ini: {len(data_pasien)}")


def ubah_pasien():
    print()
    print("--Ubah data pasien--")
    if len(data_pasien) == 0:
        print("Belum ada data pasien yang tersimpan.")
    else:
        nomor_rm = input_angka("Masukkan nomor rekam medis pasien yang ingin diubah: ")
        if nomor_rm in data_pasien:
            nama = input_teks("Masukkan nama baru pasien: ", "Nama")
            umur = input_angka("Masukkan umur baru pasien: ")
            ruangan = input_teks("Masukkan ruangan baru pasien: ", "Ruangan")
            data_pasien[nomor_rm] = {"nama": nama, "umur": umur, "ruangan": ruangan}
            print("Data pasien berhasil diubah.")
        else:
            print(f"Nomor rekam medis {nomor_rm} tidak ditemukan.")


def hapus_pasien():
    print()
    print("--Hapus data pasien--")
    if len(data_pasien) == 0:
        print("Belum ada data pasien yang tersimpan.")
    else:
        nomor_rm = input_angka("Masukkan nomor rekam medis pasien yang ingin dihapus: ")
        if nomor_rm in data_pasien:
            del data_pasien[nomor_rm]
            print(f"Data pasien dengan nomor rekam medis {nomor_rm} berhasil dihapus.")
        else:
            print(f"Nomor rekam medis {str(nomor_rm)} tidak ditemukan.")


# FUNCTION DATA MILIK SENDIRI (PASIEN)
def punya_data(username):
    nomor_rm = akun_pengguna[username]["nomor_rm"]
    return nomor_rm is not None and nomor_rm in data_pasien


def tambah_data_sendiri(username):
    print()
    print("--Tambah data saya--")
    if punya_data(username):
        print("Anda sudah memiliki data. Pasien hanya dapat menambah satu data milik sendiri.")
    else:
        nomor_rm = input_angka("Masukkan nomor rekam medis anda: ")
        if nomor_rm in data_pasien:
            print("Nomor rekam medis " + str(nomor_rm) + " sudah ada. Silakan masukkan nomor yang berbeda.")
        else:
            nama = input_teks("Masukkan nama anda: ", "Nama")
            umur = input_angka("Masukkan umur anda: ")
            ruangan = input_teks("Masukkan ruangan anda: ", "Ruangan")
            data_pasien[nomor_rm] = {"nama": nama, "umur": umur, "ruangan": ruangan}
            akun_pengguna[username]["nomor_rm"] = nomor_rm
            print("Data anda berhasil ditambahkan.")


def tampil_data_sendiri(username):
    print()
    print("--Tampilkan data saya--")
    if punya_data(username):
        nomor_rm = akun_pengguna[username]["nomor_rm"]
        data = data_pasien[nomor_rm]
        tabel = PrettyTable()
        tabel.field_names = ["No. RM", "Nama", "Umur", "Ruangan"]
        tabel.add_row([nomor_rm, data["nama"], data["umur"], data["ruangan"]])
        print(tabel)
    else:
        print("Anda belum memiliki data.")


def ubah_data_sendiri(username):
    print()
    print("--Ubah data saya--")
    if punya_data(username):
        nomor_rm = akun_pengguna[username]["nomor_rm"]
        nama = input_teks("Masukkan nama baru anda: ", "Nama")
        umur = input_angka("Masukkan umur baru anda: ")
        ruangan = input_teks("Masukkan ruangan baru anda: ", "Ruangan")
        data_pasien[nomor_rm] = {"nama": nama, "umur": umur, "ruangan": ruangan}
        print("Data anda berhasil diubah.")
    else:
        print("Anda belum memiliki data.")


# FUNCTION MENU PER ROLE 
def menu_admin():
    while True:
        print("================================")
        print("        MENU ADMIN ")
        print("================================")
        print("1. Tambah data pasien")
        print("2. Tampilkan seluruh data pasien")
        print("3. Ubah data pasien")
        print("4. Hapus data pasien")
        print("5. Logout")
        pilihan = input("Masukkan pilihan anda (1/2/3/4/5): ")

        if pilihan == "1":
            tambah_pasien()
        elif pilihan == "2":
            tampil_pasien()
        elif pilihan == "3":
            ubah_pasien()
        elif pilihan == "4":
            hapus_pasien()
        elif pilihan == "5":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")


def menu_pasien(username):
    while True:
        print("================================")
        print("          MENU PASIEN ")
        print("================================")
        print("1. Tambah data saya")
        print("2. Tampilkan data saya")
        print("3. Ubah data saya")
        print("4. Logout")
        pilihan = input("Masukkan pilihan anda (1/2/3/4): ")

        if pilihan == "1":
            tambah_data_sendiri(username)
        elif pilihan == "2":
            tampil_data_sendiri(username)
        elif pilihan == "3":
            ubah_data_sendiri(username)
        elif pilihan == "4":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")


# PROGRAM UTAMA
def main():
    print(" Database pasien opname rumah sakit")
    while True:
        print("================================")
        print("          MENU UTAMA ")
        print("================================")
        print("1. Login")
        print("2. Keluar")
        pilihan = input("Masukkan pilihan anda (1/2): ")

        if pilihan == "1":
            username = login()
            if username is not None:
                role = akun_pengguna[username]["role"]
                if role == "admin":
                    menu_admin()
                elif role == "user":
                    menu_pasien(username)
        elif pilihan == "2":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

try:
    main()
except KeyboardInterrupt:
    print("\nProgram dihentikan oleh pengguna.")