def hitung_kubus():
    print("--- Hitung Kubus ---")
    sisi = float(input("Panjang sisi: "))

    volume = sisi * sisi * sisi
    luas_permukaan = 6 * (sisi * sisi)

    print(f"Volume kubus         : {volume}")
    print(f"Luas permukaan kubus : {luas_permukaan}")


def hitung_balok():
    print("--- Hitung Balok ---")
    panjang = float(input("Panjang: "))
    lebar = float(input("Lebar  : "))
    tinggi = float(input("Tinggi : "))

    volume = panjang * lebar * tinggi
    luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

    print(f"Volume balok         : {volume}")
    print(f"Luas permukaan balok : {luas_permukaan}")