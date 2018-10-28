import time
class Hayvanlar():
    def __init__(self,cinsi,yaş,renk,cinsiyet):
        self.cinsi=cinsi
        self.yaş=yaş
        self.renk=renk
        self.cinsiyet=cinsiyet
    def __str__(self):
        return "Cinsi: {}\nYaşı: {}\nRenk: {}\nCinsiyeti: {}\n".format(self.cinsi,self.yaş,self.renk,self.cinsiyet)

class Köpek(Hayvanlar):
    def __init__(self,cinsi,yaş,renk,cinsiyet,kilo,boy,aşı):
        super().__init__(cinsi,yaş,renk,cinsiyet)
        self.kilo=kilo
        self.boy=boy
        self.aşı=aşı
    def __str__(self):
        return "kilo: {}\nBoy: {}\nAşı: {}\n".format(self.kilo,self.boy,self.aşı)

class Kuş(Hayvanlar):
    pass

class At(Hayvanlar):
    def __init__(self,cinsi,yaş,renk,cinsiyet,kilo,boy):
        super().__init__(cinsi,yaş,renk,cinsiyet)
        self.kilo=kilo
        self.boy=boy
    def __str__(self):
        return "Cinsi: {}\nYaşı: {}\nRenk: {}\nCinsiyeti: {}\nkilo: {}\nBoy: {}\n ".format( self.cinsi, self.yaş,
                                                                                             self.renk, self.cinsiyet,
                                                                                             self.kilo,self.boy)


köpek=Köpek("Kangal",3,"beyaz","dişi",20,70,"aşı yapılmış")
kuş=Kuş("papağan",1,"turuncu","erkek")
at=At("Arap",2,"siyah","dişi",80,120)

print("""
********************HAYVANLAR ALEMİ*********************
SEÇENEKLER:
1- KÖPEK

2-KUŞ

3-AT

çıkış için q' ya basınız.
********************************************************

""")
seçim=input("Lütfen seçim yapınız: ")
while True:
    if(seçim == "q"):
        print("Programdan çıktınız.")
        break
    elif( seçim == "1"):
        print("Köpek Bilgileri",köpek)
        time.sleep(1)
        break
    elif (seçim == "2"):
        print("Kuş Bilgileri",kuş)
        time.sleep(1)
        break
    else:
        print("At Bilgileri",at)
        time.sleep(1)
        break






