islemler = input("Islem turunu seciniz = (+, -, *, /, **, //, %) ")
sayimiktar = int(input("Kac tane sayi girmek istersiniz? = "))

sayilar = []

for i in range(sayimiktar):
    sayi = int(input("Sayi giriniz = "))
    sayilar.append(sayi)

def topla(sayilar):
    sonuc = 0
    for sayi in sayilar:
        sonuc += sayi
    return sonuc

def cikar(sayilar):
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
        sonuc -= sayi
    return sonuc

if islemler == "+":
    print("Toplam = ", topla(sayilar))
elif islemler == "-":
    print("Fark = ", cikar(sayilar))
