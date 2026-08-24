class Node:
    def __init__(self,data,priority):
        self.data=data
        self.priority=priority
        self.next=None

class priorityQueue:
    def __init__(self):
        self.front=None
        self.rear=None
        return
    def enqueue(self,data,priority):
        n=Node(data,priority)
        if self.front is None:
            self.front=n
            self.rear=n
            return
        temp=self.front
        while temp is not None and priority >= temp.priority:
            prev=temp
            temp=temp.next
        n.next=temp
        prev.next=n

    def dequeue(self):
        if self.front is None:
            print("priority queueue is empty:")
            return
        item=self.front.data
        self.front=self.front.next
        if self.front is None:
            self.rear=None
        return item
    def peek(self):
        if self.front is None:
            print("priority queue is empty:")
            return
        return self.front.data
    def isEmpty(self):
        return self.front is None
    def display(self):
        if self.front is None:
            print("priority queueue is emty")
            return
        temp=self.front
        while temp is not None:
            print(temp.data,temp.priority,end="->")
            temp=temp.next
        print("None")

p1=priorityQueue()
p1.enqueue(10,1)
p1.enqueue(20,4)
p1.enqueue(30,3)
p1.enqueue(40,2)
p1.dequeue()
print("front data",p1.peek())
print(p1.isEmpty())
p1.display()

        
            
        
        
    












    
