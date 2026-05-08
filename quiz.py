d = 0
y = 0
skor = 0
import time

sure = 0

soru1cevap = input("Turkiyenin Baskenti neresidir? = ")

if soru1cevap == "Ankara" or "ankara":
    print("Cevap dogru")
    d += 1
    skor += 10

else:
    print("Cevap yanlis")
    y += 1
    skor -= 5

    time.sleep(2)

    print("Tebrikler!Oyunu tamamladin")

    time.sleep(1.5)
print(d)
time.sleep(1.5)
print(y)
time.sleep(1.5)
print(skor)

if skor > 0:
    print("Genel kulturun iyi")

elif skor == 0:
    print("Genel kulturun 0")

else:
    print("Bu testte 1 soru var,sen bu testte degilsin")
