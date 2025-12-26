class HashTable:
    def __init__(self,size):
        self.size=size
        self.tablo=[]
        for i in range(size):
            self.tablo.append([])
    def hash_formülü(self,anahtar):
        return anahtar % self.size

    def ekle(self,eleman):
        index=self.hash_formülü(eleman)
        self.tablo[index].append(eleman)

    def bul(self,aranan):
        index=self.hash_formülü(aranan)
        hedef_liste=self.tablo[index]
        if aranan in hedef_liste:
            return True
        else:
            return False
    def silme(self,silinecek):
        index = self.hash_formülü(silinecek)
        hedef_liste=self.tablo[index]

        if silinecek in hedef_liste:
            hedef_liste.remove(silinecek)
        else:
            print("silinecek değer bulunamadi ")

hash_yapısı=HashTable(10)
hash_yapısı.ekle(10)
hash_yapısı.ekle(13)
hash_yapısı.ekle(28)
hash_yapısı.ekle(34)
hash_yapısı.ekle(44)
hash_yapısı.ekle(41)
hash_yapısı.ekle(50)

print(hash_yapısı.bul(10))
print(hash_yapısı.bul(5))
print(hash_yapısı.bul(41))

hash_yapısı.silme(41)

print(hash_yapısı.bul(41))

        



                
