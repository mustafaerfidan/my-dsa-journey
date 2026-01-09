class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.header=node(None)
        self.trailer=node(None)
        self.header.next=self.trailer
        self.trailer.prev=self.header
        self.size=0
    
    def insert_between(self,data,baş,son):
        new_node=node(data)

        new_node.next=son
        new_node.prev=baş

        baş.next=new_node
        son.prev= new_node

        self.size += 1

        return new_node
    
    def basa_ekle(self,data):
        self.insert_between(data,self.header,self.header.next)
    
    def sona_ekle(self,data):
        self.insert_between(data,self.trailer.prev,self.trailer)
    
    def silme(self,data):
        baş=data.prev
        son=data.next
        baş.next=son
        son.prev=baş
        self.size -= 1
    def baştan_silme(self):
        if self.header.next == self.trailer :
            return
        else:
            self.silme(self.header.next)
        

    def sondan_silme(self):
        if self.header.next == self.trailer :
            return
        else:
            self.silme(self.trailer.prev)
        

    def yazdir(self):
        if self.header.next == self.trailer :
            return
        else:
            temp=self.header.next
            while temp != self.trailer :
                print(temp.data)
                temp=temp.next

        

    



