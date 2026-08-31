import ganjilgenapnew
import bangundatar
import bangunruang

DAFTAR_MENU = {
    "1": ("Cek Bilangan Ganjil/Genap", ganjilgenapnew.cek_bilangan),
    "2": ("Cek Bilangan Prima", ganjilgenapnew.cek_prima),
    "3": ("Hitung Persegi", bangundatar.hitung_persegi),
    "4": ("Hitung Persegi Panjang", bangundatar.hitung_persegi_panjang),
    "5": ("Hitung Kubus", bangunruang.hitung_kubus),
    "6": ("Hitung Balok", bangunruang.hitung_balok),
}

def tampilkan_menu():
    garis = "=" * 25
    print("\n" + garis)
    print(" MENU UTAMA")
    print(garis)
    for kode, (nama, _) in DAFTAR_MENU.items():
        print(f"{kode}. {nama}")
    print("7. Keluar")
    print(garis)

def jalankan():
    aktif = True
    while aktif:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-7): ").strip()

        if pilihan == "7":
            print("Program selesai.")
            aktif = False
        elif pilihan in DAFTAR_MENU:
            _, fungsi = DAFTAR_MENU[pilihan]
            fungsi()
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    jalankan()