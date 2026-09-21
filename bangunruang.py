def hitung_kubus(sisi):
    volume = sisi * sisi * sisi
    luas_permukaan = 6 * (sisi * sisi)

    return volume, luas_permukaan


def hitung_balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    luas_permukaan = 2 * (
        panjang * lebar +
        panjang * tinggi +
        lebar * tinggi
    )

    return volume, luas_permukaan