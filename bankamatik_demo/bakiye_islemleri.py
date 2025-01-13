import islemler

def bakiye_goruntule(hesap):
        islemler.terminal_temizle()
        print(f'{hesap['hesap_no']} numaralı hesabınızda işlem yapmaktasınız. Hoş geldin {hesap['ad_soyad']}!\nBakiye: {hesap['bakiye']} TL\nKullanılabilir Ek Hesap Bakiyesi: {hesap['ek_hesap_bakiye']} TL\nEk Hesap Bakiye Limiti: {hesap['ek_hesap_bakiye_limit']} TL')

def para_yatir(hesap): # Burada string veri girdiğimizde program çöküyor,  
                                    #string girildiğinde lütfen  sayısal değer giriniz demesini istiyorum, sayısal değer girene kadar hata versin.
    islemler.terminal_temizle()
    miktar = int(input(f'{hesap['hesap_no']} numaralı hesabınıza yatırmak istediğiniz para miktarını giriniz: '))
    print('Lütfen miktarı sayı olarak giriniz.')
    if (miktar > 0):
        secim = input(f'{hesap['hesap_no']} numaralı hesabınıza {miktar} TL para yatırma işlemini onaylıyor musunuz? (e/h):').upper()
        islemler.terminal_temizle()
        if secim == 'E':
            hesap['bakiye'] += miktar
            print(f'{hesap['hesap_no']} numaralı hesabınıza {miktar} TL para yatırılmıştır.')
        elif secim == 'H':
            print(f'{hesap['hesap_no']} numaralı hesabınıza {miktar} TL para yatırma işleminiz isteğiniz üzere iptal edilmiştir. ')
        else:
             print('Hatalı giriş yapıldı.')
    else:
        islemler.terminal_temizle()
        print('Geçersiz para miktarı girdiniz.')
        
def para_cek(hesap):
    islemler.terminal_temizle()
    print(f'Bakiye: {hesap['bakiye']} TL\nKullanılabilir Ek Hesap Bakiyesi: {hesap['ek_hesap_bakiye']} TL\nEk Hesap Bakiye Limiti: {hesap['ek_hesap_bakiye_limit']} TL')
    miktar=int(input('Çekmek istediğiniz para miktarını giriniz: '))
    if (miktar > 0):
        if hesap['bakiye']>= miktar:
            islemler.terminal_temizle()
            print(f'{hesap['hesap_no']} numaralı hesabınızdan {miktar} TL para çekme talebinde bulundunuz.')
            print('Bu işlem için ek hesabınız kullanılmayacaktır.')
            para_cekimi_onay = str(input(f'{miktar} TL Para çekimi işlemini onaylıyor musunuz(e/h): '))
            if para_cekimi_onay.upper() == 'E':
                hesap['bakiye'] -= miktar
                islemler.terminal_temizle()
                print(f'{hesap['hesap_no']} numaralı hesabınızdan {miktar} TL para çekilmiştir. Kalan bakiye: {hesap['bakiye']} TL, ek hesabınız kullanılmamıştır.')
            elif para_cekimi_onay.upper() == 'H':
                islemler.terminal_temizle()
                print(f'{hesap['hesap_no']} numaralı hesabınızdan {miktar} TL para çekme işlemi isteğiniz üzere iptal edilmiştir. ')
            else:
                islemler.terminal_temizle()
                print('Geçersiz giriş yaptınız.')
        else:
            if (hesap['bakiye'] + hesap['ek_hesap_bakiye']) >=  miktar:
                ek_hesap_cekilecek_miktar = miktar - hesap['bakiye']
                islemler.terminal_temizle()
                print(f'Ek hesabınız ile birlikte {miktar} TL çekebilirsiniz.\n{hesap['ek_hesap_bakiye']} TL bakiyeli ek hesabınızdan {ek_hesap_cekilecek_miktar} TL çekilecektir. ')
                ek_hesap_onay = str(input('Ek hesap kullanımını onaylıyor musunuz? (e/h): '))
                if ek_hesap_onay.upper() == 'E':
                    hesap['bakiye'] = 0
                    hesap['ek_hesap_bakiye'] -= ek_hesap_cekilecek_miktar
                    islemler.terminal_temizle()
                    print(f'Ek hesapla birlikte toplam {miktar} TL para çekildi.')
                    print(f'{hesap['hesap_no']} Nolu hesabınızdan kalan:\nBakiye: {hesap['bakiye']}\nEk Hesap Bakiyesi: {hesap['ek_hesap_bakiye']}')
                elif ek_hesap_onay.upper() == 'H':
                    print(f'{miktar} TL Para çekme işlemi isteğiniz üzerine iptal edildi.')
                else:
                    print('Hatalı giriş yapıldı.')
            else:
                islemler.terminal_temizle()
                print(f'{hesap['hesap_no']} numaralı hesabınızda yeterli miktarda bakiye ve limit bulunmamaktadır. \nDilerseniz canlı desteğe bağlanarak limit arttırma talebinde bulunabilirsiniz.')
    else:
        islemler.terminal_temizle()
        print('Geçersiz para miktarı girdiniz.')

# def para_gonder():