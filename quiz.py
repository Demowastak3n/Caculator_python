d = 0
y = 0
skor = 0
import time

sure = 0

soru1 = input("Turkiyenin Baskenti neresidir? = ")

if soru1 == "Ankara" or "ankara":
    print("Cevap dogru")
    d += 1
    skor += 10

else:
    print("Cevap yanlis")
    y += 1
    skor -= 5

soru2 = input("Avrupadaki toprak sekli en buyuk ulke neresidir? = ")
if soru2 == "Rusya" or "rusya":
    print("Cevap dogru")
    d += 1
    skor += 10
else:
    print("Cevap yanlis")
    y += 1
    skor -= 5

soru3 = input("Dunyanin en yuksek dagi nerededir? = ")
if soru3 == "Nepal" or "nepal":
    print("Cevap dogru")
    d += 1
    skor += 10
else:
    print("Cevap yanlis")
    y += 1
    skor -= 5

soru4 = input("Dunyanin en derin noktasinin ismi nedir? = ")
if soru4 == "Mariana" or "mariana":
    print("Cevap dogru")
    d += 1
    skor += 10
else:
    print("Cevap yanlis")
    y += 1
    skor -= 5

soru5 = input("Dunyanin capi yaklasik olarak kac kmdir? = ")
     if soru5 == "13000Km" or "13 000 Km":
            print("Cevap dogru")
            d += 1
            skor += 10

        elif soru5 == "13000km" or "13 000 km":
            print("Cevap dogru")
            d += 1
            skor += 10

        else:
            print("Cevap yanlis")
            y += 1
            skor -= 5
