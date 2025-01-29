#Kullanıcının sisteme giriş yapıp yapamamasını sağlayan kodu yazıyoruz.
#Doğru kullanıcı bilgilerini tuttuğumuz kısım.
username = 'admin'
password = 'admin'

#Kullanıcı bilgilerini sorduğumuz kısım.
usernameinput = input("Kullanıcı adınızı giriniz: ")
passwordinput = input("Kullanıcı şifrenizi giriniz: ")

#Şartlar doğruysa, if, yani eğer çalışacaktır ve hoş geldiniz mesajı gösterilecektir.
if (usernameinput == username) and (passwordinput == password):
    print("Hoş geldiniz.")
#Eğer, ifde belirttiğimiz şartlar doğru değil ise, else komutu çalışacaktır.
else:
    print("Lütfen bilgilerinizi kontrol ediniz.")
