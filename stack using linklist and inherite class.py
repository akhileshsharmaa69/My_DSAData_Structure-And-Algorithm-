#stack using linklist:
'''class Node:
    def __init__(self,data=None): 
        self.data=data
        self.next=None 
class stack:
    def __init__(self):
        self.top=None
    
    def push(self,data):
        n=Node(data)
        n.next=self.top
        self.top=n
     
    def pop(self):
        if self.top is None:
            print("list is underflow")
            return
        item=self.top.data #data copy
        self.top=self.top.next 
        return item  
        
    def peek(self):
        if self.top is None:
            print('list is empty: ')
            return
        #print('your top element is ',self.top.data)# it is only print the value of a screen
        return self.top.data  #return the top value of a send  outside the function          
        
    def isEmpty(self):
        if self.top is None: 
            return True 
        return False
        
        
        
        
        
    def display(self):
        if self.top is None:
            print('stack is empty')
            return 
        temp=self.top    
        while temp is not None: 
            print(temp.data,end="->")
            temp=temp.next
        print('None')      
        
l1=stack()
l1.push(10)
l1.push(20)
l1.push(30)
l1.push(40) 
a=l1.peek()
print("top is",a)
print(l1.isEmpty())
#x = l1.pop()
#print(x)
l1.pop()
l1.display() ''' 
 
#  Stack by inheriting LinkedList 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
        
class LinkedList: #parent class
    def __init__(self):
        self.start=None
        
    def insert_begin(self,data):
        n=Node(data)
        if self.start is None:
            self.start=n
            return
        n.next=self.start
        self.start=n
    
    def delete_begin(self):
        if self.start is None: 
            print('stack is empty: ')
            return
        item=self.start.data
        self.start=self.start.next
        return item
        
    def display(self):
        if self.start is None: 
            print('stack is empty')
            return
        temp=self.start
        while temp is not None:
            print(temp.data,end="->")       
            temp=temp.next
        print(None)  
        
    def isEmpty(self):
        if self.start is None:
            return True 
        return False    
               
        
                 
        
        
              
        
class stack(LinkedList): #inherit by the parent class
    def push(self,data):
        self.insert_begin(data)  
        
    def pop(self):
         return self.delete_begin()       
         
    def display(self):
        super().display() 
           
    def isEmpty(self):
         return super().isEmpty()   
        
    def peek(self):
        if self.start is None: 
            print('stack is empty')
            return
        return self.start.data       
        
    
          
        
        
        
        
        
        
        
        
        
        
s1=stack()
s1.push(10)  
s1.push(20)
s1.push(30)
s1.push(40)
#s1.pop() 
#print(s1.peek())
print(s1.isEmpty())
s1.display()