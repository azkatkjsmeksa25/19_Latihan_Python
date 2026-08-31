def hitung_persegi():
    print("--- Hitung Persegi ---")
    sisi = float(input("Panjang sisi: "))

    luas = sisi * sisi
    keliling = sisi + sisi + sisi + sisi

    print(f"Luas persegi   : {luas}")
    print(f"Keliling persegi: {keliling}")


def hitung_persegi_panjang():
    print("--- Hitung Persegi Panjang ---")
    panjang = float(input("Panjang: "))
    lebar = float(input("Lebar  : "))

    luas = panjang * lebar
    keliling = 2 * panjang + 2 * lebar

    print(f"Luas persegi panjang    : {luas}")
    print(f"Keliling persegi panjang: {keliling}")