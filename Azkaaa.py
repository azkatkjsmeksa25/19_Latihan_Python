import random

print("=" * 30)
print("🎮 SELAMAT DATANG DI GAME TEBAK ANGKA")
print("=" * 30)

angka_rahasia = random.randint(1, 100)
percobaan = 0

while True:
    try:
        tebakan = int(input("Masukkan tebakanmu (1-100): "))
        percobaan += 1

        if tebakan < angka_rahasia:
            print("⬆️ Terlalu kecil!")
        elif tebakan > angka_rahasia:
            print("⬇️ Terlalu besar!")
        else:
            print(f"\n🎉 Selamat! Kamu berhasil menebak angka {angka_rahasia}.")
            print(f"Jumlah percobaan: {percobaan}")
            break

    except ValueError:
        print("Masukkan angka yang valid!")