import time

# potongan
potonganthr = 3
potongankes = 2

# gaji
gajibersih = 0
gajiperbulan = 0

# pembukaan
print("Selamat datang di sistem perhitungan gaji")
time.sleep(1)

# loop
run = True
while run:
    # input nama
    print("Masukkan nama anda")
    nama = input()
    time.sleep(0.5)
    print("Halo!", nama)

    time.sleep(1)

    # input gaji
    print("Masukkan gaji perbulan")
    gajiperbulan = int(input())
    # jeda
    time.sleep(0.7)
    print("Total gaji kotor", gajiperbulan)

    time.sleep(0.7)
    print("Anda akan mendapatkan potongan pajak THR dan Kesehatan")
    time.sleep(0.7)

    # potongan thr
    jumlahpotonganthr = gajiperbulan * potonganthr / 100
    print("Jumlah potongan THR", jumlahpotonganthr)
    time.sleep(0.7)

    # potongan kesehatan
    jumlahpotongankes = gajiperbulan * potongankes / 100
    print("Jumlah potongan kesehatan", jumlahpotongankes)
    time.sleep(0.7)

    # total gaji bersih
    gajibersih = gajiperbulan - (jumlahpotonganthr + jumlahpotongankes)
    print("Total gaji bersih perbulan", gajibersih)
    time.sleep(0.7)

    # total gaji 1 tahun setelah dapat potongan
    gajibersih *= 12
    print("Total gaji 1 tahun", gajibersih)
    time.sleep(0.7)

    # total gaji 1 tahun melebihi Rp54.000.000
    if gajibersih >= 54000000:
        # punya npwp
        print("Apakah anda memiliki NPWP? (y/t)")
        time.sleep(0.7)
        print("Jika anda mamiliki NPWP anda akan mendapatkan potongan pajak sebesar 15%\n" \
        "Jika tidak memiliki NPWP anda akan mendapatkan potongan pajak sebesar 20%")
        time.sleep(0.7)
        NPWP = input()
        if NPWP == "y":
            print("Anda mendapatkan potongan pajak sebesar 15%")
            time.sleep(0.7)
            ppp = gajibersih * 15 / 100
            print("Pajak yang akan anda bayar pertahunnya adalah", ppp)
            time.sleep(0.7)
            gajibersih -= ppp
            print("Total gaji bersih yang anda terima seteleah dipotong pajak adalah", gajibersih)
            time.sleep(0.7)
        else:
            print("Anda mendapatkan potongan pajak sebesar 20%")
            time.sleep(0.7)
            ppp = gajibersih * 20 / 100
            print("Pajak yang akan anda bayar pertahunnya adalah", ppp)
            time.sleep(0.7)
            gajibersih -= ppp
            print("Total gaji bersih yang anda terima seteleah dipotong pajak adalah", gajibersih)
            time.sleep(0.7)
    print("Total gaji perbulan", gajibersih / 12)
    time.sleep(0.7)

    # ingin menghitung gaji lagi?
    print("Apakah ingin menghitung gaji lagi? (y/t)")
    tanya = input()
    if tanya != "y":
        run = False

    time.sleep(0.7)
    
    # penutup
    print("Terimakasih")

time.sleep(2)
