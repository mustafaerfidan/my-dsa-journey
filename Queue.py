class queue():
    def __init__(self):
        self.liste=[]
    
    def is_empty(self):
        if len(self.liste)==0:
            return True
        else:
            return False

    def enqueue(self,data):
        self.liste.append(data)
    
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.liste.pop(0)
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.liste[0]
        

    
    