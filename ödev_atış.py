import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

g = 10
maksimum_mermi_hizi = 1800
minimum_mermi_hizi = 330
mermi_acisi = 30
mermi_uçuş_süresi = 0
mermi_uçuş_mesafesi = 0
hedef_mesafesi = 20000 + (200 * np.random.randint(-10, 10))
hedef_boyutu = 1000 + (100 * np.random.randint(-2, 2))
ates_noktasi_yukseklik_farki = 9
atis_deneme_sayisi = 0
hedef_vuruldu = False
while not hedef_vuruldu:
    mermi_hizi = (maksimum_mermi_hizi + minimum_mermi_hizi) / 2
    if hedef_mesafesi <= mermi_uçuş_mesafesi <= hedef_mesafesi + hedef_boyutu:
        hedef_vuruldu = True
        print("Hedef vuruldu!")
        print("Ateş denemesi sayısı: ", atis_deneme_sayisi)
        print("Mermi hızı: ", mermi_hizi)
        break
    else:
        mermi_x_ekseni_hizi = round((math.cos(math.radians(mermi_acisi))) * mermi_hizi)
        mermi_y_ekseni_hizi = round((math.sin(math.radians(mermi_acisi))) * mermi_hizi)
        mermi_uçuş_süresi = round(((mermi_y_ekseni_hizi / 10) * 2) + 0.07)
        mermi_uçuş_mesafesi = round(mermi_x_ekseni_hizi * mermi_uçuş_süresi)

        if hedef_mesafesi >= mermi_uçuş_mesafesi:
            print("Mermi hedefin önüne düştü.")
            minimum_mermi_hizi = mermi_hizi
        elif mermi_uçuş_mesafesi >= hedef_mesafesi + hedef_boyutu:
            print("Mermi hedefin arkasına isabet etti.")
            maksimum_mermi_hizi = mermi_hizi

        atis_deneme_sayisi += 1

fig, ax = plt.subplots()
kare = patches.Rectangle((hedef_mesafesi, 0), hedef_boyutu, 200, edgecolor='red', facecolor='red')
ax.add_patch(kare)
t = np.linspace(0, mermi_uçuş_süresi, num=500)
mermi_hizi = (maksimum_mermi_hizi + minimum_mermi_hizi) / 2
x = mermi_hizi * t * np.cos(math.radians(mermi_acisi))
y = mermi_hizi * t * np.sin(math.radians(mermi_acisi)) - 0.5 * g * t ** 2 + ates_noktasi_yukseklik_farki
plt.plot(x, y, label='Mermi izi')
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.xticks(range(0, int(hedef_mesafesi + hedef_boyutu + 5000) + 1, 2500))
plt.yticks(range(0, int(5000) + 1, 500))
plt.show()