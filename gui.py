import tkinter as tk
from tkinter import messagebox

from database import login, buat_akun
from bangundatar import hitung_persegi, hitung_persegi_panjang
from bangunruang import hitung_kubus, hitung_balok


# =====================================
# WINDOW UTAMA
# =====================================

root = tk.Tk()
root.title("Aplikasi Matematika")
root.geometry("500x500")
root.resizable(False, False)


# =====================================
# FUNGSI MEMBERSIHKAN WINDOW
# =====================================

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


# =====================================
# HALAMAN LOGIN
# =====================================

def halaman_login():
    clear_window()

    tk.Label(
        root,
        text="LOGIN",
        font=("Arial", 24, "bold")
    ).pack(pady=30)

    tk.Label(
        root,
        text="Username"
    ).pack()

    entry_username = tk.Entry(root, width=30)
    entry_username.pack(pady=5)

    tk.Label(
        root,
        text="Password"
    ).pack()

    entry_password = tk.Entry(
        root,
        width=30,
        show="*"
    )
    entry_password.pack(pady=5)

    def proses_login():
        username = entry_username.get()
        password = entry_password.get()

        if username == "" or password == "":
            messagebox.showwarning(
                "Peringatan",
                "Username dan password harus diisi!"
            )
            return

        if login(username, password):
            messagebox.showinfo(
                "Login",
                "Login berhasil!\nSelamat datang, " + username
            )
            halaman_menu()
        else:
            messagebox.showerror(
                "Login",
                "Username atau password salah!"
            )

    tk.Button(
        root,
        text="LOGIN",
        width=25,
        command=proses_login
    ).pack(pady=15)

    tk.Button(
        root,
        text="BUAT AKUN",
        width=25,
        command=halaman_buat_akun
    ).pack(pady=5)

    tk.Button(
        root,
        text="KELUAR",
        width=25,
        command=root.destroy
    ).pack(pady=5)


# =====================================
# HALAMAN BUAT AKUN
# =====================================

def halaman_buat_akun():
    clear_window()

    tk.Label(
        root,
        text="BUAT AKUN",
        font=("Arial", 24, "bold")
    ).pack(pady=30)

    tk.Label(
        root,
        text="Username Baru"
    ).pack()

    entry_username = tk.Entry(root, width=30)
    entry_username.pack(pady=5)

    tk.Label(
        root,
        text="Password Baru"
    ).pack()

    entry_password = tk.Entry(
        root,
        width=30,
        show="*"
    )
    entry_password.pack(pady=5)

    def proses_buat_akun():
        username = entry_username.get()
        password = entry_password.get()

        if username == "" or password == "":
            messagebox.showwarning(
                "Peringatan",
                "Username dan password harus diisi!"
            )
            return

        if buat_akun(username, password):
            messagebox.showinfo(
                "Akun",
                "Akun berhasil dibuat!"
            )
            halaman_login()
        else:
            messagebox.showerror(
                "Akun",
                "Username sudah digunakan!"
            )

    tk.Button(
        root,
        text="BUAT AKUN",
        width=25,
        command=proses_buat_akun
    ).pack(pady=15)

    tk.Button(
        root,
        text="KEMBALI",
        width=25,
        command=halaman_login
    ).pack()


# =====================================
# MENU UTAMA
# =====================================

def halaman_menu():
    clear_window()

    tk.Label(
        root,
        text="MENU UTAMA",
        font=("Arial", 24, "bold")
    ).pack(pady=35)

    tk.Button(
        root,
        text="BANGUN DATAR",
        width=30,
        height=2,
        command=menu_bangun_datar
    ).pack(pady=10)

    tk.Button(
        root,
        text="BANGUN RUANG",
        width=30,
        height=2,
        command=menu_bangun_ruang
    ).pack(pady=10)

    tk.Button(
        root,
        text="LOGOUT",
        width=30,
        command=halaman_login
    ).pack(pady=20)


# =====================================
# MENU BANGUN DATAR
# =====================================

def menu_bangun_datar():
    clear_window()

    tk.Label(
        root,
        text="BANGUN DATAR",
        font=("Arial", 22, "bold")
    ).pack(pady=35)

    tk.Button(
        root,
        text="HITUNG PERSEGI",
        width=30,
        height=2,
        command=gui_persegi
    ).pack(pady=10)

    tk.Button(
        root,
        text="HITUNG PERSEGI PANJANG",
        width=30,
        height=2,
        command=gui_persegi_panjang
    ).pack(pady=10)

    tk.Button(
        root,
        text="KEMBALI",
        width=30,
        command=halaman_menu
    ).pack(pady=20)


# =====================================
# GUI PERSEGI
# =====================================

def gui_persegi():
    clear_window()

    tk.Label(
        root,
        text="HITUNG PERSEGI",
        font=("Arial", 22, "bold")
    ).pack(pady=30)

    tk.Label(
        root,
        text="Panjang Sisi"
    ).pack()

    entry_sisi = tk.Entry(root, width=30)
    entry_sisi.pack(pady=10)

    label_hasil = tk.Label(
        root,
        text="",
        font=("Arial", 12)
    )
    label_hasil.pack(pady=15)

    def proses_hitung():
        try:
            sisi = float(entry_sisi.get())

            luas, keliling = hitung_persegi(sisi)

            label_hasil.config(
                text=f"Luas       : {luas}\n"
                     f"Keliling   : {keliling}"
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Masukkan angka yang benar!"
            )

    tk.Button(
        root,
        text="HITUNG",
        width=25,
        command=proses_hitung
    ).pack(pady=10)

    tk.Button(
        root,
        text="KEMBALI",
        width=25,
        command=menu_bangun_datar
    ).pack()


# =====================================
# GUI PERSEGI PANJANG
# =====================================

def gui_persegi_panjang():
    clear_window()

    tk.Label(
        root,
        text="HITUNG PERSEGI PANJANG",
        font=("Arial", 20, "bold")
    ).pack(pady=25)

    tk.Label(root, text="Panjang").pack()

    entry_panjang = tk.Entry(root, width=30)
    entry_panjang.pack(pady=5)

    tk.Label(root, text="Lebar").pack()

    entry_lebar = tk.Entry(root, width=30)
    entry_lebar.pack(pady=5)

    label_hasil = tk.Label(
        root,
        text="",
        font=("Arial", 12)
    )
    label_hasil.pack(pady=15)

    def proses_hitung():
        try:
            panjang = float(entry_panjang.get())
            lebar = float(entry_lebar.get())

            luas, keliling = hitung_persegi_panjang(
                panjang,
                lebar
            )

            label_hasil.config(
                text=f"Luas       : {luas}\n"
                     f"Keliling   : {keliling}"
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Masukkan angka yang benar!"
            )

    tk.Button(
        root,
        text="HITUNG",
        width=25,
        command=proses_hitung
    ).pack(pady=10)

    tk.Button(
        root,
        text="KEMBALI",
        width=25,
        command=menu_bangun_datar
    ).pack()


# =====================================
# MENU BANGUN RUANG
# =====================================

def menu_bangun_ruang():
    clear_window()

    tk.Label(
        root,
        text="BANGUN RUANG",
        font=("Arial", 22, "bold")
    ).pack(pady=35)

    tk.Button(
        root,
        text="HITUNG KUBUS",
        width=30,
        height=2,
        command=gui_kubus
    ).pack(pady=10)

    tk.Button(
        root,
        text="HITUNG BALOK",
        width=30,
        height=2,
        command=gui_balok
    ).pack(pady=10)

    tk.Button(
        root,
        text="KEMBALI",
        width=30,
        command=halaman_menu
    ).pack(pady=20)


# =====================================
# GUI KUBUS
# =====================================

def gui_kubus():
    clear_window()

    tk.Label(
        root,
        text="HITUNG KUBUS",
        font=("Arial", 22, "bold")
    ).pack(pady=30)

    tk.Label(
        root,
        text="Panjang Sisi"
    ).pack()

    entry_sisi = tk.Entry(root, width=30)
    entry_sisi.pack(pady=10)

    label_hasil = tk.Label(
        root,
        text="",
        font=("Arial", 12)
    )
    label_hasil.pack(pady=15)

    def proses_hitung():
        try:
            sisi = float(entry_sisi.get())

            volume, luas_permukaan = hitung_kubus(sisi)

            label_hasil.config(
                text=f"Volume           : {volume}\n"
                     f"Luas Permukaan   : {luas_permukaan}"
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Masukkan angka yang benar!"
            )

    tk.Button(
        root,
        text="HITUNG",
        width=25,
        command=proses_hitung
    ).pack(pady=10)

    tk.Button(
        root,
        text="KEMBALI",
        width=25,
        command=menu_bangun_ruang
    ).pack()


# =====================================
# GUI BALOK
# =====================================

def gui_balok():
    clear_window()

    tk.Label(
        root,
        text="HITUNG BALOK",
        font=("Arial", 22, "bold")
    ).pack(pady=25)

    tk.Label(root, text="Panjang").pack()

    entry_panjang = tk.Entry(root, width=30)
    entry_panjang.pack(pady=5)

    tk.Label(root, text="Lebar").pack()

    entry_lebar = tk.Entry(root, width=30)
    entry_lebar.pack(pady=5)

    tk.Label(root, text="Tinggi").pack()

    entry_tinggi = tk.Entry(root, width=30)
    entry_tinggi.pack(pady=5)

    label_hasil = tk.Label(
        root,
        text="",
        font=("Arial", 12)
    )
    label_hasil.pack(pady=15)

    def proses_hitung():
        try:
            panjang = float(entry_panjang.get())
            lebar = float(entry_lebar.get())
            tinggi = float(entry_tinggi.get())

            volume, luas_permukaan = hitung_balok(
                panjang,
                lebar,
                tinggi
            )

            label_hasil.config(
                text=f"Volume           : {volume}\n"
                     f"Luas Permukaan   : {luas_permukaan}"
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Masukkan angka yang benar!"
            )

    tk.Button(
        root,
        text="HITUNG",
        width=25,
        command=proses_hitung
    ).pack(pady=10)

    tk.Button(
        root,
        text="KEMBALI",
        width=25,
        command=menu_bangun_ruang
    ).pack()


# =====================================
# MENJALANKAN GUI
# =====================================

halaman_login()

root.mainloop()