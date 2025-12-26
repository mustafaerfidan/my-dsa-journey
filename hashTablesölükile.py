class hashTable:
    def __init__(self,size):
        self.size=size
        self.tablo=[]
        for i in range(size):
            self.tablo.append([])

    def hash_formülü(self,anahtar):
        return anahtar%self.size
    
    def ekle(self,anahtar,deger):
        index=self.hash_formülü(anahtar)
        self.tablo[index].append([anahtar,deger])
    
    def bul (self,aranan):
        index=self.hash_formülü(aranan)
        hedef_liste=self.tablo[index]
        for i in hedef_liste:
            if i[0]==aranan:
                return i[1]
        return False
    def silme(self,silinecek):
        index=self.hash_formülü(silinecek)
        hedef_liste=self.tablo[index]
        for i in hedef_liste:
            if i[0]==silinecek:
                hedef_liste.remove(i)
                return True
        return False



# --- SENİN YAZDIĞIN CLASS BURADA DURUYOR ---

# --- TEST KISMI ---
okul = hashTable(5)  # 5 Boyutlu küçük bir tablo açtık

# Ekleme Yapalım
okul.ekle(10, "Mustafa")
okul.ekle(15, "Ahmet")   # 10 ve 15 çakışır (mod 5'e göre ikisi de 0. index)
okul.ekle(22, "Zeynep")

print("--- Arama Testi ---")
print("10 Numaralı öğrenci:", okul.bul(10))   # Mustafa dönmeli
print("15 Numaralı öğrenci:", okul.bul(15))   # Ahmet dönmeli (Çakışmayı çözüp bulmalı)
print("99 Numaralı öğrenci:", okul.bul(99))   # False dönmeli

print("\n--- Silme Testi ---")
okul.silme(10) # Mustafa'yı siliyoruz
print("10 Numara silindikten sonra:", okul.bul(10)) # Artık False dönmeli
    


        