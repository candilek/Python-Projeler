def EkokBulma(sayı1,sayı2):
    sonuc=1
    for i in range(1,sayı1*sayı2):
        if(i% sayı1==0)and (i%sayı2==0):
            sonuc=i
            break
    return sonuc
sayı1=int(input("sayı girin: "))
sayı2=int(input("sayı girin: "))
ekok=EkokBulma(sayı1,sayı2)
print("ekok: ",ekok)
