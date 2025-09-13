import time

# potongan
potonganthr = 3
potongankes = 2

# gaji
gajibersih = 0
gajiperbulan = 0

# loop
run = True
while run:
    # input nama
    print("Masukkan nama karyawan")
    namakaryawan = input()
    print("Halo!", namakaryawan)

    # input gaji
    print("Masukkan gaji perbulan")
    gajiperbulan = int(input())
    print("Total gaji kotor", gajiperbulan)

    # potongan thr
    jumlahpotonganthr = gajiperbulan * potonganthr / 100
    print("Jumlah potongan THR", jumlahpotonganthr)

    # potongan kesehatan
    jumlahpotongankes = gajiperbulan * potongankes / 100
    print("Jumlah potongan kesehatan", jumlahpotongankes)

    # total gaji bersih
    gajibersih = gajiperbulan - (jumlahpotonganthr + jumlahpotongankes)
    print("Total gaji bersih perbulan", gajibersih)

    # total gaji 1 tahun setelah dapat potongan
    gajibersih *= 12
    print("Total gaji 1 tahun", gajibersih)

    # total gaji 1 tahun melebihi Rp54.000.000
    if gajibersih >= 54000000:
        # punya npwp
        print("Apakah anda memiliki NPWP? (y/t)")
        print("Jika anda mamiliki NPWP anda akan mendapatkan potongan pajak sebesar 15%\n" \
        "Jika tidak memiliki NPWP anda akan mendapatkan potongan pajak sebesar 20%")
        NPWP = input()
        if NPWP == "y":
            print("Anda mendapatkan potongan pajak sebesar 15%")
            ppp = gajibersih * 15 / 100
            print("Pajak yang akan anda bayar pertahunnya adalah", ppp)
            gajibersih -= ppp
            print("Total gaji bersih yang anda terima seteleah dipotong pajak adalah", gajibersih)
        else:
            print("Anda mendapatkan potongan pajak sebesar 20%")
            ppp = gajibersih * 20 / 100
            print("Pajak yang akan anda bayar pertahunnya adalah", ppp)
            gajibersih -= ppp
            print("Total gaji bersih yang anda terima seteleah dipotong pajak adalah", gajibersih)
    print("Total gaji perbulan", gajibersih / 12)

    # ingin menghitung gaji lagi?
    print("Apakah ingin menghitung gaji lagi? (y/t)")
    tanya = input()
    if tanya != "y":
        run = False

    # penutup
    print("Terimakasih")

time.sleep(2)
