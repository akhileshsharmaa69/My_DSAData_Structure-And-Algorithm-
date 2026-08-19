#Dequeue using doubly LinkedList 
class Node: 
    def __init__(self,data):
        self.data=data
        self.prev=None 
        self.next=None
class Dequeue:
    def __init__(self):
        self.front=None
        self.rear=None
    
    def insert_front(self,data):
        n=Node(data)
        
        if self.front is None: 
            self.front=n
            self.rear=n
            return 
        n.next=self.front
        self.front.prev=n
        self.front=n
        
    def insert_rear(self,data):
        n=Node(data)
        if self.front is None:
            print('Dequeue is empty')
            return 
        n.prev=self.rear
        self.rear.next=n
        self.rear=n
        
    def delete_front(self):
        if self.front is None: 
            print('Dequeue is empty')
            return
        item=self.front.data
        self.front=self.front.next
        if self.front is None:
            self.rear=None
        else:
            self.front.prev=None 
        return item
        
    def delete_rear(self):
        if self.front is None: 
            print('Dequeue is empty')
            return 
        item=self.rear.data
        self.rear=self.rear.prev
        if self.rear is None: 
            self.front=None 
        else:
            self.rear.next=None 
        return item
        
    def peek_front(self):
        if self.front is None: 
            print('Dequeue is empty')
            return 
        return self.front.data
    def peek_rear(self):
        if self.rear is None: 
            print('Dequeue is empty')
            return 
        return self.rear.data
        
    def isEmpty(self):
        return self.front is None   
        
    def display(self):
        if self.front is None: 
            print('Dequeue is empty')
            return 
        temp=self.front
        while temp is not None:
            print(temp.data,end="<->")  
            temp=temp.next
        print(None)     
               
d1=Dequeue()
d1.insert_front(10)
d1.insert_front(5)
d1.insert_rear(20) 
d1.insert_rear(30)  
print('deletetd front',d1.delete_front())
print('deletetd rear',d1.delete_rear())
print('front',d1.peek_front())
print('rear',d1.peek_rear())
print(d1.isEmpty())
d1.display()               
            