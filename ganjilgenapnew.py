def cek_bilangan():
    print("--- Cek Ganjil / Genap ---")
    teks = input("Masukkan sebuah bilangan bulat: ")
    angka = int(teks)

    status = "GENAP" if angka % 2 == 0 else "GANJIL"
    print(f"Angka {angka} termasuk bilangan {status}.")


def cek_prima():
    print("--- Cek Bilangan Prima ---")
    teks = input("Masukkan bilangan bulat: ")
    angka = int(teks)

    hasil = True
    if angka < 2:
        hasil = False
    else:
        akar = int(angka ** 0.5) + 1
        for pembagi in range(2, akar):
            if angka % pembagi == 0:
                hasil = False
                break

    if hasil:
        print(f"{angka} adalah bilangan PRIMA.")
    else:
        print(f"{angka} BUKAN bilangan prima.")