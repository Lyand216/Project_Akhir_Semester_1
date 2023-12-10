import math

list_bangun_datar = ["Persegi", "Persegi panjang","Belah ketupat", "Jajar genjang", "lingkaran"]

rumus_luas_bangun_datar = {
    "p": "s x s\nKet :\ns : sisi persegi",
    "pp": "p x l\nKet :\np : panjang\nl : lebar",
    "bk": "0.5 x d1 x d2\nKet :\nd1 : diagonal 1\nd2 : diagonal 2",
    "jg": "a x t\nKet :\na : alas\nt : tinggi",
    "l": "phi x r x r\nKet :\nr : jari-jari"
}

rumus_keliling_bangun_datar = {
    "p": "s x 4\nKet :\ns : sisi persegi",
    "pp": "(p x 2) + (l x 2)\nKet :\np : panjang\nl : lebar",
    "bk": "(d1 x 2) + (d2 x 2)\nKet :\nd1 : diagonal 1\nd2 : diagonal 2",
    "jg": "(a x 2) + (t x 2)\nKet :\na : alas\nt : tinggi",
    "l": "2 x phi x r\nKet :\nphi : 3,14 atau 22/7\nr : jari-jari"
}


def garis():
    garis = print("-"*40)
    return garis


def persegi():
    garis()
    print("Anda memilih ", list_bangun_datar[0])
    print("1. Luas")
    print("2. Keliling")
    while True:
        pilih = input("Pilih (1/2) : ")

        if pilih == '1':
            garis()
            print("Rumus :", rumus_luas_bangun_datar["p"])
            sisi = int(input("Masukkan nilai sisi (cm): "))
            luas = sisi ** 2
            return print(f"Luas persegi = {luas} cm")

        elif pilih == '2':
            garis()
            print("Rumus :", rumus_keliling_bangun_datar["p"])
            sisi = int(input("Masukkan nilai sisi (cm): "))
            keliling = sisi * 4
            return print(f"Keliling persegi : {keliling} cm")

        else:
            print("Pilihan tidak valid")
            continue


def persegi_panjang():
    garis()
    print("Anda memilih ", list_bangun_datar[1])
    print("1. Luas")
    print("2. Keliling")
    while True:
        pilih = input("Pilih (1/2) : ")

        if pilih == '1':
            garis()
            print("Rumus :", rumus_luas_bangun_datar["pp"])
            panjang = int(input("Masukkan nilai panjang : "))
            lebar = int(input("Masukkan nilai lebar : "))
            luas = panjang * lebar
            return print(f"Luas persegi panjang = {luas} cm")

        elif pilih == '2':
            garis()
            print("Rumus :", rumus_keliling_bangun_datar["pp"])
            panjang = int(input("Masukkan nilai panjang : "))
            lebar = int(input("Masukkan nilai lebar : "))
            keliling = (panjang * 2) + (lebar * 2)
            return print(f"Keliling persegi panjang : {keliling} cm")

        else:
            print("Pilihan tidak valid")
            continue


def belah_ketupat():
    garis()
    print("Anda memilih ", list_bangun_datar[2])
    print("1. Luas")
    print("2. Keliling")
    while True:
        pilih = input("Pilih (1/2) : ")

        if pilih == '1':
            garis()
            print("Rumus :", rumus_luas_bangun_datar["bk"])
            diagonal1 = int(input("Masukkan nilai diagonal 1 : "))
            diagonal2 = int(input("Masukkan nilai diagonal 2 : "))
            luas = 0.5 * diagonal1 * diagonal2
            return print(f"Luas belah ketupat = {luas} cm")

        elif pilih == '2':
            garis()
            print("Rumus :", rumus_keliling_bangun_datar["bk"])
            diagonal1 = int(input("Masukkan nilai diagonal 1 : "))
            diagonal2 = int(input("Masukkan nilai diagonal 2 : "))
            keliling = (diagonal1 * 2) + (diagonal2 * 2)
            return print(f"Keliling belah ketupat : {keliling} cm")

        else:
            print("Pilihan tidak valid")
            continue


def jajar_genjang():
    garis()
    print("Anda memilih ", list_bangun_datar[3])
    print("1. Luas")
    print("2. Keliling")
    while True:
        pilih = input("Pilih (1/2) : ")

        if pilih == '1':
            garis()
            print("Rumus :", rumus_luas_bangun_datar["jg"])
            alas = int(input("Masukkan nilai alas : "))
            tinggi = int(input("Masukkan nilai tinggi : "))
            luas = alas * tinggi
            return print(f"Luas jajar genjang = {luas} cm")

        elif pilih == '2':
            garis()
            print("Rumus :", rumus_keliling_bangun_datar["jg"])
            alas = int(input("Masukkan nilai alas : "))
            tinggi = int(input("Masukkan nilai tinggi : "))
            keliling = (alas * 2) + (tinggi * 2)
            return print(f"Keliling jajar genjang {keliling} cm")

        else:
            print("Pilihan tidak valid")
            continue


def lingkaran():
    garis()
    print("Anda memilih ", list_bangun_datar[4])
    print("1. Luas")
    print("2. Keliling")
    while True:
        pilih = input("Pilih (1/2) : ")

        if pilih == '1':
            garis()
            print("Rumus :", rumus_luas_bangun_datar["l"])
            jari = int(input("Masukkan nilai jari-jari : "))
            luas = math.pi * jari ** 2
            return print(f"Luas lingkaran = {round(luas,2)} cm")

        elif pilih == '2':
            garis()
            print("Rumus :", rumus_keliling_bangun_datar["l"])
            jari = int(input("Masukkan nilai jari-jari : "))
            keliling = 2 * math.pi * jari
            return print(f"Keliling lingkaran : {round(keliling,2)} cm")

        else:
            print("Pilihan tidak valid")
            continue
