class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
        
class Dll:
    def __init__(self):
        self.start=None
        
    def _insert_start(self,data):
        n=Node(data)
        if self.start is None:
            self.start=n
            
        else:
            n.next=self.start
            self.start.prev=n
            self.start=n
            
    def insert_at_end(self,data):
        n=Node(data)
        
        if self.start is None:
            self.start=n
            
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
            n.prev=temp
                     
    def delete_at_first(self,data):
        
        if self.start is None:
            print('list is empty')
        
        elif self.start.next is None:
            self.start=None
        
        else:
            self.start=self.start.next
            self.start.prev=None 
              
    def delete_at_last(self):
        if self.start is None:
            print("list is empty")
            return
        elif self.start.next is None:
            self.start=None 
        temp=self.start   
        while temp.next is not None:
            temp=temp.next
        temp.prev.next=None      
                  
    def insert_at_specific(self,data,item):
        if self.start is None: 
            print("list is empty")   
            
        if self.start.next is not  None:
            self.start=None
            
        n=Node(data)
                
             
            
    def insert_before(self,data,item):
        n=Node(data) 
        temp=self.start
        while temp is not None and temp.data!=item:
            temp=temp.next
        if temp is None:
            print("item not found")
            return 
            
        n.prev=temp.prev
        n.next=temp
        if temp.prev is not None: 
            temp.prev.next=n
            
        else:
            self.start=n
        temp.prev=n    
        
    def insert_after(self,data,item):
        n=Node(data)
        temp=self.start
        
        while temp is not None and temp.data!=item:
            temp=temp.next
        if temp is None:
            print("item not found")   
            return
            
        n.next=temp.next
        n.prev=temp
        if temp.next is not None:
            temp.next.prev=n
            
        temp.next=n   
    def search(self,data):
        temp=self.start
        while temp is not None: 
            if temp.data==data:
                print("yes data is found",data)
                return True
                
            temp=temp.next
        return   False    
    
    def count_nodes(self):
        temp=self.start 
        count =0
        while temp is not None: 
            count=count+1
            temp=temp.next
        print (count)
        return count
        
    def reverse_display(self):
        if self.start is None: 
            print ("list is empty")
            return 
        temp=self.start
        
        while temp.next is not None: 
            temp=temp.next 
            
        while temp is not None:
            print(temp.data,end=" <-> ")
            temp=temp.prev
        print(None)  
        
    def insert_at_position(self,pos,data):
        n=Node(data)
        if pos==1:
            self._insert_start(data)
            return
        
        temp=self.start 
        count=1
        while temp is not None and count<pos-1:
            temp=temp.next
            count+=1
            
        if temp is None:
            print('invalid positions')
            return
            
        n.next=temp.next
        n.prev=temp
        if temp.next is not None:
            temp.next.prev=n
        temp.next=n        
              
              
                              
            
    def display(self):
        temp=self.start
        while temp is not None:
            print(temp.data,end=" <-> ")    
            temp=temp.next
        print(None)    
            

l1=Dll()
l1._insert_start(40)
l1._insert_start(30)
l1._insert_start(20)
l1._insert_start(10)
#l1.insert_at_end(50)
#l1.delete_at_first(10)
#l1.insert_before(35,40)
#l1.insert_after(31,30)
#l1.search(35)
#l1.search(30)
#l1.count_nodes()
#l1.reverse_display()
#l1.delete_at_last()
l1.insert_at_position(3,25)
l1.display()        
                
        