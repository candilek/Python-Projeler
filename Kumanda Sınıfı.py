import random
import time #sleep fonksiyonunu kullanmak için
class Kumanda():
    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["TRT"],kanal="Trt"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
    def tv_ac(self):
        if(self.tv_durum == "Açık"):
            print("Televizyon zaten açık...")
        else:
            print("Televizyon açılıyor.")
            self.tv_durum ="Açık"
    def tv_kapat(self):
        if(self.tv_durum =="kapalı"):
            print("Televizyon zaten kapalı...")
        else:
            print("Televizyon kapanıyor.")
            self.tv_durum = "Kapalı"
    def ses_ayarla(self):
        while True:
            cevap=input("ses azalt: '<' \nSes Arttır: '>' \nçıkış: çıkış ")
            if(cevap == "<"):
                if(self.tv_ses != 0):
                    self.tv_ses -=1
                    print("ses: ",self.tv_ses)
            elif(cevap == ">"):
                if(self.tv_ses != 31):
                    self.tv_ses += 1
                    print( "ses: ", self.tv_ses )
            else:
                print("ses güncellendi...",self.tv_ses)
                break

    def kanal_ekle(self,kanal_ismi):
        print("kanal ekleniyor...")
        time.sleep(1)#bir saniye beklemek için
        self.kanal_listesi.append(kanal_ismi)
        print("kanal eklendi...")

    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        #bütün indexlerin üzerinde rstgele bir index almak için random kullandık.
        #0 ile kanal listesi -1 kadar bir sayı oluşturulacak ve rastgele değişkenine atılacak
        self.kanal=self.kanal_listesi[rastgele]
        print("Şu anki kanal: ",self.kanal)
    def __len__(self):
        return len(self.kanal_listesi)

    def kanal_sil(self,kanal_ismi):
        kanal_ismi=input("kanal ismi: ")
        print("kanal siliniyor.")
        time.sleep(1)
        self.kanal_listesi.remove(kanal_ismi)
        print("Kanal Silindi...")


    def __str__(self): #print fonksiyonu çağrıldığında bu str fonksiyonu çalıştırılacak
        return "Tv Durun: {}\nTv Ses: {}\nKanal Listesi: {}\nŞu anki Kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda= Kumanda()#obje oluşturduk

print("""
    televizyon Uygulaması

    1-Tv Aç

    2-Tv Kapat

    3-Ses Ayarları

    4-kanal Ekle

    5-Kanal sayısını Öğrenme

    6-Rastgele Kanala Geçme

    7-Televizyon Bilgileri

    8-Kanal Sil

    çıkmak için 'q' ya basın.

    """)
while True:
        işlem=input("İşlemi seçiniz: ")
        if(işlem == 'q'):
            print("programdan çıkılıyor.")
            break
        elif(işlem == "1"):
            kumanda.tv_ac()
        elif(işlem == "2"):
            kumanda.tv_kapat()
        elif(işlem == "3"):
            kumanda.ses_ayarla()
        elif(işlem == "4"):
            kanal_isimleri =input("kanka isimlerini virgül ile ayırarak girin.")
            kanal_listesi =kanal_isimleri.split(",")#kanal isimlerini , ile ayırmak için
            for eklenecekler in kanal_listesi:
                kumanda.kanal_ekle(eklenecekler)
        elif(işlem=="5"):
            print("kanal sayısı: ",len(kumanda))
        elif(işlem== "6"):
            kumanda.rastgele_kanal()
        elif(işlem =="7"):
            print(kumanda)
        elif (işlem == "8"):
            for sil in kanal_listesi:
                kumanda.kanal_sil(sil)
                break
        else:
            print("Geçersiz işlem...")










































