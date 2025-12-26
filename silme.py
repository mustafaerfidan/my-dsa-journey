class AgacDugumu:
    def __init__(self, veri):
        self.veri = veri
        self.sol = None
        self.sag = None

# ---------------------------------------------------------
# 1. EKLEME FONKSİYONU (Insert)
# ---------------------------------------------------------
def ekle(dugum, yeni_veri):
    # Eğer bulunduğumuz yer boşsa, düğümü buraya oluştur
    if dugum is None:
        return AgacDugumu(yeni_veri)

    # Veri küçükse SOL'a git
    if yeni_veri < dugum.veri:
        dugum.sol = ekle(dugum.sol, yeni_veri)
    
    # Veri büyükse SAĞ'a git
    elif yeni_veri > dugum.veri:
        dugum.sag = ekle(dugum.sag, yeni_veri)
        
    return dugum

# ---------------------------------------------------------
# 2. SIRALI DOLAŞMA FONKSİYONU (In-Order Traversal)
# ---------------------------------------------------------
def sirali_dolas(dugum):
    if dugum is None:
        return

    sirali_dolas(dugum.sol)        # Önce SOL
    print(dugum.veri, end=" ")     # Sonra YAZDIR
    sirali_dolas(dugum.sag)        # Sonra SAĞ

# ---------------------------------------------------------
# 3. SİLME İÇİN YARDIMCI: EN KÜÇÜK DEĞERİ BULMA
# ---------------------------------------------------------
def en_kucuk_degeri_bul(dugum):
    mevcut = dugum
    # Sol taraf boş olana kadar git (En küçük değer en soldadır)
    while mevcut.sol is not None:
        mevcut = mevcut.sol
    return mevcut

# ---------------------------------------------------------
# 4. SİLME FONKSİYONU (Delete)
# ---------------------------------------------------------
def sil(dugum, silinecek_veri):
    # Ağaç boşsa işlem yapma
    if dugum is None:
        return None

    # Silinecek veriyi ara
    if silinecek_veri < dugum.veri:
        dugum.sol = sil(dugum.sol, silinecek_veri)
    elif silinecek_veri > dugum.veri:
        dugum.sag = sil(dugum.sag, silinecek_veri)
    
    else:
        # --- DÜĞÜM BULUNDU! ---
        
        # Durum 1 & 2: Çocuğu yoksa veya tek çocuğu varsa
        if dugum.sol is None:
            temp = dugum.sag
            dugum = None
            return temp
        elif dugum.sag is None:
            temp = dugum.sol
            dugum = None
            return temp

        # Durum 3: İki Çocuğu Varsa
        # Sağ tarafın en küçüğünü (halef) bul
        temp = en_kucuk_degeri_bul(dugum.sag)

        # O değeri, silinenin yerine kopyala
        dugum.veri = temp.veri

        # Kopyasını aldığımız düğümü eski yerinden sil
        dugum.sag = sil(dugum.sag, temp.veri)

    return dugum

# =========================================================
# TEST ALANI (Ana Program)
# =========================================================

# 1. Ağacı Başlat
root = None
sayilar = [13, 7, 15, 3, 8, 14, 19, 18]

print("--- 1. Ağaç Oluşturuluyor ---")
for sayi in sayilar:
    root = ekle(root, sayi)
    print(f"{sayi} eklendi.")

print("\n--- 2. Silmeden Önce Sıralı Liste ---")
sirali_dolas(root)
print("\n")

# 2. Silme İşlemi
silinecek_sayi = 15
print(f"--- 3. {silinecek_sayi} Sayısı Siliniyor ---")
root = sil(root, silinecek_sayi)

print("\n--- 4. Sildikten Sonra Sıralı Liste ---")
sirali_dolas(root)
print("\n\n(Not: 15 listeden gitti, ancak sıralama (küçükten büyüğe) bozulmadı.)")