
sys_username = "talha"
sys_password = "123456"
kullanici_adi = input("Kullanıcı Adını Giriniz: ")
sifre = input("Şifre'yi Giriniz: ")
print("çözmek için 2ye tıklayınız")
if (kullanici_adi == sys_username) and (sifre != sys_password):
    print("Şifre yanlış..")

elif (kullanici_adi != sys_username) and (sifre == sys_password):
    print("Kullanıcı adı yanlış..")

elif (kullanici_adi != sys_username) and (sifre != sys_password):
    print("Kullanıcı adı ve şifre yanlış..")
else:
    print("Giriş yapıldı!")

    veri = input("çözmek istediğiniz metini yazınız: ")

    sayı = int(veri)

    print("kriptolanmış şifreniz: ", sayı * 2/6*9*75+9999+65865844*9)
if sayı == 2:

     print ("kriptonun çözümü",sayı * 99)
