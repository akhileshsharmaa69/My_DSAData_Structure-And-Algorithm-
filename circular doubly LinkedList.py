class Node: 
    def __init__(self,item):
        self.prev=None 
        self.data=item
        self.next=None
        
class CDLL:
    def __init__(self):
        self.last=None
        
    def insert_start(self,data):
        n=Node(data) 
        if self.last is None:
            n.next=n
            n.prev=n
            self.last=n
            
        n.next=self.last.next 
        self.last.next.prev=n
        self.last.next=n
        n.prev=self.last   
        
    def insert_last(self,data):
        n=Node(data)
        if self.last is None: 
            n.next=n
            n.prev=n
            self.last=n
            return
        n.prev=self.last
        n.next=self.last.next
        self.last.next.prev=n
        n.prev=self.last
        self.last.next=n
        self.last=n   
        
    def delete_first(self):
        if self.last is None: 
            print("List is empty") 
            return
        if self.last.next ==self.last:
            del self.last 
            self.last=None 
            print("node deletetd successfully")
            return 
        temp=self.last.next
        self.last.next=temp.next
        temp.next.prev=self.last
        del temp
        print("node deletetd successfully")
        return           
        
    def delete_last(self):
        if self.last is None: 
            print('list is empty')
            return 
        if self.last.next == self.last:
            del self.last 
            self.last=None
            print("node deletetd")   
        temp=self.last
        temp.prev.next=temp.next 
        temp.next.prev=temp.prev
        self.last =temp.prev
        del temp
        print("node deletetd")
        return
        
    def insert_before(self,data,item):
        if self.last is None: 
            print('list is empty:') 
            return
        temp=self.last.next 
        while True: 
            if temp.data==item: 
                if temp==self.last.next: 
                    self.insert_start(data)
                    print("Node inserted successfully")  
                    return
                n=Node(data)
                n.next=temp
                n.prev=temp.prev 
                temp.prev.next =n
                temp.prev=n
                print("Node inserted successfully:")
                return 
            temp=temp.next
            if temp==self.last.next:
                break
        print("item not found")   
        
    def insert_after(self,item,data):
        if self.last is None: 
            print("list is empty")
            return
        temp=self.last.next 
        while True: 
            if temp.data==item:
                n=Node(data)
                n.prev=temp
                n.next=temp.next
                temp.next.prev=n
                temp.next=n
                if temp==self.last:
                    self.last=n
                print("node inserted successfully: ")    
                return 
            temp=temp.next 
            if temp==self.last.next:
               break
        print("item not found")                   
        
    def delete_before(self,item):
        if self.last is None:
            print('list is empty')
            return
        if self.last.next == self.last:
            print("insert before not possible:")
            return
        temp=self.last.next
        while True: 
            if temp.data==item:
                delete=temp.prev 
                
                if delete == temp:
                    print("delete not possible")
                    return 
                current =delete.prev 
                
                current.next=temp
                temp.prev=current 
                
                if delete==self.last:
                   self.last=current 
                del delete
                print("node deleted successfully: ")
                return
                   
            temp=temp.next
            if temp==self.last.next:
              break
        print ('item not found')               
                       
    def delete_after(self,item):
        if self.last is None:
            print('list is empty:')
            return 
        if self.last.next==self.last:
            print("not possible delete after") 
            return 
        temp=self.last.next 
        while True: 
            if temp.data==item:
                delete=temp.next  
                #if delete==temp:
                #only two node present 
                if delete.next==temp:
                    temp.next=temp
                    temp.prev=temp
                    self.last=temp
                    print("delete node successfully:")
                    return 
                current=delete.next 
                temp.next=current 
                current.prev=temp
                if delete==self.last:
                    self.last=temp
                del delete 
                print("node deletetd successfully: ")
                return 
            temp=temp.next
            if temp==self.last.next:
                break
        print("item not found")              
          
    def search(self,data):
        if self.last is None:
            print('list is empty')
            return 
        temp=self.last.next 
        while True:
            if temp.data==data:
                print(temp.data,"item found")
                return 
            temp=temp.next
            if temp==self.last.next:
                break
        print("itemm not found")                 
        
    def reverse_list(self):
        if self.last is None: 
            print('list is empty')
            return
        temp=self.last 
        while True: 
            print(temp.data,end="<-> ")  
            temp=temp.prev
            if temp==self.last:
             break
        print('your list is reverse')   
        
    def delete_item(self,item):
        if self.last is None: 
            print("list is empty") 
            return 
        if self.last.next==self.last:
            if self.last.data==item:
                self.last=None
                print("node deletetd successfully")
            else:
                print("item not found") 
            return
                
        temp=self.last.next
        while True: 
            if temp.data==item:
                if temp==self.last.next:
                    self.delete_first()
                    return
                elif temp==self.last:
                    self.delete_last()
                    return 
                else:
                    temp.prev.next=temp.next
                    temp.next.prev=temp.prev
                    del temp
                    print("node deletetd successfully")
                    return
            temp=temp.next
            if temp==self.last.next:
                break
        print('item not found')                 
                       
    def count(self):
        if self.last is None: 
            print("list is empty") 
            return
        temp=self.last.next 
        count=0 
        while True: 
            count+=1
            temp=temp.next
            if temp==self.last.next:
                break
        print("total count is ",count)   
        
    def update(self,old_item,new_item):
        if self.last is None: 
            print('list is empty')
            return
        temp=self.last.next
        while True:
            if temp.data==old_item:
                temp.data=new_item
                print("node updated successfully: ")
                return 
            temp=temp.next
            if temp==self.last.next:
                break
        print('item not found')        
        
    def reverse_link(self):
        if self.last is None:
            print('list is empty')
            return
        head=self.last.next
        temp=head
        while True: 
            temp.next,temp.prev=temp.prev,temp.next 
            temp=temp.prev
            if temp==head:
                break
        self.last=head   
                              
    def display(self):
        if self.last is None:
            print('list is empty: ')
            return
        temp=self.last.next
        while True: 
            print(temp.data,end="<->") 
            temp=temp.next 
            if temp==self.last.next:
                break
        print()              

cd=CDLL()
#cd.insert_start(40)
cd.insert_start(30)
cd.insert_start(20)
cd.insert_start(10)
#cd.insert_last(50)
#cd.delete_first()
#cd.delete_last()
#cd.insert_before(25,30)
#cd.insert_after()
#cd.delete_before(30)
#cd.delete_after(30)
#cd.search(30)
#cd.reverse_list()
#cd.delete_item(30)
#cd.count()
#cd.update(10,5)
cd.reverse_link()
cd.display()        