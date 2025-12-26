class agacdügümü:
    def __init__(self, veri):
        self.veri = veri
        self.sol = None
        self.sağ = None

# ARAMA FONKSİYONU
def arama(düğüm, hedef):
    # 1. Durum: Düğüm boşsa veya aradığımızı bulduysak
    if düğüm is None or düğüm.veri == hedef:
        return düğüm

    # 2. Durum: Hedef değer küçükse, SOL tarafta ara
    if hedef < düğüm.veri:
        return arama(düğüm.sol, hedef)

    # 3. Durum: Hedef değer büyükse, SAĞ tarafta ara
    return arama(düğüm.sağ, hedef)

# --- Ağacı Oluşturma ---
kok = agacdügümü(13)
dugum7 = agacdügümü(7)
dugum15 = agacdügümü(15)
dugum3 = agacdügümü(3)
dugum8 = agacdügümü(8)
dugum14 = agacdügümü(14)
dugum19 = agacdügümü(19)
dugum18 = agacdügümü(18)

# Bağlantılar
kok.sol = dugum7
kok.sağ = dugum15
dugum7.sol = dugum3
dugum7.sağ = dugum8
dugum15.sol = dugum14
dugum15.sağ = dugum19
dugum19.sol = dugum18

# --- Test Edelim ---
aranan_sayi = 14
sonuc = arama(kok, aranan_sayi)

if sonuc:
    print(f"Buldum! Düğüm verisi: {sonuc.veri}")
else:
    print(f"{aranan_sayi} ağaçta yok.")

# Olmayan bir sayıyı arayalım
aranan_sayi2 = 99
sonuc2 = arama(kok, aranan_sayi2)

if sonuc2:
    print(f"Buldum! Düğüm verisi: {sonuc2.veri}")
else:
    print(f"{aranan_sayi2} ağaçta yok.")