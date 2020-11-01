# Status Kelulusan Mahasiswa
bahasa = int(input("Nilai Bahasa Indonesia : "))
ipa = int(input("Nilai IPA: "))
mate = int(input("Nilai Matematika : "))

print ("=============================")

if bahasa >= 0 and bahasa <= 100 and ipa >= 0 and ipa <= 100 and mate >= 0 and mate <= 100 :
    if(bahasa >= 60 and ipa >= 60 and mate > 70):
        print ("LULUS")
    else:
        print ("TIDAK LULUS")
else:
    print ("Maaf input ada yang tidak valid")
