print(""""
***************************************
Hesap Makinası Programı
İşlemler;
1- Toplama İşlemi
2- Çıkarma İşlemi
3- Çarpma işlemi
4- Bölme İşlemi
***************************************
""")
a=int(input("birinci sayıyı girin: "))
b=int(input("ikinci sayıyı girin: "))
işlem= int(input("işlemi giriniz: "))

if (işlem == 1):
    print("{} ile {} in toplamı {} dir.".format(a, b, a+b))
elif(işlem == 2):
    print("{} ile {} nin farkı {} dır.".format(a, b, a-b))
elif (işlem == 3):
    print("{} ile {} nin çarpımı {} dır.".format(a, b, a*b))
elif (işlem == 4):
    print("{} nın {} ye bölümü {} dır.".format(a, b, a/b))
else:
    print("Geçersiz işlem...")



