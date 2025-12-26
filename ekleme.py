class agacdügümü:
    def __init__(self, veri):
        self.veri = veri
        self.sol = None
        self.sağ = None

# EKLEME FONKSİYONU
def ekle(düğüm, yeni_veri):
    # 1. Durum: Eğer yer boşsa, yeni düğümü buraya oluştur
    if düğüm is None:
        return agacdügümü(yeni_veri)

    # 2. Durum: Veri küçükse SOLa ekle (recursive)
    if yeni_veri < düğüm.veri:
        düğüm.sol = ekle(düğüm.sol, yeni_veri)
    
    # 3. Durum: Veri büyükse SAĞa ekle (recursive)
    elif yeni_veri > düğüm.veri:
        düğüm.sağ = ekle(düğüm.sağ, yeni_veri)
    
    # Değişiklik yapılmış düğümü geri döndür (bağlantıyı güncellemek için)
    return düğüm

# --- Test Edelim: Ağacı Sıfırdan Otomatik Oluşturalım ---

# Önce sadece kökü oluşturuyoruz
kok = agacdügümü(13)

# Şimdi diğer sayıları sırayla ekleyelim (Slayttaki sırayla)
# Slayt 29'daki düğümler: 7, 15, 3, 8, 14, 19, 18
ekle(kok, 7)
ekle(kok, 15)
ekle(kok, 3)
ekle(kok, 8)
ekle(kok, 14)
ekle(kok, 19)
ekle(kok, 18)

# Doğru eklenip eklenmediğini kontrol etmek için "Sıralı Dolaşma" (In-Order) yapalım.
# Eğer sonuç küçükten büyüğe sıralı çıkarsa, kod doğru çalışıyor demektir.
def sirali_dolas(düğüm):
    if düğüm is None:
        return
    sirali_dolas(düğüm.sol)
    print(düğüm.veri, end=", ")
    sirali_dolas(düğüm.sağ)

print("Otomatik oluşturulan ağacın sıralı hali:")
sirali_dolas(kok)