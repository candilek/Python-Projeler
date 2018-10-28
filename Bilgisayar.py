import time
import random


class Bilgisayar( ):
    def __init__(self, pc_durum="kapalı", pc_ses=0, pc_uygulamalar=["PyCharm", "Notepad++", "Vivaldi"],
                 acik_uygulama="PyCharm"):
        self.pc_durum = pc_durum
        self.pc_ses = pc_ses
        self.pc_uygulamalar = pc_uygulamalar
        self.acik_uygulama = acik_uygulama

    def pc_ac(self):
        if (self.pc_durum == "açık"):
            print( "Bilgisayarınız zaten açık." )
        else:
            print( "Bilgisayarınız açılıyor." )
            time.sleep( 2 )
            self.pc_durum = "açık"
            print( "Hoşgeldiniz." )

    def pc_kapat(self):
        if (self.pc_durum == "kapalı"):
            print( "Bilgisayarınız zaten kapalı." )
        else:
            print( "Bilgisayarınız kapanıyor." )
            time.sleep( 2 )
            self.pc_durum = "kapalı"
            print( "Hoşça kal!" )

    def ses_ayarları(self):
        while True:
            ses_ayar = input( "Sesi Ayarlamak İçin: !\nSes Artır (+)\nSes Azalt(-)\nÇıkış(q)" )
            if (ses_ayar == "-"):
                if (self.pc_ses != 0):
                    self.pc_ses -= 1
                    print( "Ses Düzeyi: ", self.pc_ses )
                else:
                    print( "Ses zaten kapalı." )
            elif (ses_ayar == "+"):
                if (self.pc_ses != 100):
                    self.pc_ses += 1
                    print( "Ses Düzeyi: ", self.pc_ses )
                else:
                    ("Ses en yüksek düzeyde.")
            elif (ses_ayar == "q"):
                print( "Ses Ayarlarından Çıkılıyor..." )
                time.sleep( 2 )
                print( "Yeni Ses Düzeyiniz: ", self.pc_ses )
                break
            else:
                print( "Geçersiz bir giriş yaptınız." )

    def uygulama_yukle(self, uygulama_adi):
        print( "Uygulamanız yükleniyor..." )
        self.pc_uygulamalar.append( uygulama_adi )
        time.sleep( 2 )
        print( uygulama_adi, "uygulaması başarıyla yüklendi." )

    def __len__(self):
        return len( self.pc_uygulamalar )

    def alt_tab(self):
        numara = random.randint( 0, len( self.pc_uygulamalar ) - 1 )
        self.acik_uygulama = self.pc_uygulamalar[numara]
        print( self.acik_uygulama )

    def __str__(self):
        return "PC Durumu: {}\nSes Düzeyi {}\nYüklü Uygulamalar {}\nAçık Uygulama{}".format( self.pc_durum, self.pc_ses,
                                                                                             self.pc_uygulamalar,
                                                                                             self.acik_uygulama )


mypc = Bilgisayar( )
print( """

______________İŞLEMLER______________

1. Bilgisayarı Aç
2. Bilgisayarı Kapat
3. Ses Ayarları
4. Yüklü Uygulamalar Listesi
5. Yüklü Uygulama Sayısı
6. Uygulama Yükleme
7. Uygulama Değiştirme
8. Bilgisayar Bilgileri
9. Çıkış

""" )
while True:
    işlem = input( "İşlemi Seçiniz: " )
    if (işlem == "9"):
        break
    elif (işlem == "1"):
        mypc.pc_ac( )
    elif (işlem == "2"):
        mypc.pc_kapat( )
    elif (işlem == "3"):
        mypc.ses_ayarları( )
    elif (işlem == "4"):
        print( mypc.pc_uygulamalar )
    elif (işlem == "5"):
        print( "Uygulama Sayısı: ", len( mypc ) )
    elif (işlem == "6"):
        uygulamalar = input( "Yüklemek istediğiniz uygulamaları ',' ile ayırarak giriniz: " )
        pc_uygulamalar = uygulamalar.split( "," )
        for eklenecek in pc_uygulamalar:
            mypc.uygulama_yukle( eklenecek )
    elif (işlem == "7"):
        mypc.alt_tab( )
    elif (işlem == "8"):
        print( mypc )
    else:
        print( "Geçersiz İşlem !" )