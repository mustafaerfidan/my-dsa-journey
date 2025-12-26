class maxHeap:
    def __init__(self):
        self.heap=[]

    def parent_bul(self,index):
        parent=(index-1)//2
        return parent
    

    def sol_cocuk_bul(self,index):
        sol_cocuk=(index*2)+1
        return sol_cocuk

    def sag_cocuk_bul(self,index):
        sag_cocuk=(index*2)+2
        return sag_cocuk
    
    def ekle(self,eleman):
        self.heap.append(eleman)
        index=len(self.heap)-1
        while index>0 and self.heap[index]>self.heap[self.parent_bul(index)]:
            parent_index=self.parent_bul(index)

            geçici=self.heap[index]
            self.heap[index]=self.heap[parent_index]
            self.heap[parent_index]=geçici
            index=parent_index


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
            enbuyuk=sol

            if sag < len(self.heap) and self.heap[sag] > self.heap[sol]:
                enbuyuk = sag

            if self.heap[enbuyuk]<self.heap[index]:
                return silinen
            else:
                geçici=self.heap[index]
                self.heap[index]=self.heap[enbuyuk]
                self.heap[enbuyuk]=geçici
                index=enbuyuk
           
        return silinen







            

    

        