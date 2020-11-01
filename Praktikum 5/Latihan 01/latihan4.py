kodeKaryawan = input("Masukkan kode karyawan : ")
namaKaryawan = input("Masukkan nama karyawan : ")
golongan = input("Masukkan golongan : ")

if(golongan == "A"):
    gajiPokok = 10000000
    potongan = 2.5
    jumlahPotongan = 2.5 / 100 * 10000000
    gajiBersih = 10000000 - jumlahPotongan
elif(golongan == "B"):
    gajiPokok = 8500000
    potongan = 2.0
    jumlahPotongan = 2. / 100 * 8500000
    gajiBersih = 8500000 - jumlahPotongan
elif(golongan == "C"):
    gajiPokok = 7000000
    potongan = 1.5
    jumlahPotongan = 1.5 / 100 * 7000000
    gajiBersih = 10000000 - jumlahPotongan
elif(golongan == "D"):
    gajiPokok = 5500000
    potongan = 1.0
    jumlahPotongan = 1.0 / 100 * 5500000
    gajiBersih = 5500000 - jumlahPotongan
    

print("====================================")

print("STRUK RINCIAN GAJI KARYAWAN")

print("-----------------------------------------------------------")

print("Nama Karyawan : " + namaKaryawan + "(Kode Karyawan : " + str(kodeKaryawan) + ")")
print("Golongan : " + golongan)

print("-----------------------------------------------------------")

print("Gaji Pokok : Rp" + str(gajiPokok))
print("Potongan (" + str(potongan) + "%): Rp" + str(jumlahPotongan))

print("-----------------------------------------------------------")

print("Gaji Bersih : Rp" + str(gajiBersih))
