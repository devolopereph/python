#Kullanıcının sisteme giriş yapıp yapamamasını sağlayan kodu yazıyoruz.
#Doğru kullanıcı bilgilerini tuttuğumuz kısım.
username = 'admin'
password = 'admin'

#Kullanıcı bilgilerini sorduğumuz kısım.
usernameinput = input("kullanici adinizi giriniz: ")
passwordinput = input("kullanici sifrenizi giriniz: ")

#Şartlar doğruysa, isloggedin = True olacaktır ve hoş geldiniz mesajı gösterilecektir.
isloggedin = (usernameinput == username) and (passwordinput == password)

if isloggedin:
    print("hos geldiniz.")
#Eğer, isloggedin == True değil ise, yani kullanıcı adı veya şifre yanlış ise, aşağdıaki else komutu çalışacaktır.
else:
    print("lutfen bilgilerinizi kontrol ediniz.")