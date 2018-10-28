"""
Asal Sayı Bulan Program

"""
def asal_mi(sayı):
    if(sayı== 1): #asal sayı değil
        return False
    elif(sayı == 2): #en üçük asal sayı
        return True
    else:
        for i in range(2,sayı):
            if( sayı %i == 0): #sayı tam bölünüyorsa
                return False
        return True #diğer durumlar için
while True:
    sayı=int(input("Sayı Girin: "))
    if (sayı== "q"):
        print("programdan çıktınız!")
        break
    else:
        sayı=int(sayı)
        if(asal_mi((sayı))):#sayıyı fonksiyona gönderdik.
            print(sayı,"Asal sayıdır.")
        else:
            print(sayı,"asal değildir!!!")






