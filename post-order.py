class agacdügümü:
    def __init__(self, veri):
        self.veri = veri
        self.sol = None
        self.sağ = None

# Post-Order (Sonra Kök) Dolaşma Fonksiyonu
def sonra_kok_dolas(düğüm):
    if düğüm is None:
        return

    # 1. Önce en SOLa git
    sonra_kok_dolas(düğüm.sol)

    # 2. Sonra SAĞa git
    sonra_kok_dolas(düğüm.sağ)

    # 3. İşin bitince KÖKÜ yazdır (En son burası çalışır)
    print(düğüm.veri, end=", ")

# --- Ağacı Tekrar Oluşturalım ---
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

print("Post-Order (Sonra Kök) Gezinti Sonucu:")
sonra_kok_dolas(kok)