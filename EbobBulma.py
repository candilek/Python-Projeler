def BuyukSayı(sayı1,sayı2):
    if(sayı1> sayı2):
        return sayı1
        print( "buyuk sayı: ", sayı1 )
    else:
        return sayı2
        print("buyuk sayı: ",sayı2)

def Ebob (sayı1,sayı2):
    sonuc=1
    buyuk=BuyukSayı(sayı1,sayı2)
    for i in range(buyuk+1,1,-1):
        if((sayı1%i==0) and (sayı2%i==0)):
            sonuc=i
    return sonuc
sayı1=int(input("sayı girin: "))
sayı2=int(input("sayı girin: "))
sayı=Ebob(sayı1,sayı2)
print("ebob= ",sayı)