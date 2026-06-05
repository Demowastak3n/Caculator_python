ogrenci = {
    "Isim": "",
    "Yas": 0,
    "Sinif": 0,
}

ogrenci["Isim"] = input("Ogrenci adini giriniz = ")
ogrenci["Yas"] = int(input("Ogrenci Yasini giriniz = "))
ogrenci["Sinif"] = int(input("Ogrencinin kacinci Sinif oldugunu giriniz = "))


def Mat():
    mat = {}

    mat["Birinci Sinav Notu"] = int(input("Birinci Sinav Notu = "))
    mat["Ikinci Sinav Notu"] = int(input("Ikinci Sinav Notu = "))
    mat["Sozlu Notu"] = int(input("Sozlu Notu = "))

    return mat


def Turk():
    turk = {}

    turk["Birinci Sinav Notu"] = int(input("Birinci Sinav Notu = "))
    turk["Ikinci Sinav Notu"] = int(input("Ikinci Sinav Notu = "))
    turk["Sozlu Notu"] = int(input("Sozlu Notu = "))

    return turk


def Fen():
    fen = {}

    fen["Birinci Sinav Notu"] = int(input("Birinci Sinav Notu = "))
    fen["Ikinci Sinav Notu"] = int(input("Ikinci Sinav Notu = "))
    fen["Sozlu Notu"] = int(input("Sozlu Notu = "))

    return fen


def Ing():
    ing = {}

    ing["Birinci Sinav Notu"] = int(input("Birinci Sinav Notu = "))
    ing["Ikinci Sinav Notu"] = int(input("Ikinci Sinav Notu = "))
    ing["Sozlu Notu"] = int(input("Sozlu Notu = "))

    return ing


def ort():
    secim = input(
        "Hangi dersin ortalamasini hesaplamak istiyorsunuz? (MatO, TurkO, FenO, IngO) = "
    )

    if secim == "MatO":
        mat = Mat()

        Mat_ort = (
            (mat["Birinci Sinav Notu"] * 2)
            + (mat["Ikinci Sinav Notu"] * 2)
            + mat["Sozlu Notu"]
        ) / 5

        print(ogrenci["Isim"], "Matematikten Ortalama", Mat_ort, "aldi")

    elif secim == "TurkO":
        turk = Turk()

        Turk_ort = (
            (turk["Birinci Sinav Notu"] * 2)
            + (turk["Ikinci Sinav Notu"] * 2)
            + turk["Sozlu Notu"]
        ) / 5

        print(ogrenci["Isim"], "Turkceden Ortalama", Turk_ort, "aldi")

    elif secim == "FenO":
        fen = Fen()

        Fen_ort = (
            (fen["Birinci Sinav Notu"] * 2)
            + (fen["Ikinci Sinav Notu"] * 2)
            + fen["Sozlu Notu"]
        ) / 5

        print(ogrenci["Isim"], "Fenden Ortalama", Fen_ort, "aldi")

    elif secim == "IngO":
        ing = Ing()

        Ing_ort = (
            (ing["Birinci Sinav Notu"] * 2)
            + (ing["Ikinci Sinav Notu"] * 2)
            + ing["Sozlu Notu"]
        ) / 5

        print(ogrenci["Isim"], "Ingilizceden Ortalama", Ing_ort, "aldi")

    else:
        print("Gecersiz secim!")


ort()
