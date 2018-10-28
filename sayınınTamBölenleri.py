
def SayınınTamBölenleri(sayı):
    tam_bolenler=[]
    for i in range(2,sayı):
        if(sayı%i== 0):
            tam_bolenler.append((i))
    return tam_bolenler
while True:
    sayı=(input("sayı girin: "))
    if(sayı == "q"):
        print("program sonlandırılıyor!")
    else:
        sayı=int(sayı)
        print("sayının tam bölenleri",SayınınTamBölenleri(sayı))
        break

