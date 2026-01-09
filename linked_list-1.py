
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None
    
    def basa_ekle(self,data):
       new_node=node(data)
       new_node.next=self.head
       self.head=new_node
    
    def sona_ekle(self,data):
        new_node=node(data)
        if self.head == None:
            self.basa_ekle(data)
        else:
            temp=self.head
            while temp.next != None :
                temp=temp.next
            temp.next=new_node

    def bastan_sil(self):
        if self.head == None :
            return
        else:
            self.head=self.head.next
    def sondan_sil(self):
        if self.head == None :
            return
        
        elif self.head.next == None :
            self.bastan_sil()

        else:
            temp=self.head
            while temp.next.next != None:
                temp=temp.next
            temp.next=None

    def yazdir(self):
        temp=self.head
        while temp != None:
            print(temp.data)
            temp=temp.next
    
    def ters_cevir(self):
        temp=self.head
        prev=None
        next=None
        while temp != None :
            next=temp.next
            temp.next=prev
            prev=temp
            temp=next
        self.head=prev
    
       
        
