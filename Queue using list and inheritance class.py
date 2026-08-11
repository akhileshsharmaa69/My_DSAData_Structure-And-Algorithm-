#Queue using list
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
class Queue:
    def __init__(self):
        self.front=None 
        self.rear=None 
        
    def enqueue(self,data):
        n=Node(data)
        if self.front is None: 
            self.front=n
            self.rear=n
            return 
        self.rear.next=n
        self.rear=n
        
    def dequeue(self):
        if self.front is None: 
            print('Queue is empty:')
            return
        item=self.front.data
        self.front=self.front.next
        if self.front is None:
            self.rear=None 
        return item    
    
    def peek(self):
        if self.front is None: 
            print('Queue is empty')
            return
        return self.front.data   
        
    def isEmpty(self):
        return self.front is None
    
    def display(self):
        if self.front is None: 
            print('Queue is empty')
            return 
        temp=self.front
        while temp is not None: 
            print(temp.data,end="->")
            temp=temp.next    
        print("None")    
        
q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
print('deletetd',q1.dequeue())
print('front',q1.peek())
print(q1.isEmpty())
q1.display()'''


#Queue using inheritance 
class Node: 
    def __init__(self,data):
        self.data=data
        self.next=None
       
class LinkedList:
    def __init__(self):
        self.start=None 
        
class Queue(LinkedList):
    def __init__(self):
        super().__init__()
        self.rear=None 
    def enqueue(self,data):
        n=Node(data)
        if self.start is None: 
            self.start=n
            self.rear=n
            return 
        self.rear.next=n
        self.rear=n
    def dequeue(self):
        if self.start is None: 
            print('Queue is empty')
            return
        item=self.start.data
        self.start=self.start.next
        if self.start is None:
            self.rear=None 
        return item
    def peek(self):
        if self.start is None: 
            print('Queue is empty')    
            return 
        return self.start.data
    def isEmpty(self):
        return self.start is None   
    def display(self):
        if self.start is None:
            print('Queue is empty:')
            return
        temp=self.start 
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next   
        print("None")                    
        
        
q1=Queue() 
q1.enqueue(10) 
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
print('deletetd',q1.dequeue()) 
print('front element',q1.peek())
print(q1.isEmpty())
q1.display()