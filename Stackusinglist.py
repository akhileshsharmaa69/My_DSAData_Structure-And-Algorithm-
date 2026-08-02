#stack using list ()
class Stack:
    def __init__(self):
        self.Stack=[None]*5
        self.top=-1
        
    def push(self,data):
        if self.top==len(self.Stack)-1:
            print("stack is overflow")
            return
        self.top=self.top+1
        #self.top+=1
        self.Stack[self.top]=data
    
    def pop(self):
        if self.top==-1:
            print("stack is underflow: ")
            return 
        item=self.Stack[self.top]
        self.Stack[self.top]=None
        self.top=self.top-1
        return item  
            
    def peek(self):
        if self.top==-1:
            return
        print('your first element is' ,self.Stack[self.top])  
         
        
              
    def isEmty(self):
        if self.top==-1:
            return True 
        return False    
        
    def isfull(self):
        if self.top==len(self.Stack)-1:
            return True
        return False
    
    
    
    
     
    def display(self):
        #check stack is empty or not
        if self.top==-1:
            print('Stack is empty: ')
            return
            #top se start karo
        i=self.top
        # jb tak index 0 se bada ya brabar ho
        while i>=0:
            print(self.Stack[i],end=" ")# current element 
            i=i-1 #ek kam karo   
        print()   
        
        
        
        
    
s1=Stack()
s1.push(10)  
s1.push(20) 
s1.push(30)
s1.push(40)
s1.push(50)
#s1.pop()
#s1.pop()
s1.peek()
print(s1.isEmty())
print(s1.isfull())
s1.display()          

            