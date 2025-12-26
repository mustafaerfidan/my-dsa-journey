class min_heap:
    def __init__(self):
        self.heap=[]
    
    def parent_bul(self,index):
        parent_index=(index-1)//2
        return parent_index       
    
    def sol_cocuk_bul(self,index):
        sol_cocuk_index=(index*2)+1
        return sol_cocuk_index
    
    def sag_cocuk_bul(self,index):
        sag_cocuk_index=(index*2)+2
        return sag_cocuk_index
    
    def ekleme(self,eklenen):
        self.heap.append(eklenen)
        eklenen_index=len(self.heap)-1

        while eklenen_index>0 and self.heap[eklenen_index]<self.heap[self.parent_bul(eklenen_index)]:
            parent_index=self.parent_bul(eklenen_index)

            geçici=self.heap[eklenen_index]
            self.heap[eklenen_index]=self.heap[parent_index]
            self.heap[parent_index]=geçici
            eklenen_index=parent_index
    
    def silme(self):
        if len(self.heap)==0:
            return None
        elif len(self.heap)==1:
            return self.heap.pop()
        silinen=self.heap[0]
        self.heap[0]=self.heap[-1]
        self.heap.pop()
        index=0
        while self.sol_cocuk_bul(index)<len(self.heap):
            sol=self.sol_cocuk_bul(index)
            sag=self.sag_cocuk_bul(index)
            enkucuk=sol

            if sag < len(self.heap) and self.heap[sol]>self.heap[sag]:
                enkucuk=sag
            
            if self.heap[index]<self.heap[enkucuk]:
                return silinen
            
            else:
                geçici=self.heap[index]
                self.heap[index]=self.heap[enkucuk]
                self.heap[enkucuk]=geçici
                index=enkucuk
        return silinen

          
