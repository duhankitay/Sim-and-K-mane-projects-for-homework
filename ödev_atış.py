import random
import math
import matplotlib.pyplot as plt

def atis_simulasyonu(a, b, mesafe):
    n = 1
    vurus_x = []
    vurus_y = []
    while True:
        v_son = random.randint(a, b)
        t = v_son / 20
        v_son_x = v_son * math.cos(30) - 10 * t
        v_son_y = v_son * math.sin(30)

        yatay = v_son_x * t * 2
        vurus_x.append(yatay)
        vurus_y.append(v_son_y)

        if abs(mesafe - yatay) < 0.01:
            print("Hedefi vurdun!")
            print("Deneme sayısı:", n)
            print("Gereken hız:", v_son)
            break
        elif mesafe - yatay > 0:
            print("Önüne düştü.")
            a = v_son - (v_son - a) * 0.1
        else:
            print("Uzağına düştü.")
            b = v_son + (b - v_son) * 0.1
        n += 1

    plt.plot(vurus_x, vurus_y, 'bo-')
    plt.xlabel('Atış Mesafesi (m)')
    plt.ylabel('Yükseklik (m)')
    plt.grid(True)
    plt.show()

atis_simulasyonu(330, 1800, 20000 + 200 * random.randint(-2, 2))
