
import os
import module_bangun_datar as mbd
import module_bangun_ruang as mbr


teks_judul1 = "* Kalkulator bangun ruang *"
teks_judul2 = "* dan bangun datar *"

# inputan pilihan user


def pilihan_user():
    pilihan = input("Pilih : ")
    print("-"*40)

    if pilihan == "1":
        print("=> Menu Bangun Datar <=".center(40))
        print("-"*40)
        # for untuk menampilkan list menu bangun datar
        for index, i in enumerate(mbd.list_bangun_datar):
            print(f"{index+1}. {i}")
        else:
            print("-"*40)

        # memilih bangun datar yg ada di menu
        while True:
            bangun_datar = input("Pilih bangun datar : ")

            if bangun_datar == "1":
                mbd.persegi()
                break
            elif bangun_datar == "2":
                mbd.persegi_panjang()
                break
            elif bangun_datar == "3":
                mbd.belah_ketupat()
                break
            elif bangun_datar == "4":
                mbd.jajar_genjang()
                break
            elif bangun_datar == "5":
                mbd.lingkaran()
                break
            else:
                print("Pilihan tidak valid")
                continue

    elif pilihan == "2":
        print("=> Menu Bangun Ruang <=".center(40))
        print("-"*40)
        # for untuk menampilkan list menu bangun ruang
        for index, i in enumerate(mbr.list_bangun_ruang):
            print(f"{index+1}. {i}")
        else:
            print("-"*40)
        while True:
            bangun_ruang = (input("Pilih bangun ruang : "))

            if bangun_ruang == "1":
                mbr.kubus()
                break
            elif bangun_ruang == "2":
                mbr.balok()
                break
            elif bangun_ruang == "3":
                mbr.limas()
                break
            elif bangun_ruang == "4":
                mbr.prisma()
                break
            elif bangun_ruang == "5":
                mbr.tabung()
                break
            else:
                print("Pilihan tidak valid")
                continue
    else:
        print("Pilihan invalid")


def garis():
    garis = print("-"*40)
    return garis


while True:
    os.system("cls")
    # menampilkan header dan menu
    # header_menu()
    print("="*40)
    print(teks_judul1.upper().center(40))
    print(teks_judul2.upper().center(40))
    print("="*40)
    # menu
    print("Menu :")
    print("1. Bangun Datar")
    print("2. Bangun Ruang")
    garis()
    # fungsi untuk memberikan pilihan pada user dan memproses perhitungan
    # user memilih bangun ruang atau bangun datar dan memproses perhitungan
    pilihan_user()

    lanjut = input("lanjut ? (y/n) : ")
    if lanjut == "n":
        print("Program selesai")
        break
