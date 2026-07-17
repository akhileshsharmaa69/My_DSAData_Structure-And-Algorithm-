class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
        #insert_beginning

    def insert_beginning(self, data):
        n = Node(data)
        n.next = self.start
        self.start = n
        # insert_at_last
    def insert_at_last(self,data):
        n=Node(data)    
        if self.start is None:
            self.start=n
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
            
            #insert_after
    def insert_after(self,item,data):
        temp=self.start
        while temp is not None: 
            if temp.data==item:
                n=Node(data)  
                n.next=temp.next
                temp.next=n
                break
            temp=temp.next 
               
    def delete_at_first(self):
        if self.start is None:
            print("List is empty: ")    
        else:
            self.start=self.start.next 
            
    def delete_at_lastnode(self):
        if self.start is None:
            print('list is empty')
        elif self.start.next is None:
            self.start=None 
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
        
    def delete_item(self,data):
        if self.start is None:
            print("List is empty")
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
            
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.data==data:
                return True
            temp=temp.next
        return False
    
    def count_nodes(self):
        count=0
        temp=self.start
        while temp is not None:
            count=count+1
            temp=temp.next
        return count
        
    def reverse(self):
        prev=None
        current=self.start
        while current is not None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.start=prev   
               
    def insert_before(self,item,data):
        
        n=Node(data)
        if self.start is None:
           print('list is empty')
           return
        if self. start==item:
            n.next=self.start
            self.start=n
            return
        prev=None
        temp=self.start
        while temp is not None:
            if temp.data==item:
               n.next=temp
               prev.next=n
               break
            prev = temp
            temp=temp.next
            
    def display(self):
        temp = self.start

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")
        

l1 = LinkedList()

l1.insert_beginning(30)
l1.insert_beginning(20)
l1.insert_beginning(10)
l1.insert_after(30,35)
l1.insert_at_last(50)
#l1.delete_at_first()
#print(l1.count_nodes())
#l1.reverse()
#l1.delete_at_lastnode()
l1.insert_before(30,25)
l1.display()

    