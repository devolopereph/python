# Basit bir Quiz uygulaması yapacağız.
import os
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def readQuestion(self, index):
        self.index=index
        print(f'{self.index}.Soru: {self.text}')
        for i in self.choices:
            print(f'- {i}')

    def checkAnswer(self, answer):
        return self.answer == answer
    
class Quiz(Question):
    def __init__(self, text, choices, answer):
        super().__init__(text, choices, answer)
        self.score = 0
        self.questionIndex = 0

q1 = Question("Python'da değişken tanımlamak için hangi sembol kullanılır?", ['=', '==', ':=', '==='], '=')
q2 = Question("Hangisi Python’da bir döngü türüdür?", ['if-else', 'while', 'elif', 'switch'], 'while')
q3 = Question("Python'da ekrana çıktı vermek için hangi fonksiyon kullanılır?", ['echo()', 'display()', 'print()', 'write()'], 'print()')
q4 = Question("Python'da koşullu ifadeler hangi anahtar kelimeyle başlar?", ['if', 'when', 'case', 'switch'], 'if')
liste = [q1,q2,q3,q4]
tam_puan=100
cikarilacak_puan=tam_puan//(len(liste))
for i in range(len(liste)):
    os.system('cls||clear')
    liste[i].readQuestion(i+1)
    print(f'Kalan soru: {i+1}/{len(liste)}')
    if liste[i].checkAnswer(input('Cevabınız: ')) == False:
        tam_puan -= cikarilacak_puan
os.system('cls||clear')
print(f'Quiz sona erdi.\nPuanınız: {tam_puan}')