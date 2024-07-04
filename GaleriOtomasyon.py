#Basit Galeri Otomasyonu

import datetime
dosyaAdi="ozellikler.txt"
#Dosyadan bilgileri satır satır alıp ardından onları yazdıran Listeleme fonksiyonu. Try-excepti doğru isimde dosyanın olup olmadığına bakmak için kullandım.
def arabaListele():
    #Burada try except dosyanın olup olmadığına bakıyor.
    try:
        #Dosya "r" modu ile okunmak için açılıyor ve satirlara bölünüyor daha sonra satirların içindeki bilgiler "," ile ayırılıp arabaBilgileri listesine koyuluyor.
        with open(dosyaAdi, 'r') as dosya:
            for satir in dosya:
                arabaBilgileri = satir.split(',')
                print("\nAraba ID: ", arabaBilgileri[0])
                print("Arabanin Tipi: ", arabaBilgileri[1])
                print("Arabanin Fiyati: ", arabaBilgileri[2])
                print("Arabanin Kilometresi: ", arabaBilgileri[3])
                print("Arabanin Yili: ", arabaBilgileri[4])

    except FileNotFoundError:
        print("Dosya bulunamadi.")

#Araba eklemesi yapılan fonksiyon.
def arabaEkle():
    ekle=True
    while ekle:
        try:
            bilgiler=list()
            # Öncelikle bilgiler kullanıcıdan isteniyor ve listede tutuluyor.
            bilgiler.append(input("Eklemek İstediginiz Arabanin ID numarasini: "))
            bilgiler.append(input("Eklemek İstediginiz Arabanin Tipi(Sedan, Suv vs.): "))
            bilgiler.append(input("Eklemek İstediginiz Arabanin Fiyati: "))
            bilgiler.append(input("Eklemek İstediginiz Arabanin Kilometresi: "))
            bilgiler.append(input("Eklemek İstediginiz Arabanin Yilini (2009, 1998,...): "))
            #Burada(37. satır) try ile ID, fiyat, kilometre ve yıl bilgilerinin sadece rakamlardan oluştuğunu kontrol ediyoruz.
            #Eğer int'e dönüştürülemiyorsa hata verecek ve yanlış girildiği anlaşılacak(52. Satır).
            for bilgi in bilgiler[0:1:] + bilgiler[2::]:
                int(bilgi)
            #Dosyayı "r" yani okuma moduyla açıyoruz çünkü dosya içerisindeki ID bilgilerini ekleme
            # işlemi sırasında önceden kullanılıp kullanılmadığını kontrol etmek için kullancağız.
            dosya = open(dosyaAdi, "r")
            satirlar = dosya.readlines()
            dosya.close()
            # Eklenecek arabanın ID numarasını kontrol ediyoruz.
            kontrol = 0
            for satir in satirlar:
                if satir.split(",")[0]==bilgiler[0]:
                    kontrol=1
            if kontrol:
                print("Hata: Bu ID numarasina sahip bir araba zaten mevcut.")
            else:
                #Dosyayı "a" yani ekleme moduyla açıyoruz.
                dosya = open(dosyaAdi, "a")
                #Döngü ile bilgileri dosyaya ekliyoruz ve aralara "," işareti koyuyoruz. Ardından dosyayı kapatıyoruz.
                sayac=0
                print(bilgiler)
                for i in bilgiler:
                    if sayac < 4:
                        dosya.write(i + ",")
                        sayac=sayac+1
                    else:
                        dosya.write(i+"\n")
                dosya.close()
                print("Araba basariyla sisteme eklendi.")
                ekle=False
        #Bilgiler alınırken ID, fiyat, kilometre ve yıl bilgileri int'den farklı girilirse excepte giriyor ve tekrar değer isteniyor.
        except ValueError:
            print("ID numarasi,fiyat,kilometre ve yil bilileri sadece sayilardan olusabilir.")

#Araba silmesi yapan fonksiyonu.
def arabaSil():
    arabaId = input("Silmek istediginiz arabanin ID numarasini giriniz: ")
    #Dosyamı başta "r" modunda açıyorum çünkü ilk önce arabalara bakıp bilgilerini almalı.
    with open(dosyaAdi, "r") as dosya:
        satirlar = dosya.readlines()

    yeniSatirlar= []
    idBul = True
    #Burada yukarıda dosyadan aldığım bilgilere göre arabayı ID bilgisine göre arıyorum.
    #Eğer ID farklı ise yeni oluşturduğım "yeniSatirlar" adlı listeye ekliyorum. Farklı ise eklemiyorum ve boolean değişkenimi false yapıyorum.
    for satir in satirlar:
        if satir.split(',')[0] != arabaId:
            yeniSatirlar.append(satir)
        else:
            idBul = False
    #Burada boolean değişkenim false olmadı ise arabaların hepsi tekrar yeni listeye eklenmiş yani aranan ID'ye ait araba bulunammış demektir.
    if idBul:
        print("Verilen ID'de araba bulunamadi.")
        return
    #Burada "w" mod ile dosyamı açıyorum. "a" modu ile açmamamın nedeni silme işlemini yaparken silmek yerine silinmeyecek değerleri ekleme şeklinde yaptığım için kullanmadım.
    with open(dosyaAdi, "w") as dosya:
        dosya.write("".join(yeniSatirlar))
    print("Araba basariyla sistemden silindi.")

#Araba aramaya yarayan fonksiyon.
def arabaAra():
    id = input("Aramak istediginiz arabanin ID numarasini giriniz: ")
    arabalar = {}

    with open(dosyaAdi, "r") as dosya:
        satirlar = dosya.readlines()

    arabaBilgileri = [satir.split(",") for satir in satirlar]
    #Burada araba bilgilerini sözlükle kullandım.
    for bilgi in arabaBilgileri:
        arabaID = bilgi[0]
        arabalar[arabaID] = {"Tipi": bilgi[1],"Fiyati": bilgi[2],"Kilometresi": bilgi[3],"Yili": bilgi[4]}
    #Aranna araba mevcutsa bilgileri yazdırılıyor.
    if id in arabalar:
        print("ID: {}".format(id))
        print("Tipi: {}".format(arabalar[id]["Tipi"]))
        print("Fiyati: {}".format(arabalar[id]["Fiyati"]))
        print("Kilometresi: {}".format(arabalar[id]["Kilometresi"]))
        print("Yili: {}".format(arabalar[id]["Yili"]))
    else:
        print("Belirtilen ID'ye ait bir araba bulunamadi.")

#Araba bilgisi güncelliyen fonksiyon.
def arabaGuncelle():
    #Hangi araba üzerinde güncelleme yapılacağı belirleniyor.
    arabaId = input("Guncellemek istediginiz arabaya ait ID bilgisini giriniz: ")

    #Id arabanın 1.(0. index),tip 2., fiyat 3., kilometre 4. ve yılı 5. özelliği olduğundan sırası ile yazdım.
    #Seçime göre yeni özellik eski özelliğin üzerine yazılıyor.
    def idGuncelle(yeniId):
        nonlocal arabaOzellik
        arabaOzellik[0] = yeniId
        print("Id bilgisi basari ile guncellendi.")

    def tipGuncelle(yeniTip):
        nonlocal arabaOzellik
        arabaOzellik[1] = yeniTip
        print("Tip bilgisi basari ile guncellendi.")

    def fiyatGuncelle(yeniFiyat):
        nonlocal arabaOzellik
        arabaOzellik[2] = yeniFiyat
        print("Fiyat bilgisi basari ile guncellendi.")

    def kilometreGuncelle(yeniKilometre):
        nonlocal arabaOzellik
        arabaOzellik[3] = yeniKilometre
        print("Kilometre bilgisi basari ile guncellendi.")

    def yilGuncelle(yeniYil):
        nonlocal arabaOzellik
        arabaOzellik[4] = yeniYil
        print("Yil bilgisi basari ile guncellendi.")

    with open(dosyaAdi, 'r') as dosya:
        satirlar = dosya.readlines()
    # "i" değişkeni satir değişkeninin indeksini kullanabilsin diye enumerate kullandım.
    for i, satir in enumerate(satirlar):
        arabaOzellik = satir.split(',')
        if arabaOzellik[0] == arabaId:
            #Seçilen arabanın özelliklerini yazdırdım ardından hangi özelliğinin değişmesi istendiğini sordum ve ona göre değiştirdim.
            print("Araba bilgileri: ", arabaOzellik)
            secim = int(input("Hangi bilgiyi degistirmek istersiniz?\n1)Id\n2)Tip\n3)Fiyat\n4)Kilometre\n5)Yil\nSecim: "))

            if secim == 1:
                id=True
                while id:
                    yeniId = input("Yeni id: ")
                    if yeniId not in satirlar:
                        idGuncelle(yeniId)
                        id=False
                    else:
                        print("Bu id baska bir arabaya ait!")
            elif secim == 2:
                yeniTip = input("Yeni tip: ")
                tipGuncelle(yeniTip)
            elif secim == 3:
                yeniFiyat = input("Yeni fiyat: ")
                fiyatGuncelle(yeniFiyat)
            elif secim == 4:
                yeniKilometre = input("Yeni kilometre: ")
                kilometreGuncelle(yeniKilometre)
            elif secim == 5:
                yeniYil = input("Yeni yil: ")
                yilGuncelle(yeniYil)
            else:
                print("Gecersiz bir secim yaptiniz.")

            satirlar[i] = ','.join(arabaOzellik)
            break
    else:
        print("Belirtilen ID'ye ait bir araba bulunamadı.")

    with open(dosyaAdi, 'w') as dosya:
        dosya.writelines(satirlar)

#Araba vergisini yıllık olarak hesaplayan fonksiyon.
def arabaVergiHesapla():
    #Burada hangi yılda olduğumuzu datetime kütüphanesi ile belirliyorum. Bu yıl bilgisini arabanın kaç yaşında olduğunu belirlemek için kullanacağım.
    #Burada kütüphane kullanmak yerine 2023 olarak yılı kendim belirleyebilirdim ama böyle yaparsam kodum her zaman kullanılır olamazdı.
    simdi = datetime.datetime.now()
    yilimiz= simdi.year

    #Burada güncelleme silme fonksiyoınundaki ile aynı şekilde "idBul" değişkeni ekliyorum amacı tamamen aynı.
    arabaId = input("Yillik vergisini hesaplamak istediginiz arabanin ID numarasini giriniz: ")
    idBul = True
    #Dosyayı açıp satır satır okuyorum ve listeye atıyorum.
    with open(dosyaAdi, "r") as dosya:
        satirlar = dosya.readlines()
    #Burada tek tek her satırı araba bilgilerine bölüp koyuyorum ve sıfırıncı index id bilgisi tuttuğu için kontrol yapıyorum.
    for satir in satirlar:
        arabaBilgileri = satir.split(",")
        id = arabaBilgileri[0]
        #Eğer girilen id bir arabaya ait ise vergi hesaplama işlemini yapıyorum.
        if id == arabaId:
            fiyat = float(arabaBilgileri[2])
            yil = int(arabaBilgileri[4])
            yillikVergiMiktari=0
            yas=yilimiz-yil
            durumu=str
            if 0<=yas<1:
                yillikVergiMiktari= 10000+(fiyat*0.001)
                durumu="sifir"
            elif 1<=yas<8:
                yillikVergiMiktari=5000+(fiyat*0.001)
                durumu="yeni"
            elif 8<=yas<14:
                yillikVergiMiktari=3500+(fiyat*0.001)
                durumu="az eski"
            elif 14<=yas<22:
                yillikVergiMiktari=2000+(fiyat*0.001)
                durumu="eski"
            elif 22<=yas<90:
                yillikVergiMiktari=12000+(fiyat*0.001)
                durumu="klasik"

            print("Araba ID:", id)
            print("Secilen araba {} bir arac ve yillik vergi miktari:{}TL".format(durumu,yillikVergiMiktari))
            idBul = False
    #Eğer verilen id'ye ait araba bulunamadıysa ilgili mesajı veriyor.
    if idBul:
        print("Belirtilen ID'ye ait bir araba bulunamadi.")

print("******************************************   Galeri Otomasyonuna Hosgeldiniz   ***********************************************")
while True:
    print("----------------------------------------------------------------\n""Asagidan Yapmak İstediginiz İslemi Seciniz:"
          " \n1.Eldeki Tum Arabalari Listeleme\n2.Araba Ekleme\n3.Araba Silme\n4.Araba Arama"
          "\n5.Araba Bilgisi Guncelleme\n6.Yillik Vergi Hesaplama""\n7.cikis")
    secim = input("Secim Yapiniz: ")
    print("----------------------------------------------------------------")
    if secim == '1':
        arabaListele()
    elif secim == '2':
        arabaEkle()
    elif secim == '3':
        arabaSil()
    elif secim == '4':
        arabaAra()
    elif secim == '5':
        arabaGuncelle()
    elif secim == '6':
        arabaVergiHesapla()
    elif secim == '7':
        print("cikis Yapiliyor..")
        break
    else:
        print("Yanlis bir tuslama yaptiniz!")
