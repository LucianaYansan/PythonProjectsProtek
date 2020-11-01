kodeKaryawan = input("Masukkan kode karyawan : ")
namaKaryawan = input("Masukkan nama karyawan : ")
golongan = input("Masukkan golongan : ")

if(golongan == "A"):
    gajiPokok = 10000000
    potongan = 2.5
    jumlahPotongan = 2.5 / 100 * 10000000
    
elif(golongan == "B"):
    gajiPokok = 8500000
    potongan = 2.0
    jumlahPotongan = 2. / 100 * 8500000
    
elif(golongan == "C"):
    gajiPokok = 7000000
    potongan = 1.5
    jumlahPotongan = 1.5 / 100 * 7000000
   
elif(golongan == "D"):
    gajiPokok = 5500000
    potongan = 1.0
    jumlahPotongan = 1.0 / 100 * 5500000

status = int (input ("Masukkan status(1: menikah, 2: belum) : "))
if(status == 1):
    tunjanganMenikah = gajiPokok * 10/100
    jumlahAnak = int(input ("Masukkan jumlah anak : "))
    tunjanganAnak = gajiPokok * 5/100 * jumlahAnak
elif(status==2):
    tunjanganMenikah = 0
    jumlahAnak = 0
    tunjanganAnak = 0

print("====================================")

print("STRUK RINCIAN GAJI KARYAWAN")

print("-----------------------------------------------------------")

print("Nama Karyawan : " + namaKaryawan + "(Kode Karyawan : " + str(kodeKaryawan) + ")")
print("Golongan : " + golongan)

if(status == 1):
    print ("Status Menikah : Sudah Menikah")
    print ("Jumlah Anak : " , jumlahAnak)
else:
    print ("Status Menikah : Belum Menikah")

print("-----------------------------------------------------------")

print("Gaji Pokok : Rp" + str(gajiPokok))
print("Tunjangan Istri/Suami : Rp" + str(tunjanganMenikah))
print("Tunjangan Anak : Rp" + str(tunjanganAnak))

print("-----------------------------------------------------------")

gajiKotor = gajiPokok + tunjanganMenikah + tunjanganAnak
print("Gaji Kotor : Rp" + str(gajiKotor))
potonganGaji = int(gajiKotor * potongan/100)
print("Potongan (" + str(potongan) + "%): Rp" + str(potonganGaji))

print("-----------------------------------------------------------")

gajiBersih = gajiKotor - potonganGaji
print("Gaji Bersih : Rp" + str(gajiBersih))








