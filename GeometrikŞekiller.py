
print("""Geometrik Şekil Hesaplama İşlemi:
Dikdörtgen için 1,
Üçgen için 2 yi seçiniz!!!
""")
Tip= input("Seçim Yapınız: ")

if( Tip == "1"):
     print("Dikdörtgen seçtiniz.")
     a=int(input("1. kenarı girin: "))
     b=int(input("ikinci kenarı girin: "))
     c=int(input("üçüncü kenarı girin: "))
     d=int(input("dördüncü kenarı girin: "))
     if(a==b==c==d):
        print("KARE ")
     elif((a==b and c==d) or (a==c and b==d)):
        print("DİKDÖRTGEN ")
     else:
        print("DÖRTGEN ")
elif(Tip== "2"):
    print("Üçgen seçtiniz!")
    x=int(input("1. kenar: "))
    y=int(input("2. kenar: "))
    z=int(input("3. kenar: "))
    if( (abs(x-y )< abs(z) < abs(x+y)) or (abs(x-z) < abs(y) < abs(x+z)) or abs(y-z) < abs(x) < abs(y+z) ):
        if(abs(x)== abs(y) == abs(z)):
            print("EŞKENAR ÜÇGEN! ")
    elif(( abs(x) == abs(y) and x!= abs(z)) or ( abs(x) == abs(z) and x!= abs(y)) or ( abs(z) == abs(y) and z!= abs(x))):
        print("İKİZKENAR ÜÇGEN!")
    else:
        print( "ÜÇGEN BELİRTMİYOR!" )















