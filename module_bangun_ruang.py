import math

list_bangun_ruang = ["Kubus", "Balok", "Limas", "Prisma", "Tabung"]
list_limas = ["Limas segitiga", "Limas segiempat", "Limas segilima"]
list_prisma = ["Prisma segitiga", "Prisma segiempat", "Prisma segilima"]

# Rumus luas permukaan bangun ruang
rumus_volume_bangun_ruang = {
    "k": "s x s x s\nKet :\ns : sisi kubus",
    "b": "p x l x t\nKet :\np : panjang\nl : lebar\nt : tinggi",
    "l": "1/3 x a x t\nKet :\na : alas\nt : tinggi",
    "p": "a x t\nKet :\na : alas\nt : tinggi",
    "t": "a x t\nKet :\na : alas\nt : tinggi"
}

rumus_selimut_bangun_ruang = {
    "k": "s x 6\nKet :\ns : sisi kubus",
    "b": "(2 x p x l) + (2 x p x t) + (2 x l x t)\nKet :\np : panjang\nl : lebar\nt : tinggi",
    "l3": "La + (3 x Lst)\nKet :\nLa : Luas alas\nLst : Luas sisi tegak limas",
    "l4": "La + (4 x Lst)\nKet :\nLa : Luas alas\nLst : Luas sisi tegak limas",
    "l5": "La + (5 x Lst)\nKet :\nLa : Luas alas\nLst : Luas sisi tegak limas",
    "p3": "(2 x La) + (Ka x t) atau\n(2 x La) + (3 x Lst)\nKet :\nLa : Luas alas\nKa : Keliling alas\nt : tinggi prisma\nLst : Luas sisi tegak",
    "p4": "(2 x La) + (Ka x t) atau\n(2 x La) + (4 x Lst)\nKet :\nLa : Luas alas\nKa : Keliling alas\nt : tinggi prisma\nLst : Luas sisi tegak",
    "p5": "(2 x La) + (Ka x t) atau\n(2 x La) + (5 x Lst)\nKet :\nLa : Luas alas\nKa : Keliling alas\nt : tinggi prisma\nLst : Luas sisi tegak",
    "t": "2 x phi x r x (r + t)\nKet :\nphi : 3.14 atau 22/7\nr : jari-jari alas / tutup tabung\nt : tinggi tabung"
}


def garis():
    garis = print("-"*40)
    return garis

# fungsi untuk menghitung volume bangun ruang


def kubus():
    garis()
    print("Anda memilih ", list_bangun_ruang[0])
    print("1. Volume")
    print("2. Luas Permukaan")
    while True:
        pilih = input("Pilih (1/2) : ")

        if pilih == "1":
            print("Rumus :", rumus_volume_bangun_ruang["k"])
            sisi = int(input("Masukkan nilai sisi (cm): "))
            volume = sisi**3
            return print(f"Volume kubus = {volume} cm")

        elif pilih == '2':
            print("Rumus :", rumus_selimut_bangun_ruang["k"])
            sisi = int(input("Masukkan nilai sisi (cm): "))
            lp = sisi * 6
            return print(f"Luas permukaan kubus = {round(lp,2)} cm")

        else:
            print("Pilihan tidak valid")
            continue


def balok():
    garis()
    print("Anda memilih ", list_bangun_ruang[1])
    print("1. Volume")
    print("2. Luas Permukaan")
    while True:
        pilih = input("Pilih (1/2) : ")

        if pilih == "1":
            print("Rumus :", rumus_volume_bangun_ruang["b"])
            panjang = int(input("Masukkan nilai panjang (cm): "))
            lebar = int(input("Masukkan nilai lebar (cm): "))
            tinggi = int(input("Masukkan nilai tinggi (cm): "))
            volume = panjang * lebar * tinggi
            return print(f"Volume balok = {volume} cm")

        elif pilih == '2':
            print("Rumus :\n", rumus_selimut_bangun_ruang["b"])
            panjang = int(input("Masukkan nilai panjang (cm): "))
            lebar = int(input("Masukkan nilai lebar (cm): "))
            tinggi = int(input("Masukkan nilai tinggi (cm): "))
            lp = (2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi)
            return print(f"Luas permukaan balok = {round(lp,2)} cm")

        else:
            print("Pilihan tidak valid")
            continue


def limas():
    garis()
    print("Anda memilih ", list_bangun_ruang[2])

    for index, j in enumerate(list_limas):
        print(f"{index+1}. {j}")

    while True:
        pilih_limas = input("Pilih limas : ")

        if pilih_limas == "1":
            garis()
            print("\nAnda memilih ", list_limas[0])
            print("Anda memilih ", list_bangun_ruang[1])
            print("1. Volume")
            print("2. Luas Permukaan")
            while True:
                pilih = input("Pilih (1/2) : ")

                if pilih == '1':
                    print("Rumus :", rumus_volume_bangun_ruang['l'])
                    alas_segitiga = int(input("Alas segitiga : "))
                    tinggi_segitiga = int(input("Tinggi segitiga : "))
                    alas = 1/2 * alas_segitiga * tinggi_segitiga
                    print("Alas limas segitiga = ", round(alas, 2))
                    tinggi = int(input("Tinggi limas : "))
                    volume = 1/3 * alas * tinggi
                    return print(f"Volume limas = {volume:.2f}")

                elif pilih == '2':
                    print("Rumus :\n", rumus_selimut_bangun_ruang['l3'])
                    print("Menghitung luas alas limas")
                    alas_segitiga = int(input("Alas segitiga : "))
                    tinggi_segitiga = int(input("Tinggi segitiga : "))
                    alas = 1/2 * alas_segitiga * tinggi_segitiga
                    print("Alas limas segitiga = ", round(alas, 2))
                    print("Menghitung luas sisi tegak")
                    print("Diketahui alas segitiga = ", alas_segitiga)
                    tinggi_sisi_tegak = int(input("Tinggi sisi tegak : "))
                    luas_sisi_tegak = 1/2 * alas_segitiga * tinggi_sisi_tegak
                    lp = alas + (3 * luas_sisi_tegak)
                    return print(f"Luas permukaan limas = {round(lp,2)} cm")

                else:
                    print("Pilihan tidak valid")
                    continue

        elif pilih_limas == "2":
            garis()
            print("Anda memilih ", list_limas[1])
            print("Anda memilih ", list_bangun_ruang[1])
            print("1. Volume")
            print("2. Luas Permukaan")
            while True:
                pilih = input("Pilih (1/2) : ")

                if pilih == '1':
                    print("Rumus :", rumus_volume_bangun_ruang['l'])
                    sisi_alas = int(input("Sisi alas limas : "))
                    alas = sisi_alas ** 2
                    print("Alas limas segi empat = ", round(alas, 2))
                    tinggi = int(input("Tinggi limas : "))
                    volume = 1/3 * alas * tinggi
                    return print(f"Volume limas = {volume:.2f}")

                elif pilih == '2':
                    print("Rumus :\n", rumus_selimut_bangun_ruang['l4'])
                    sisi_alas = int(input("Sisi alas limas : "))
                    alas = sisi_alas ** 2
                    print("Alas limas segi empat = ", round(alas, 2))
                    print("Menghitung luas sisi tegak")
                    print("Diketahui sisi segiempat = ", sisi_alas)
                    tinggi_sisi_tegak = int(input("Tinggi sisi tegak : "))
                    luas_sisi_tegak = 1/2 * sisi_alas * tinggi_sisi_tegak
                    lp = alas + (4 * luas_sisi_tegak)
                    return print(f"Luas permukaan limas = {round(lp,2)} cm")

                else:
                    print("Pilihan tidak valid")
                    continue

        elif pilih_limas == "3":
            garis()
            print("Anda memilih ", list_limas[2])
            print("1. Volume")
            print("2. Luas Permukaan")
            while True:
                pilih = input("Pilih (1/2) : ")

                if pilih == '1':
                    print("Rumus :", rumus_volume_bangun_ruang['l'])
                    sisi_segilima = int(input("Sisi segilima : "))
                    alas = (sisi_segilima ** 2) * \
                        math.sqrt(5 * (5 + 2 * math.sqrt(5))) / 4
                    print("Alas limas segilima = ", round(alas, 2))
                    tinggi = int(input("Tinggi limas : "))
                    volume = 1/3 * alas * tinggi
                    return print(f"Volume limas = {volume:.2f}")

                elif pilih == '2':
                    print("Rumus :\n", rumus_selimut_bangun_ruang['l5'])
                    sisi_segilima = int(input("Sisi segilima : "))
                    alas = (sisi_segilima ** 2) * \
                        math.sqrt(5 * (5 + 2 * math.sqrt(5))) / 4
                    print("Alas limas segi empat = ", round(alas, 2))
                    print("Menghitung luas sisi tegak")
                    print("Diketahui sisi segilima = ", sisi_segilima)
                    tinggi_sisi_tegak = int(input("Tinggi sisi tegak : "))
                    luas_sisi_tegak = 1/2 * sisi_segilima * tinggi_sisi_tegak
                    lp = alas + (5 * luas_sisi_tegak)
                    return print(f"Luas permukaan limas = {round(lp,2)} cm")

                else:
                    print("Pilihan tidak valid")
                    continue

        else:
            print("Pilihan tidak valid")


def prisma():
    garis()
    print("Anda memilih ", list_bangun_ruang[3])
    for index, j in enumerate(list_prisma):
        print(f"{index+1}. {j}")

    while True:
        pilih_prisma = input("Pilih prisma : ")

        if pilih_prisma == "1":
            garis()
            print("Anda memilih ", list_prisma[0])
            print("1. Volume")
            print("2. Luas Permukaan")
            while True:
                pilih = input("Pilih (1/2) : ")

                if pilih == '1':
                    print("Rumus :", rumus_volume_bangun_ruang['p'])
                    alas_segitiga = int(input("Alas segitiga : "))
                    tinggi_segitiga = int(input("Tinggi segitiga : "))
                    alas = 1/2 * alas_segitiga * tinggi_segitiga
                    print("Alas prisma segitiga = ", round(alas, 2))
                    tinggi = int(input("Tinggi prisma : "))
                    volume = alas * tinggi
                    return print(f"Volume prisma = {volume:.2f}")

                elif pilih == '2':
                    print("Rumus :", rumus_selimut_bangun_ruang['p3'])
                    alas_segitiga = int(input("Alas segitiga : "))
                    tinggi_segitiga = int(input("Tinggi segitiga : "))
                    alas = 1/2 * alas_segitiga * tinggi_segitiga
                    print("Alas prisma segitiga = ", round(alas, 2))
                    print("Menghitung luas sisi tegak")
                    print("Diketahui alas segitiga = ", alas_segitiga)
                    tinggi = int(input("Tinggi prisma : "))
                    luas_sisi_tegak = alas_segitiga * tinggi
                    print("Luas sisi tegak = ", luas_sisi_tegak)
                    lp = (2 * alas) + (3 * luas_sisi_tegak)
                    return print(f"Luas permukaan prisma = {round(lp,2)} cm")

                else:
                    print("Pilihan tidak valid")
                    continue

        elif pilih_prisma == "2":
            garis()
            print("Anda memilih ", list_prisma[1])
            print("1. Volume")
            print("2. Luas Permukaan")
            while True:
                pilih = input("Pilih (1/2) : ")
                if pilih == '1':
                    print("Rumus :", rumus_volume_bangun_ruang['p'])
                    sisi_alas = int(input("Sisi alas prisma : "))
                    alas = sisi_alas ** 2
                    print("Alas prisma segi empat = ", round(alas, 2))
                    tinggi = int(input("Tinggi prisma : "))
                    volume = alas * tinggi
                    return print(f"Volume prisma = {volume:.2f}")

                elif pilih == '2':
                    print("Rumus :", rumus_selimut_bangun_ruang['p4'])
                    sisi_alas = int(input("Sisi alas prisma : "))
                    alas = sisi_alas ** 2
                    print("Alas prisma segiempat = ", round(alas, 2))
                    print("Menghitung luas sisi tegak")
                    print("Diketahui sisi alas segiempat = ", sisi_alas)
                    tinggi = int(input("Tinggi prisma : "))
                    luas_sisi_tegak = sisi_alas * tinggi
                    print("Luas sisi tegak = ", luas_sisi_tegak)
                    lp = (2 * alas) + (4 * luas_sisi_tegak)
                    return print(f"Luas permukaan prisma = {round(lp,2)} cm")

                else:
                    print("Pilihan tidak valid")
                    continue

        elif pilih_prisma == "3":
            garis()
            print("Anda memilih ", list_prisma[2])
            print("1. Volume")
            print("2. Luas Permukaan")
            while True:
                pilih = input("Pilih (1/2) : ")

                if pilih == '1':
                    print("Rumus :", rumus_volume_bangun_ruang['p'])
                    sisi_segilima = int(input("Sisi segilima : "))
                    alas = (sisi_segilima ** 2) * \
                        math.sqrt(5 * (5 + 2 * math.sqrt(5))) / 4
                    print("Alas prisma segilima = ", round(alas, 2))
                    tinggi = int(input("Tinggi prisma : "))
                    volume = alas * tinggi
                    return print(f"Volume prisma = {volume:.2f}")

                elif pilih == '2':
                    print("Rumus :", rumus_selimut_bangun_ruang['p5'])
                    sisi_segilima = int(input("Sisi segilima : "))
                    alas = (sisi_segilima ** 2) * \
                        math.sqrt(5 * (5 + 2 * math.sqrt(5))) / 4
                    print("Alas prisma segilima = ", round(alas, 2))
                    print("Menghitung luas sisi tegak")
                    print("Diketahui sisi segilima = ", sisi_segilima)
                    tinggi = int(input("Tinggi prisma : "))
                    luas_sisi_tegak = sisi_segilima * tinggi
                    print("Luas sisi tegak = ", luas_sisi_tegak)
                    lp = (2 * alas) + (5 * luas_sisi_tegak)
                    return print(f"Luas permukaan prisma = {round(lp,2)} cm")

                else:
                    print("Pilihan tidak valid")
                    continue


def tabung():
    garis()
    print("Anda memilih ", list_bangun_ruang[4])
    print("1. Volume")
    print("2. Luas Permukaan")
    while True:
        pilih = input("Pilih (1/2) : ")

        if pilih == '1':
            print("Rumus :", rumus_volume_bangun_ruang['t'])
            jari_lingkaran = int(input("Jari-jari lingkaran : "))
            alas = math.pi * jari_lingkaran ** 2
            print("Luas alas tabung = ", round(alas, 2))
            tinggi = int(input("Tinggi tabung : "))
            volume = alas * tinggi
            return print(f"Volume tabung = {volume:.2f}")

        elif pilih == '2':
            print("Rumus :", rumus_selimut_bangun_ruang['t'])
            jari_jari = int(input("Jari-jari lingkaran : "))
            alas = math.pi * jari_jari ** 2
            print("Luas alas tabung = ", round(alas, 2))
            tinggi = int(input("Tinggi tabung : "))
            lp = 2 * math.pi * jari_jari * (jari_jari + tinggi)
            return print(f"Luas permukaan tabung = {round(lp,2)} cm")

        else:
            print("Pilihan tidak valid")
            continue
