import pandas as pd
import numpy as np

yaşlar = [15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65]
c1 = 16
c2 = 22


def merkez(yaş, cluster_1, cluster_2):
    c1_fark = abs(yaş - cluster_1)
    c2_fark = abs(yaş - cluster_2)
    if c2_fark > c1_fark:
        return cluster_1
    elif c1_fark >= c2_fark:
        return cluster_2


def find_cluster(cluster1, cluster2):
    c1_toplam = 0
    c2_toplam = 0
    a = 0
    b = 0

    for yaş in yaşlar:
        nearest_cluster = merkez(yaş, cluster1, cluster2)
        if nearest_cluster == cluster2:
            b += 1
            c2_toplam += yaş
        elif nearest_cluster == cluster1:
            a += 1
            c1_toplam += yaş
    return c1_toplam / a, c2_toplam / b


c1_son = c1
c2_son = c2

sonuç = []

for i in range(1, 5):
    c1, c2 = find_cluster(c1_son, c2_son)

    data = []
    for yaş in yaşlar:
        c1_fark = abs(yaş - c1_son)
        c2_fark = abs(yaş - c2_son)
        cluster = "1" if merkez(yaş, c1_son, c2_son) == c1_son else "2"
        new_cluster = c1 if cluster == "1" else c2
        data.append([yaş, f"{c1_son:.2f}", f"{c2_son:.2f}", f"{c1_fark:.2f}", f"{c2_fark:.2f}", cluster,
                     f"{new_cluster:.2f}"])

    df = pd.DataFrame(data, columns=["Xi", "C1", "C2", "Fark 1", "Fark 2", "En Yakın Küme", "Küme Merkezi"])

    sonuç.append({
        'Iterasyon': i,
        'Küme Merkezleri': {'c1': c1, 'c2': c2},
        'Sonuçlar': df
    })

    c1_son = c1
    c2_son2 = c2

for p in sonuç:
    print(f"Iterasyon: {p['Iterasyon']}")
    print("Küme Merkezleri:", p['Küme Merkezleri'])
    print("Sonuçlar:")
    print(p['Sonuçlar'])
    print()

