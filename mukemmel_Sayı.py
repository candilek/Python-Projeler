print("""************\n Mukemmel Sayı bulan program\n******************""")

sayı=int(input("Sayı girin: "))

toplam=0

for i in range(1,sayı): #1 den sayıyya kadar döngüde dolaş
    if(sayı % i == 0): #sayı i ye tam bölünürse
        toplam +=i
if(toplam == sayı):
    print( "Girdiğiniz sayı mükemmel sayıdır!")
else:
    print("Girdiğiniz sayı mükemmel sayı değildir!")


