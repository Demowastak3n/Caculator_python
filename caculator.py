import time


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


def bol(sayilar):
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
        if sayi != 0:
            sonuc /= sayi
        else:
            print("Sıfıra bölme hatası!")
            return None
    return sonuc


def MODal(sayilar):
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
        if sayi != 0:
            sonuc %= sayi
        else:
            print("Sıfıra mod alma hatası!")
            return None
    return sonuc


def USal(sayilar):
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
        sonuc **= sayi
    return sonuc


def TAMBol(sayilar):
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
        if sayi != 0:
            sonuc //= sayi
        else:
            print("Sıfıra bölme hatası!")
            return None
    return sonuc


Devam = True

while Devam:

    islemler = input("İşlem türünü seçiniz (+, -, *, /, **, //, %) : ")
    sayimiktar = int(input("Sayı miktarını giriniz: "))

    sayilar = []

    for i in range(sayimiktar):
        sayi = int(input(f"{i+1}. sayıyı giriniz: "))
        sayilar.append(sayi)

    if islemler == "+":
        print("Cevap =", topla(sayilar))

    elif islemler == "-":
        print("Cevap =", cikar(sayilar))

    elif islemler == "*":
        print("Cevap =", carp(sayilar))

    elif islemler == "/":
        print("Cevap =", bol(sayilar))

    elif islemler == "%":
        print("Cevap =", MODal(sayilar))

    elif islemler == "**":
        print("Cevap =", USal(sayilar))

    elif islemler == "//":
        print("Cevap =", TAMBol(sayilar))

    else:
        print("Geçersiz işlem seçtiniz!")

    time.sleep(1.5)

    durum = input("Devam etmek için 'e', çıkmak için 'q' giriniz: ").lower()

    if durum == "q":
        Devam = False

print("Program sonlandırıldı.")
