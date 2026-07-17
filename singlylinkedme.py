class Node:
    def __init__(self,data):
        self.data=data
        self. next=None
        
class LinkedList:
    def __init__(self):
        self.start=None
        
    def insert_data(self,data):
        n=Node(data)
        n.next=self.start
        self.start=n
        
    def delete_at_first(self):
        if self.start is not None:
            self.start=self.start.next  
            
    def delete_at_end(self):
        temp=self.start
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None 
    
    def delete_specific(self,data):
        if self.start is  None:
            print("List is empty:")
            return
        if self.start.data==data:
            self.start=self.start.next
            return 
            
        prev=None
        temp=self.start
        while temp is not None:
            if temp.data==data:
                prev.next=temp.next
                break
            prev=temp 
            temp=temp.next        
          
    def insert_at_end(self,data):
        n=Node(data)
        if self.start is None:
            self.start=n
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n   
            
    def insert_at_specific(self,item,data):
        n=Node(data)
        temp=self.start
        while temp is not None and temp.data!=item:
            temp=temp.next
        if temp is None:
            print(' item not found')
            return   
        n.next=temp.next
        temp.next=n  
        
    def _delete_complete_linklist(self):
        self.start = None
                                           
        
    def display(self):
        temp=self.start
        while temp is not None:
            print(temp.data,end=" -> ")   
            temp=temp.next
        print("None")       
l1=LinkedList()
l1.insert_data(40)
l1.insert_data(30)
l1.insert_data(20)
#l1.insert_at_specific(60,70)
l1.insert_data(10)
#l1.delete_specific(30)
l1.insert_at_end(50)
l1._delete_complete_linklist()
#l1.delete_at_first()
#l1.delete_at_end()
l1.display()