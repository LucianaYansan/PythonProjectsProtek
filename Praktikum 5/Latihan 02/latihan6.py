from random import randint
print("Hai... nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!")
bil=randint(0,100)
score = 100
while True:
    if(score < 0):
        print("GAME OVER")
        break
    jawaban=int(input("Tebakan Anda : "))
    if(jawaban > bil):
        print("Hehehe... Bilangan tebakan Anda terlalu besar")
    elif(jawaban<bil):
        print("Hehehe... Bilangan tebakan Anda terlalu kecil")
    elif(jawaban==bil):
        print("Yey... Bilangan tebakan Anda BENAR :D")
        print("Score Anda : ",score)
        break
    score -= 2
    

