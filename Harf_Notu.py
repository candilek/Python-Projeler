
print("""
************************************
HARF NOTU SİSTEMİ
************************************
 """)
Vize1=int(input("Vize1 notu: "))
Vize2 =int(input("Vize2 notu: "))
final=int(input("Final notu: "))

toplam_Not=((Vize1*30)/100) + ((Vize2*30)/100)+ ((final*40)/100)
if (toplam_Not >= 90):
    print("AA")
elif(89 >=  toplam_Not >= 85):
     print("BA")
elif(84 >= toplam_Not >=80 ):
    print("BB")
elif(79 >= toplam_Not >= 75):
    print("CB")
elif(74 >= toplam_Not >= 70):
    print("CC")
elif(69 >= toplam_Not >= 65):
    print("DC")
elif(64 >= toplam_Not >= 60):
    print("DD")
elif (59 >= toplam_Not >=55):
    print("FD")
else:
    print("KALDINIZ!!!")
