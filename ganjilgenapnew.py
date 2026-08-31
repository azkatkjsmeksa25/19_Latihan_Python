while True:
    # progam cek bialngan ganjilgenap
    angka = int(input("Masukkan sebuah bilangan: "))

    if angka % 2 == 0:
        print(angka, "adalah bilangan Genap")

    else:
        print(angka, "adalah bilangan Ganjil")

    tombol = input("Tekan 'x' untuk keluar atau tekan tombol lain untuk melanjutkan: ")

    if tombol == "x":
        break