#Dequeue using list 
'''class Dequeue:
    def __init__(self):
        self.item=[]
        
    def insert_rear(self,data):
        self.item.append(data)
        
    def insert_front(self,data):
        self.item.insert(0,data)
        
    def delete_front(self):
        if len(self.item)==0:
            print("Dequeue is empty")
            return 
        return self.item.pop(0)
    
    def delete_rear(self):
        if len(self.item)==0:
            print("Dequeue is empty")
            return 
        return self.item.pop()     
        
    def peekfront(self):
        if len(self.item)==0:
            print('Dequeue is empty')
            return
        return self.item[0]
    def peekrear(self):
        if len(self.item)==0:
            print("Dequeue is empty")
            return 
        return self.item[-1]
        
    def isEmpty(self):
        return len(self.item)==0 
          
    def display(self):
        if len(self.item)==0:
            print("Dequeue is empty")
            return 
        for item in self.item:
            print(item,end="->")   
        print('None')      
        
d1=Dequeue()
d1.insert_rear(10) 
d1.insert_rear(20)
d1.insert_front(5)
d1.insert_front(1) 
print("front element",d1.peekfront()) 
print("last element", d1.peekrear())
d1.isEmpty()
d1.display()  '''         


    