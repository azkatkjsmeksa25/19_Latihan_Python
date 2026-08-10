# Menentukan Apakah Angka Positif, Negatif, atau Nol

while True:
    x = int(input("Silahkan Masukkan Angka: "))

    if x > 0:
        print("Angka", x, "adalah Bilangan Positif")
    elif x < 0:
        print("Angka", x, "adalah Bilangan Negatif")
    else:
        print("Angka", x, "adalah Nol")

    tombol = input("Tekan 'x' untuk keluar atau tekan tombol lain untuk melanjutkan: ")
    if tombol == 'x':
        break