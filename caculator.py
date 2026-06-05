Devam = True

import time

while Devam == True:
    islemler = input("Islem turunu seciniz = (+, -, *, /, **, //, %,q,e) " )

    if islemler == "q":
        Devam = False
        time.sleep(0.5)
        exit()

    if islemler == "e":
        repeat = True

    else:
        sayimiktar = int(input("Sayi  miktarini giriniz = "))

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


        def MODal(sayilar):
            sonuc = sayilar[0]
            for sayi in sayilar[1:]:
                sonuc %= sayi
            return sonuc


        def bol(sayilar):
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


        def TAMBol(sayilar):
            sonuc = sayilar[0]
            for sayi in sayilar[1:]:
                if sayi != 0:
                    sonuc //= sayi
                else:
                    print("Sifira bölme hatasi!")
                    return None
            return sonuc


        if islemler == "+":
            print("Cevap = ", topla(sayilar))
            time.sleep(0.5)
            print("Devam mi yeter mi? q yeter ve e devam anlamina gelir")

        elif islemler == "-":
            print("Cevap = ", cikar(sayilar))
            time.sleep(0.5)
            print("Devam mi yeter mi? q yeter ve e devam anlamina gelir")

        elif islemler == "*":
            print("Cevap = ", carp(sayilar))
            time.sleep(0.5)
            print("Devam mi yeter mi? q yeter ve e devam anlamina gelir")

        elif islemler == "/":
            print("Cevap = ", bol(sayilar))
            time.sleep(0.5)
            print("Devam mi yeter mi? q yeter ve e devam anlamina gelir")

        elif islemler == "%":
            print("Cevap = ", MODal(sayilar))
            time.sleep(0.5)
            print("Devam mi yeter mi? q yeter ve e devam anlamina gelir")

        elif islemler == "**":
            print("Cevap = ", USal(sayilar))
            time.sleep(0.5)
            print("Devam mi yeter mi? q yeter ve e devam anlamina gelir")

        elif islemler == "//":
            print("Cevap = ", TAMBol(sayilar))
            time.sleep(0.5)
            print("Devam mi yeter mi? q yeter ve e devam anlamina gelir")

        else:
            print("Baska islem kalmadi ahbap")

        if Devam == False:
            break
