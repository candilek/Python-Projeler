print("""
***********************************
Faktoriyel Bulma Programı

Çıkmak için q ya basınız.

***********************************
""")
while True:
    sayı=input("sayı: ")
    if(sayı== "q"):
        print( "program sonlandırılıyor.")
        break
    else:
        sayı=int(sayı)
        faktoriyel=1

        for i in range (2,sayı+1):
            faktoriyel*=i

        print("faktöriyel: ",faktoriyel)

