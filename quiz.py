# Basit bir Quiz uygulaması yapacağız.
import os

class Soru:
    def __init__(self, soru, cevaplar, cevap):
        self.soru = soru
        self.cevaplar = cevaplar
        self.cevap = cevap

    def soruOku(self, index):
        self.index=index
        print(f'{self.index}.Soru: {self.soru}')
        for i in self.cevaplar:
            print(f'- {i}')

    def cevapKontrol(self, cevap):
        return self.cevap == cevap
    
q1 = Soru("Python'da değişken tanımlamak için hangi sembol kullanılır?", ['=', '==', ':=', '==='], '=')
q2 = Soru("Hangisi Python’da bir döngü türüdür?", ['if-else', 'while', 'elif', 'switch'], 'while')
q3 = Soru("Python'da ekrana çıktı vermek için hangi fonksiyon kullanılır?", ['echo()', 'display()', 'print()', 'write()'], 'print()')
q4 = Soru("Python'da koşullu ifadeler hangi anahtar kelimeyle başlar?", ['if', 'when', 'case', 'switch'], 'if')

soru_listesi = [q1,q2,q3,q4]
tam_puan = 100
cikarilacak_puan=tam_puan//(len(soru_listesi))

for i in range(len(soru_listesi)):
    os.system('cls||clear')
    soru_listesi[i].soruOku(i+1)
    print(f'Kalan soru: {i+1}/{len(soru_listesi)}')
    if soru_listesi[i].cevapKontrol(input('Cevabınız: ')) == False:
        tam_puan -= cikarilacak_puan
os.system('cls||clear')
print(f'Quiz sona erdi.\nPuanınız: {tam_puan}')