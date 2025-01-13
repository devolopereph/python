#Bankamatik geliştiriyorum. Github'a yüklenecek.
#IBAN'a para gönderme yapıcam.
# 4 Haneli pin kodu yapıcam.
import hesaplar, bakiye_islemleri, islemler
admission = False
hesap = None

def menu_ayir(): # Menülerde farkındalığı sağlamak için kullandığımız sembolleri bu fonksiyon ile tek bir değişiklikle güncelleyebiliriz.
 return '*'*35

def giris_yap():
        global admission
        global hesap
        giris_hesap_no=input('Hesap numaranızı giriniz: ')
        if giris_hesap_no in hesaplar.uyeler:
            giris_hesap_sifre=input('Hesap şifrenizi giriniz: ')
            if giris_hesap_sifre == hesaplar.uyeler[giris_hesap_no]['hesap_sifre']:
                islemler.terminal_temizle()
                print('Başarılı giriş. Hesaba yönlendiriliyor...')
                admission = True
                hesap =  hesaplar.uyeler[giris_hesap_no]
            else:
                islemler.terminal_temizle()
                print('Geçersiz şifre.')
        else:
                islemler.terminal_temizle()
                print('Hesap numarası bulunamadı.')

# def kayit_ol():
# def admin_paneli():  Admin clası oluşturulup, o clasın içinde üyelik silme açma fonksiyonları eklenebilir.

def hesap_guvenligi():
    print(f'{menu_ayir()}\n1-Hesap Şifresini Değiştir \n2-Ana Menüye Geri Dön\n{menu_ayir()}')
    secim = input('Seçim yapınız:(1-2): ')
    if secim == '1':
        hesap_sifre_degistir()
    elif secim == '2':
        islemler.terminal_temizle()
        ana_menu()
    else:
        print('Hatalı giriş yaptınız.')

def hesap_sifre_degistir():
        global hesap
        sifre_dogrula = None
        while sifre_dogrula != hesap['hesap_sifre']:
            islemler.terminal_temizle()
            print(f'{menu_ayir()}\nŞİFRE DOĞRULAMA İŞLEMİ\n{menu_ayir()}')
            sifre_dogrula=input('Şu anda kullanmakta olduğunuz şifre: ')
            islemler.terminal_temizle()
        print(f'{menu_ayir()}\nŞİFRE DEĞİŞTİRME İŞLEMİ\n{menu_ayir()}')
        yeni_sifre=input('Kullanmak istediğiniz yeni şifreyi giriniz: ')
        hesap['hesap_sifre'] = yeni_sifre
        islemler.terminal_temizle()
        print(f'{hesap['hesap_no']} numaralı hesabınızın şifresi başarıyla değiştirildi.')
        
def ana_menu():
    global admission
    global hesap
    print(f'{menu_ayir()}\n1-Bakiye Görüntüle\n2-Para Çek\n3-Para Yatır\n4-Güvenlik\n5-Hesaptan Çıkış Yap\n{menu_ayir()}')
    secim = input('Seçim yapınız:(1-5): ')
    if secim == '1':
        bakiye_islemleri.bakiye_goruntule(hesap)
    elif secim == '2':
        bakiye_islemleri.para_cek(hesap)
    elif secim == '3':
        bakiye_islemleri.para_yatir(hesap)
    elif secim == '4':
        islemler.terminal_temizle()
        hesap_guvenligi()
    elif secim == '5':
        islemler.terminal_temizle()
        print('Çıkış Yapılıyor...')
        admission = False
        hesap = None
    else:
        print('Hatalı giriş yaptınız.')

while True:
    if admission == False or hesap == None:
        giris_yap()
    else:
        ana_menu()