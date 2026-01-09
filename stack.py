class stack:
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        if len(self.items)==0:
            return True
        else:
            return False
        
    def push(self,data):
        self.items.append(data)
    
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop()
    
    def peek(self):
        if self.is_empty() :
            return None
        else:
            return self.items[-1]



def parantez_kontrol(metin):
    s=stack()
    sözlük={"(":")"}

    for i in metin:
        if i=="(" :
            s.push(i)
        elif i==")":
            if s.is_empty():
                return False
            else:
                s.pop()
    if s.is_empty():
        return True
    else:
        return False
    
