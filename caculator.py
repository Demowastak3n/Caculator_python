islemler = input("Islem turunu seciniz = (+, -, *, /, **, //, %)")
ne_kadar = int(input("Kaç tane sayiyla bi işlem yapmak istiyorsunuz? = "))
sayilar = []

for i in range(ne_kadar):
    sayi = int(input("Sayi giriniz = "))
    sayilar.append(sayi)

def topla(sayilar):
    sonuc = 0
    for sayi in sayilar:
        sonuc += sayi
    return sonuc
