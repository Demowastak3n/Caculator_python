""""
islemler = input("Islem turunu seciniz = (+, -, *, /, **, //, %) ")
sayimiktar = int(input("Kac tane sayi girmek istersiniz? = "))

sayilar = []

for i in range(sayimiktar):
    sayi = int(input("Sayi giriniz = "))
    sayilar.append(sayi)


def topla(sayilar):
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
        sonuc += sayi
    return sonuc


def cikar(sayilar):
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
        sonuc -= sayi
    return sonuc


def carp(sayilar):
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
        sonuc *= sayi
    return sonuc


def MOD(sayilar):
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
        sonuc %= sayi
    return sonuc


def bolme(sayilar):
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
        if sayi != 0:
            sonuc /= sayi
        else:
            print("Sifira bölme hatasi!")
            return None
    return sonuc


def USal(sayilar):
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
        sonuc **= sayi
    return sonuc


def tambolme(sayilar):
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
        if sayi != 0:
            sonuc //= sayi
        else:
            print("Sifira bölme hatasi!")
            return None
    return sonuc


if islemler == "+":
    print(topla(sayilar))

elif islemler == "-":
    print(cikar(sayilar))

elif islemler == "*":
    print(carp(sayilar))

elif islemler == "%":
    print(MOD(sayilar))

elif islemler == "/":
    print(bolme(sayilar))

elif islemler == "**":
    print(USal(sayilar))

elif islemler == "//":
    print(tambolme(sayilar))

else:
    print("Baska islem turu kalmadi amca")
    """
