islemler = input("Islem turunu seciniz = (+, -, *, /, **, //, %)")
sayimiktar = float(input("Kac tane sayi girmek istersiniz? = "))
sayilar = []
for i in range(sayimiktar):
    sayi = int(input("Sayi giriniz = "))
    sayilar.append(sayi)
def topla(sayilar):
    sonuc = 0
    for sayi in sayilar:
        sonuc += sayi
    return sonuc
