import random
import os
os.system("pip install random")
# Kullanıcıdan bilgileri alın
ad = input("Adınızın ilk 3 harfini girin: ")
soyad = input("Soyadınızın ilk 2 harfini girin: ")
ozel = input("Özel bir simge giriniz: ")
hayvan = input("En sevdiğiniz hayvan: ")
rakm = input("rastgele 3 haneli rakam yazınız: ")


# Karakter listelerini oluşturun
harfler = [ch for ch in ad + soyad]
rakamlar = [ch for ch in ozel]
hayv = [ch for ch in hayvan]
rakama = [ch for ch in rakm]
# Karakterleri karıştırın
random.shuffle(harfler)
random.shuffle(rakamlar)
random.shuffle(hayv)
random.shuffle(rakama)

# Şifreyi oluşturun
sifre = ''.join(harfler + rakamlar + hayv + rakama)

# Oluşturulan şifreyi ekrana yazdırın
print("Oluşturulan şifre:", sifre)
