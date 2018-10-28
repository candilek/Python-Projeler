a=int(input("Birinci sayıyı giriniz: "))
b=int(input("İkinci sayıyı giriniz: "))
c=int(input("Üçüncü sayıyı giriniz: "))

if(a > b and a > c):
    print("En büyük sayı: {} dır".format(a))
elif(b > a and b > c):
    print("en büyük sayı: {} dır.".format(b))
elif(c > a and c > b ):
    print("En büyük sayı: {} dır.".format(c))