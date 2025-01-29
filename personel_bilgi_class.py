#PErsonel adında bir class tanımlıyoruz.
class Personel:
    def __init__(self, ad_soyad, dogum_yili, bolum):
        self.ad_soyad = ad_soyad
        self.dogum_yili = dogum_yili
        self.bolum = bolum
    
    def bilgi(self):
        print(f'Personelin adı ve soyadı: {self.ad_soyad}\nPersonelin yaşı: {2025-self.dogum_yili}\nPersonelin bölümü: {self.bolum}')

eleman = Personel('Devoloper Eph',2000,'Güvenlik')
eleman.bilgi()