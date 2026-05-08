iislemler = input("Islem turunu seciniz = (+, -, *, /, **, //, %) ")
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

if topla(sayilar):
    print(topla(sayilar))

elif cikar(sayilar):
    print(cikar(sayilar))

elif carp(sayilar):
    print(carp(sayilar))

elif MOD(sayilar):
    print(MOD(sayilar))

elif bolme(sayilar):
    print(bolme(sayilar))

elif USal(sayilar):
    print(USal(sayilar))
    
elif(tambolme(sayilar)):
    print(tambolme(sayilar))
    
else:
    print("Baska islem turu kalmadi amca")
