# Program Menentukan Bilangan Ganjil atau Genap
while True:
    angka = int(input("Masukkan sebuah angka: "))

    if angka % 2 == 0:
        print("Angka", angka, "adalah bilangan Genap")
    else:
        print("Angka", angka, "adalah bilangan Ganjil")
    terus = str(input("Apakah Anda ingin memasukkan angka lagi? (y/n): "))
    if terus == "y":
        continue 
    else:
        print("Terima kasih telah menggunakan program ini.")
        break  