print("""*****************************

 Atm Makinesine Hoşgeldiniz.

 İşlemler;
 1-Bakiye Sorgulama
 2-Para Yatırma
 3- Para Çekme
 4-Havale

 Programdan çıkmak için q'ya basın.
***************************************
 """)

bakiye =1000
while True:

    işlem= input("işlemi seçiniz: ")

    if (işlem == "q"):
        print( "Yine Bekleriz.:)" )
        break

    elif(işlem== "1"):
        print("Bakiyeniz: {} tl'dir.".format(bakiye))

    elif(işlem == "2"):
        miktar=int(input("yatırılacak para miktarını giriniz: "))
        bakiye +=miktar

    elif(işlem== "3"):
        miktar=int(input("para miktarını giriniz: "))

        if(bakiye - miktar <0):
            print("Böyle bir miktar çekemessiniz.")
            continue
        bakiye -= miktar
    elif(işlem=="4"):
        havale=int(input("Havale edilecek miktarı girin: "))
        bakiye-=havale
        print("bakiyeniz: {} tl'dir".format((bakiye)))

    else:
        print("geçersiz işlem")






