class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
       
class cll:
    def __init__(self):      
        self.last=None
        
    def insert_at_start(self,data):
        n=Node(data)
        if self.last is None:
            self.last=n
            n.next=n
            
        else:
            n.next=self.last.next
            self.last.next=n
    
    def insert_at_end(self,data):
        n=Node(data)
        if self.last is None: 
            self.last=n
            n.next=n   
            
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
            
    def delete_at_first(self): 
        if self.last is None:
            print("list is empty")
            return 
            
        if self.last.next==self.last:
            self.last=None
            
        else:
            temp=self.last.next    
            self.last.next=temp.next 
    
    def delete_at_last(self):
        if self.last is None:      
            print('list is empty')
            return 
            
        if self.last.next==self.last:
            self.last=None
            return 
                        
        temp=self.last.next 
        while temp.next!=self.last:
            temp=temp.next
            
        temp.next=self.last.next
        self.last =temp  
        
    def search (self,item):
        if self.last is None: 
            print ('list is empty')
            return
            
        temp=self.last.next 
        while True: 
            if temp.data==item:
                print('item found')
                return True 
            temp=temp.next    
                
            if temp==self.last.next: 
                break 
                
        print ("item not found")         
        return False
        
    def count_nodes(self):
        if self .last is None: 
            print('lost is empty')
            return count0
            
        temp=self.last.next 
        count =0
        
        while True: 
            count +=1
            temp=temp.next 
            
            if temp==self.last.next: 
                break
                
        print ('total count=',count)
        return count      
      
    def insert_after(self,item,data):
        if self.last is None: 
            print("list is empty: ")     
            return 
        temp=self.last.next 
        
        while True: 
            if temp.data==item:
                n=Node(data)
                n.next=temp.next 
                temp.next=n
                
                if temp==self.last:
                  self.last=n
                return 
            temp=temp.next
            
            if temp==self.last.next:
                break
        print ("item not found: ")  
    
    def insert_at_before(self,item,data): 
        if self.last is None: 
            print('list is empty')    
            return 
        
        if self.last.next.data==item:
            self. insert_at_start(data)
            return 
                
        prev=self.last.next
        temp=prev.next
        
        while temp != self.last:
            if temp.data==item:
                n=Node(data)
                n.next=temp
                prev.next=n
                return 
                            
            prev=temp
            temp=temp.next
        print("item not found")    
      
    def delete_after(self,item):
        if self.last is None: 
            print('list is empty: ')
            return
            
        if self.last.next==self.last:
            print('only one node present')  
            return
            
        temp=self.last.next 
        while True: 
            if temp.data==item:
                delete=temp.next
                if delete==self.last:
                   self.last=temp
                   
                temp.next=delete.next
                del delete
                print("node deletetd successfully:")
                return
                 
            temp=temp.next
            if temp==self.last.next:
             break
        print("item not found")            
                
                
    def delete_before(self,item):
        if self.last is None:
            print('list is empty:')
            return
            
        if self.last.next==self.last:
            print('only one node is present')
            return
        if self.last.next.data==item:
            temp=self.last.next
            
            while temp.next!=self.last:
                temp=temp.next
            temp.next=self.last.next    
            del self.last
            self.last=temp
            print('node delete successfully')
            return 
                        
        prev=self.last
        temp=self.last.next 
        current=temp.next 
        while True: 
            
            if current.data==item:
                prev.next=current 
                del temp
                print("node deletetd successfully")
                return 
            prev=temp
            temp=current 
            current=current.next 
            
            if current ==self.last.next:
                break
        print("item not found")        
            
    def reverse(self):
        if self.last is None: 
            print('list is empty')
            
        if self.last.next==self.last:
            return 
            
        prev=self.last
        temp=self.last.next 
        current=temp.next 
        
        while current!=self.last.next:
            temp.next=prev
            prev=temp
            temp=current 
            current=current.next
        
        temp.next=prev
        self.last=self.last.next    
    
    def update(self,old_data,new_data):
        if self.last is None: 
            print('list is empty')
            return 
        temp=self.last.next 
        while True:
            if temp.data==old_data:
                temp.data=new_data
                print("data update successfully: ")     
                return 
            temp=temp.next
            if temp==self.last.next: 
                break
        print("item not found")     
        
    def sorted(self):
        if self.last is None:
            print('list is empty')    
            return
        if self.last.next==self.last:
            print("only one present")
            return
            
        count=self.count_nodes()
        for i in range(count-1):
            temp=self.last.next 
            for j in range(count-1):
                if temp.data>temp.next.data:
                   x=temp.data
                   temp.data=temp.next.data
                   temp.next.data=x
        temp=temp.next 
        print("Sorted successfully")           
        
    def display(self):
        if self.last is None:
            print("List is empty")   
            return 
        
        temp=self.last.next
        while temp!=self.last: 
            print(temp.data,end="->")  
            temp=temp.next
        print(temp.data)  
        
c1=cll()
c1.insert_at_start(30)
c1.insert_at_start(20)
c1.insert_at_start(10)
c1.insert_at_end(40)
#c1.delete_at_first ()
#c1.delete_at_last()
#c1.count_nodes() 
#c1.insert_after()
#c1.insert_at_before(40,35)
#c1.insert_at_before(10,5)
#c1.delete_after(40)
#c1.delete_before(10)
#c1.search (70)
#c1.reverse()
#c1.update(10,5)
c1.display()
c1.sorted()      
        