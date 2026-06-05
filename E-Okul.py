ogrenci = {

    "Isim": "",
    "Yas": 0,
    "Sinif": 0,

}

ogrenci["Isim"] = input("Ogrenci adini giriniz = ")
ogrenci["Yas"] = int(input("Ogrenci Yasini giriniz = "))
ogrenci["Sinif"] = int(input("Ogrencinin kacinci Sinif oldugunugiriniz = "))

dersler = [ ]

def Mat():

    Mat = {

        "Birinci Sinav Notu": 0,
        "Ikinci Sinav Notu": 0,
        "Sozlu Notu": 0,

    }

    Mat["Birinci Sinav Notu"] = int(input("Birinci Sinav Notu = "))
    Mat["Ikinci Sinav Notu"] = int(input("Ikinci Sinav Notu = "))
    Mat["Sozlu  Notu"] = int(input("Sozlu Notu = "))

def Turk():

    Turk = {
        "Birinci Sinav Notu": 0,
        "Ikinci Sinav Notu": 0,
        "Sozlu Notu": 0,
    }

    Turk["Birinci Sinav Notu"] = int(input("Birinci Sinav Notu = "))
    Turk["Ikinci Sinav Notu"] = int(input("Ikinci Sinav Notu = "))
    Turk["Sozlu  Notu"] = int(input("Sozlu Notu = "))

def Fen():

    Fen = {

        "Birinci Sinav Notu": 0,
        "Ikinci Sinav Notu": 0,
        "Sozlu Notu": 0,

    }

    Fen["Birinci Sinav Notu"] = int(input("Birinci Sinav Notu = "))
    Fen["Ikinci Sinav Notu"] = int(input("Ikinci Sinav Notu = "))
    Fen["Sozlu  Notu"] = int(input("Sozlu Notu = "))

def Ing():

    Ing = {
        "Birinci Sinav Notu": 0,
        "Ikinci Sinav Notu": 0,
        "Sozlu Notu": 0,
    }

    Ing["Birinci Sinav Notu"] = int(input("Birinci Sinav Notu = "))
    Ing["Ikinci Sinav Notu"] = int(input("Ikinci Sinav Notu = "))
    Ing["Sozlu  Notu"] = int(input("Sozlu Notu = "))

def ort():
    secim = input("Hangi dersin ortalamasini hesaplamak istiyorsunuz? = ")
    
    Mat_ort = ((Mat["Birinci Sinav Notu"] * 2) + (Mat["Ikinci Sinav Notu"] * 2) + Mat["Sozlu  Notu"]) / 5
    
    Turk_ort = ((Turk["Birinci Sinav Notu"] * 2) + (Turk["Ikinci Sinav Notu"] * 2) + Turk["Sozlu  Notu"]) / 5
    
    Fen_ort = ((Fen["Birinci Sinav Notu"] * 2) + (Fen["Ikinci Sinav Notu"] * 2) + Fen["Sozlu  Notu"]) / 5
    
    Ing_ort = ((Ing["Birinci Sinav Notu"] * 2) + (Ing["Ikinci Sinav Notu"] * 2) + Ing["Sozlu  Notu"]) / 5
    
    Ort = ((Mat_ort * 3) + (Turk_ort * 2) + (Fen_ort * 2) + (Ing_ort * 1)) / 8
