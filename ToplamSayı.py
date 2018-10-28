
print("programdan çıkamak için q ya basın...")
toplam=0
while True:
    sayı = input( "Sayı girin: " )
    if(sayı =="q"):
        print("Program sonlanıyor! ")
        break
    else:
        sayı=int(sayı)
    toplam += sayı
    print("toplam sayı: ",toplam)


