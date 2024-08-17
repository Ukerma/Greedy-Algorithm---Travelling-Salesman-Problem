# Kütüphaneler
import numpy as np                  # Matematiksel işlemler ve çok boyutlu diziler için kullanılır
import matplotlib.pyplot as plt     # Grafik çizimleri için kullanılır
import networkx as nx               # Graf teorisi işlemleri için kullanılır
import random                       # Rastgele sayı üretmek için kullanılır

sehirSayisi = 30
sehirler = [chr(i) for i in range(65, 65 + sehirSayisi)]
fiyat = random.randint(499,649)
yakit = 42


def rastgeleSehirKonumuOlustur(sehirSayisi, xLimit=125, yLimit=125):
    """
    Bu fonksiyon, şehirler için rastgele konumlar (x, y koordinatları) oluşturur.
    """
    sehirKonumlari = {}
    for i in range(sehirSayisi):
        sehirKonumlari[i] = (random.uniform(10, xLimit), random.uniform(10, yLimit))
    return sehirKonumlari

def mesafeMatrisiOlustur(sehirKonumlari):
    """
    Şehirler arasındaki mesafeleri hesaplayarak bir mesafe matrisi oluşturan fonksiyondur. 
    Oluşturulan matris, her bir şehir çifti arasındaki mesafeleri içerir.
    Numpy kütüphanesi olmadan çalışmaz. --> import numpy
    """
    sehirSayisi = len(sehirKonumlari)
    mesafeMatrisi = np.zeros((sehirSayisi, sehirSayisi))
    for i in range(sehirSayisi):
        for j in range(sehirSayisi):
            if i != j:
                fark = np.array(sehirKonumlari[i]) - np.array(sehirKonumlari[j])
                karelerToplami = np.sum(fark ** 2)
                mesafe = np.sqrt(karelerToplami)
                mesafeMatrisi[i][j] = mesafe
    return mesafeMatrisi

def rastgeleAliciSayilariOlustur(sehirSayisi, minAlici=2, maxAlici=12):
    """
    Her şehir için belirlenen minimum ve maksimum değerlere göre rastgele bir alıcı sayısı oluşturan fonksiyon.
    random kütüphanesi olmadan çalışmaz. --> import random
    """
    aliciSayilari = []
    for _ in range(sehirSayisi):
        aliciSayilari.append(random.randint(minAlici, maxAlici))
    return aliciSayilari

def karHesapla(tur, mesafeMatrisi, aliciSayilari, urunFiyati):
    """
    Belirli bir tur için toplam mesafeyi, toplam karı, yakıt ücretini ve elde edilen net karı hesaplayan fonksiyon.
    random kütüphanesi olmadan çalışmaz. --> import random
    """
    global yakit, fiyat
    yakitFiyati = yakit
    toplamMesafe = 0
    toplamKar = 0
    
    
    for i in range(len(tur) - 1):
        u = tur[i]
        v = tur[i + 1]
        toplamKar += aliciSayilari[v] * urunFiyati
        toplamMesafe += mesafeMatrisi[u][v]
    toplamMesafe += mesafeMatrisi[tur[-1]][tur[0]]
    toplamKar += aliciSayilari[tur[0]] * urunFiyati

    yakitUcreti = toplamMesafe * yakitFiyati
    eldeEdilenKar = toplamKar - yakitUcreti

    fiyat = urunFiyati

    return toplamMesafe, toplamKar, yakitUcreti, eldeEdilenKar

def karliTurOlustur(mesafeMatrisi, aliciSayilari, baslangicSehri, maximize=True):
    """
    Başlangıç şehrinden başlayarak en yüksek veya en düşük karı sağlayacak bir tur oluşturan fonksiyon. (Kar maksimizasyonu veya kar minimizasyonu)
    Greedy Algoritma'sını kullanır.
    """
    global fiyat
    sehirSayisi = len(mesafeMatrisi)
    ziyaretEdilenler = [False] * sehirSayisi
    tur = [baslangicSehri]
    ziyaretEdilenler[baslangicSehri] = True


    for _ in range(sehirSayisi - 1):
        enIyiSehir = None
        enIyiKar = -float('inf') if maximize else float('inf')
        for sonrakiSehir in range(sehirSayisi):
            denemeTur = tur + [sonrakiSehir]
            mesafe, _, _, _ = karHesapla(denemeTur, mesafeMatrisi, aliciSayilari, fiyat)
            sehirKar = aliciSayilari[sonrakiSehir] * fiyat
            if not ziyaretEdilenler[sonrakiSehir] and (not maximize or (sehirKar <= fiyat * mesafe)):
                yakitUcreti = mesafeMatrisi[tur[-1]][sonrakiSehir] * 42 # Yeni şehre gitmek için harcanacak yakıt ücreti
                eldeEdilenKar = aliciSayilari[sonrakiSehir] * fiyat
                netKar = eldeEdilenKar - yakitUcreti                    # Yeni şehirde elde edilecek kar
                
                
                if netKar <= 0:                                         # Eğer elde edilen kar yakıt ücretinden fazla değilse bu şehre uğrama
                    continue
                
                denemeTur = tur + [sonrakiSehir]
                _, _, _, kar = karHesapla(denemeTur, mesafeMatrisi, aliciSayilari, fiyat)
                
                if (maximize and (kar > enIyiKar)) or (not maximize and (kar < enIyiKar)):
                    enIyiKar = kar
                    enIyiSehir = sonrakiSehir
        
        if enIyiSehir is None:  # Eğer uygun bir şehir bulunamadıysa turu tamamla
            break
        
        tur.append(enIyiSehir)
        ziyaretEdilenler[enIyiSehir] = True
    
    
    if not maximize:                        # Eğer maksimize etmiyorsak  
        for sehir in range(sehirSayisi):    
            if not ziyaretEdilenler[sehir]: # Ve tüm şehirlere uğranmadıysa,
                tur.append(sehir)           # Uğranmayan şehirleri ekle
    
    return tur

def grafikCiz(tur, baslik):
    """
    Belirli bir turu grafik olarak çizmeyi sağlayan fonksiyon.
    networkx ve mathplotlib kütüphaneleri olmadan çalışmaz. --> import networkx , import mathplotlib
    """
    G = nx.DiGraph()
    for i in range(sehirSayisi):
        G.add_node(sehirler[i], pos=sehirKonumlari[i], label=f"{sehirler[i]}\n{aliciSayilari[i]}A")
    kenarEtiketleri = {}
    for i in range(len(tur) - 1):
        u = sehirler[tur[i]]
        v = sehirler[tur[i + 1]]
        G.add_edge(u, v)
        kenarEtiketleri[(u,v)] = int(mesafeMatrisi[tur[i]][tur[i + 1]])

    u = sehirler[tur[-1]]
    v = sehirler[tur[0]]
    G.add_edge(u, v)
    kenarEtiketleri[(u, v)] = int(mesafeMatrisi[tur[-1]][tur[0]])

    pos = nx.get_node_attributes(G, 'pos')
    labels = nx.get_node_attributes(G, 'label')
    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=700, node_color='skyblue', font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=kenarEtiketleri, font_color='red')
    plt.title(baslik)
    plt.show()


# ANA PROGRAM

baslangicSehri = 0                                                                                                                                               # Başlangıç şehrini seçme | 0->A , 1->B ...
sehirKonumlari = rastgeleSehirKonumuOlustur(sehirSayisi)                                                                                                         # Rastgele şehir pozisyonları oluşturma
mesafeMatrisi = mesafeMatrisiOlustur(sehirKonumlari)                                                                                                             # Mesafe matrisi oluşturma
aliciSayilari = rastgeleAliciSayilariOlustur(sehirSayisi)                                                                                                        # Rastgele alıcı sayıları oluşturma
enYuksekKarliTur = karliTurOlustur(mesafeMatrisi, aliciSayilari, baslangicSehri, maximize=True)                                                                  # En yüksek karlı tur için rota oluşturma
enDusukKarliTur = karliTurOlustur(mesafeMatrisi, aliciSayilari, baslangicSehri, maximize=False)                                                                  # En düşük karlı tur için rota oluşturma
enYuksekKarliMesafe, enYuksekKazanilanPara, enYuksekYakitUcreti, enYuksekEldeEdilenKar = karHesapla(enYuksekKarliTur, mesafeMatrisi, aliciSayilari, fiyat)       # En yüksek karlı rota için hesaplamalar
enDusukKarliMesafe, enDusukKazanilanPara, enDusukYakitUcreti, enDusukEldeEdilenKar = karHesapla(enDusukKarliTur, mesafeMatrisi, aliciSayilari, fiyat)            # En düşük karlı rota için hesaplamalar

# KONSOLA YAZDIRMAK İÇİN

print("En yüksek karlı olan rota:", [sehirler[i] for i in enYuksekKarliTur])
print("Rotanın mesafesi:", int(enYuksekKarliMesafe))
print("Kazanacağı para:", int(enYuksekKazanilanPara))
print("Yakıt ücreti:", int(enYuksekYakitUcreti))
print("Elde edeceği kar:", int(enYuksekEldeEdilenKar))
print(" ")
print("En düşük karlı olan rota:", [sehirler[i] for i in enDusukKarliTur])
print("Rotanın mesafesi:", int(enDusukKarliMesafe))
print("Kazanacağı para:", int(enDusukKazanilanPara))
print("Yakıt ücreti:", int(enDusukYakitUcreti))
print("Elde edeceği kar:", int(enDusukEldeEdilenKar))
print(" ")
print("Ürünün birim fiyatı:", fiyat)

# GRAFIK OLUŞTURMAK İÇİN

grafikCiz(enYuksekKarliTur, 'En Yüksek Karlı Tur')
grafikCiz(enDusukKarliTur, 'En Düşük Karlı Tur')
