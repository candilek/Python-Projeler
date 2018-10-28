boy=float(input("Boyunuzu girin: "))
kilo=int(input("Kilonuzu Girin: "))

BKE = kilo/(boy * boy)
if(BKE <  18.5):
    print("Zayıf!!!")
elif(18.5 < BKE < 25):
    print("Normal!!!")
elif(25 < BKE < 30):
    print("Fazla Kilo!!!")
elif( BKE < 30):
    print("OBEZ!!!")
else:
    print("Geçersiz değer!")
