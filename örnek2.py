import time

class Hayvan( ):
    def __init__(self, isim, hız,  özellik):
        self.isim = isim
        self.hız = hız
        self.özellik = özellik

    def __str__(self):
        return "İsim: {}\nHızı: {}\nDoğum Olayı: {}\nÖzellik : {}".format( self.isim,
                                                                           self.hız,
                                                                           self.özellik )


class Köpek( Hayvan ):
    pass


class Kuş( Hayvan ):
    def __init__(self, isim,  hız,  özellik, yuvası):
        super( ).__init__( isim,  hız, özellik )
        self.yuvası = yuvası


class At( Hayvan ):
    pass


kuş = Kuş( "Kuş", "382 Km/sa", " " , "Ağaç" )
köpek = Köpek( "Köpek", "10 km/sa", "Sadık" )
at = At( "At", "78 Km/sa", "Binek olarak kullanılır" )
print( """
***************************************
Hayvanlar alemine hoşgeldiniz.

Öğrenmek istedğiniz bilgiyi seçiniz:

1)Köpek bilgileri
2)Kuş Bilgileri
3)At bilgileri
***************************************
""" )
while True:
    cevap = input( "Köpek Bilgileri: '1',Kuş Bilgileri: '2',At Bilgileri: '3',çıkış: 'q'" )

    if (cevap == "q"):
        print( "Program sonlanıyor..." )
        break
    if (cevap == "1"):
        while True:
            cevap1 = input(
                "Tür: '1' Hızı: '3' Özellik: '5', Her şey '6', çıkış: 'exit'" )
            if (cevap1 == "exit"):
                print( "Hayvan alemine dönülüyor..." )
                time.sleep( 1 )
                break
            if (cevap1 == "1"):
                print( "Köpek adı:", köpek.isim )

            elif (cevap1 == "3"):
                print( "Köpeğin hızı", köpek.hız )

            elif (cevap1 == "5"):
                print( "Özelliği:", köpek.özellik )

            elif (cevap1 == "6"):
                print( köpek )
            else:
                print( "Geçersiz cevap" )

    if (cevap == "2"):
        while True:
            cevap2 = input(
                "Tür: '1'  Hızı: '3' Özellik: '5',Yuva '6' ,Her şey '7', çıkış: 'exit'" )

            if (cevap2 == "exit"):
                print( "Hayvanlar alemine dönülüyor..." )
                time.sleep( 1 )
                break
            if (cevap2 == "1"):
                print( "Tür:", kuş.isim )

            elif (cevap2 == "3"):
                print( "Hız:", kuş.hız )

            elif (cevap2 == "5"):
                print( "Özelliği:", kuş.özellik )
            elif (cevap2 == "6"):
                print( "Yuvası:", kuş.yuvası )
            elif (cevap2 == "7"):
                print( "Her şey", kuş )

            else:
                print( "Geçersiz işlem." )

    if (cevap == "3"):
        while True:
            cevap2 = input(
                "Tür: '1' Hızı: '3' Özellik: '5', Her şey '6', çıkış: 'exit'" )

            if (cevap2 == "exit"):
                print( "Hayvanlar alemina dönülüyor..." )
                time.sleep( 1 )
                break
            if (cevap2 == "1"):
                print( "Tür:", at.isim )
            elif (cevap2 == "3"):
                print( "Hız:", at.hız )
            elif (cevap2 == "5"):
                print( "Özelliği:", at.özellik )
            elif (cevap2 == "6"):
                print( at )
            else:
                print( "Geçersiz işlem" )