class agacdügümü:
    def __init__(self,veri):
        self.veri=veri
        self.sol=None
        self.sağ=None

def önce_sol_dolas(dügüm):
     if dügüm is None:
         return
     
     önce_sol_dolas(dügüm.sol,)
     print(dügüm.veri,end=", ")
     önce_sol_dolas(dügüm.sağ)
    


kok = agacdügümü(13)
dugum7 = agacdügümü(7)
dugum15 = agacdügümü(15)
dugum3 = agacdügümü(3)
dugum8 = agacdügümü(8)
dugum14 = agacdügümü(14)
dugum19 = agacdügümü(19)
dugum18 = agacdügümü(18)


kok.sol = dugum7
kok.sağ = dugum15
dugum7.sol = dugum3
dugum7.sağ = dugum8
dugum15.sol = dugum14
dugum15.sağ = dugum19
dugum19.sol = dugum18

print("In-Order (Sıralı) Gezinti Sonucu:")

önce_sol_dolas(kok)


