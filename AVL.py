class AVLdugumu:
    def __init__(self,data):
        self.data=data
        self.sol=None
        self.sağ=None
        self.yukseklik=1


def yukseklik_al(dugum):
    if dugum is None:
        return 0
    
    return dugum.yukseklik




def denge_faktoru(dugum):
    if dugum is None:
        return 0
    return yukseklik_al(dugum.sol) - yukseklik_al(dugum.sağ)




def yukseklik_guncelle(dugum):
    if dugum is None:
        return 
    
    sol_boy = yukseklik_al(dugum.sol)

    sağ_boy = yukseklik_al(dugum.sağ)

    dugum.yukseklik= 1 + max(sol_boy,sağ_boy)


def dugum_ekleme(dugum,data):

    if dugum is None :
        return AVLdugumu(data)
    
    if dugum.data<data:
        dugum.sağ=dugum_ekleme(dugum.sağ,data)

    elif dugum.data>data:
        dugum.sol=dugum_ekleme(dugum.sol,data)
    
    else:
        return dugum
    
    yukseklik_guncelle(dugum)


    denge = denge_faktoru(dugum)

    if denge > 1 and data<dugum.sol.data:
        return saga_dondur(dugum)
        
        
    if denge < -1 and data > dugum.sağ.data :

        return sola_dondur(dugum)
    
    if denge > 1 and data > dugum.sol.data:

        dugum.sol = sola_dondur(dugum.sol) 
        return saga_dondur(dugum)
    
    if denge < -1 and data < dugum.sağ.data:

        dugum.sağ=saga_dondur(dugum.sağ)
        return sola_dondur(dugum)

    
    return dugum


def saga_dondur(y): #Verilen 'y' düğümü etrafında SAĞA döndürme yapar.

    x=y.sol          # x: y'nin sol çocuğu (Yeni Tepe olacak)

    T2 = x.sağ       # T2: x'in sağındaki olası fazlalık (y'nin soluna geçecek) T2 burda geçici değişkendir 

    x.sağ = y        # x'in sağına y'yi (eski tepeyi) al

    y.sol = T2       # y'nin boşa çıkan soluna T2'yi tak


    yukseklik_guncelle(y)     # Önce aşağıya inen 'y' güncellenmeli, sonra tepeye çıkan 'x'.

    yukseklik_guncelle(x)   

    return x   # 4. Yeni kökü (x) geri döndürür burdaki amaç y nin babasının x e bağlanması için fonksyon return x yapıyor 

def sola_dondur(y): #Verilen 'y' düğümü etrafında sola döndürme yapar

    x = y.sağ

    T2 = x.sol

    x.sol = y 
    
    y.sağ = T2

    yukseklik_guncelle(y)

    yukseklik_guncelle(x)

    return x





#-------------------------------------------------------------------------------------------------------------------------------------






    

    