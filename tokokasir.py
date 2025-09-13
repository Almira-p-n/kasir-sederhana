import time

# pernyataan
# list
Bproduk = ["Beras", "Air Mineral", "Minyak", "Es Krim", "Gula", "Garam", "Mie Instan", "Pasta Gigi", "Sikat Gigi", "Deterjen"]
Hproduk = [65000, 3000, 10000, 4000, 27000, 2000, 3000, 8000, 5000, 20000]
keranjang = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# diskon
diskontigaratus = 15
diskonseratus = 5

# pembukaan
print("Selamat datang di toko kami!\n")

# tuku-tuku
run = True
while run:
    print("Silahkan pilih kode barang yang akan dibeli")

    print(
    "0.", Bproduk[0], ":", Hproduk[0],"\n" 
    "1.", Bproduk[1], ":", Hproduk[1],"\n"
    "2.", Bproduk[2], ":", Hproduk[2],"\n"
    "3.", Bproduk[3], ":", Hproduk[3],"\n"
    "4.", Bproduk[4], ":", Hproduk[4],"\n"
    "5.", Bproduk[5], ":", Hproduk[5],"\n"
    "6.", Bproduk[6], ":", Hproduk[6],"\n"
    "7.", Bproduk[7], ":", Hproduk[7],"\n"
    "8.", Bproduk[8], ":", Hproduk[8],"\n"
    "9.", Bproduk[9], ":", Hproduk[9])

    print("Silahkan masukkan kode barang yang akan dibeli:")

    #-----------#
    kode = int(input())
    if kode == kode:
        keranjang[kode] += 1

    print("\n Ingin membeli barang lagi? (y/t)")
    lagi = input()
    if lagi != "y":
        run = False

# total
total = (Hproduk[0] * keranjang[0] +
         Hproduk[1] * keranjang[1] +
         Hproduk[2] * keranjang[2] +
         Hproduk[3] * keranjang[3] +
         Hproduk[4] * keranjang[4] +
         Hproduk[5] * keranjang[5] +
         Hproduk[6] * keranjang[6] +
         Hproduk[7] * keranjang[7] +
         Hproduk[8] * keranjang[8] +
         Hproduk[9] * keranjang[9])

print("Total belanjaan anda:\n", total)

# bayar
# total belanja lebih dari 300000
if total >= 300000:
    if total > 300000:
        print("Belanjaan anda melebihi 300000, Anda akan mendapatkan diskon 15%")
    else:
        print("Belanjaan anda mencapai 300000, Anda akan mendapatkan diskon 15%")

    # dapat diskon
    diskontigaratus = total * diskontigaratus / 100
    print("Total diskon yang anda dapatkan:", diskontigaratus)

    # total setelah diskon
    diskontotal = total - diskontigaratus
    print("Total harga setelah diskon:", diskontotal)

    # bayar!!
    print("Silahkan bayar sesuai total harga")
    # kalo uangnya kurang
    run = True
    while run:
        bayar = int(input())
        if bayar < diskontotal:
            print("Uang anda kurang, bayar sesuai dengan total:", diskontotal)
        else:
            run = False
    # kalo uangnya lebih
    if bayar > diskontotal:
        kembalian = bayar - diskontotal
        print("Kembalian anda:", kembalian)
    else:
        print("Uang pas, tidak ada kembalian")

# total belanja lebih dari 100000
elif total >= 100000 and total < 300000:
    if total > 100000:
        print("Belanjaan anda melebihi 100000, Anda akan mendapatkan diskon 5%")
    else:
        print("Belanjaan anda mencapai 100000, Anda akan mendapatkan diskon 5%")

    # dapat diskon
    diskonseratus = total * diskonseratus / 100
    print("Total diskon yang anda dapatkan:", diskonseratus)

    # total setelah diskon
    diskontotal = total - diskonseratus
    print("Total harga setelah diskon:", diskontotal)

    # bayar!!
    print("Silahkan bayar sesuai total harga")
    # kalo uangnya kurang
    run = True
    while run:
        bayar = int(input())
        if bayar < diskontotal:
            print("Uang anda kurang, bayar sesuai dengan total:", diskontotal)
        else:
            run = False
    # kalo uangnya lebih
    if bayar > diskontotal:
        kembalian =  bayar - diskontotal
        print("Kembalian anda:", kembalian)
    else:
        print("Uang pas, tidak ada kembalian")

# total belnja kurang dari 100000 dan 300000
else:
    # bayar!!
    print("Silahkan bayar sesuai total harga")
    # kalo uangnya kurang
    run = True
    while run:
        bayar = int(input())
        if bayar < total:
            print("Uang anda kurang, bayar sesuai dengan total:", total)
        else:
            run = False
    # kalo uangnya lebih
    if bayar > total:
        kembalian = bayar - total
        print("Kembalian anda:", kembalian)
    else:
        print("Uang pas, tidak ada kembalian")

print("Terimakasih sudah berbelanja di toko kami!")
time.sleep(2)