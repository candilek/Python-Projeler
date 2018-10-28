import random #rastgele sayı üretmek için
import time #1 saniye beklemek için

print("""**************************
 Sayı Tahmin Oyunu

 1 ile 40 arasında sayıyı tahmin edin.
 **********************************
""")
rastgele_sayı=random.randint(1,40) #1 ile 40 arasında rastgele sayı üretmek için
tahmin_hakkı=7
while True:

    tahmin=int(input("tahmin: "))
    if(tahmin<rastgele_sayı ):
        print("Bilgiler kontrol ediliyor!")
        time.sleep(1)#program bir saniyeliğine durucak..
        print("Daha yüksek bir sayı söyleyin: ")
        tahmin_hakkı -=1
    elif(tahmin > rastgele_sayı):
        print("Bilgiler kontrol ediliyor!")
        time.sleep(1)#program bir saniyeliğine durucak..
        print("Daha düşük bir sayı söyleyin: ")
        tahmin_hakkı -=1
    else:
        print("Bilgiler kontrol ediliyor!")
        time.sleep(1)#program bir saniyeliğine durucak..
        print("tebrikler",rastgele_sayı)
        break
    if(tahmin_hakkı==0):
        print("Tahmin hakkınız bitti...")
        print("sayı: ",rastgele_sayı)
        break





