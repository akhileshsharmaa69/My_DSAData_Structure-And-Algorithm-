class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right

class BST:
    def __init__(self):
        self.root=None  
    def insert(self,data):
        self.root=self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left=self.rinsert(root.left,data)
        elif data > root.item:
            root.right=self.rinsert(root.right,data)
        return root 
    def search(self,data):
        return self.rsearch(self.root,data)
    def rsearch(self,root,data):
        if root is None or root.item==data:
            return root
        if data<root.item:
           return self.rsearch(root.left,data)
        else:
            return self.rsearch(root.right,data)

    def inorder(self):
        result=[]
        self.rinorder(self.root,result)   
        return result
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)

    def preorder(self):
            result=[]
            self.rpreorder(self.root,result)   
            return result
    def rpreorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)

    def postorder(self):
            result=[]
            self.rpostorder(self.root,result)   
            return result
    def rpostorder(self,root,result):
            if root:
                self.rpostorder(root.left,result)
                self.rpostorder(root.right,result)
                result.append(root.item)

    def min_value(self,temp):
        current=temp
        while current.left is not None:
            current=current.left
        return current.item    
    def max_value(self,temp):
        current=temp
        while current.right is not None:
            current=current.right
        return current.item
    
    def delete (self,data):
        self.root=self.rdelete(self.root,data)  
    def rdelete(self,root,data):
        if root is None:
            return root
        if data < root.item:
            root.left=self.rdelete(root.left,data)
        elif data > root.item:
            root.right=self.rdelete(root.right,data)
        else:
            if  root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item=self.min_value(self,root.right)
            self.rdelete(root.right,root.item)
        return root 
    def size(self):
        return len(self.inorder())

b=BST()
b = BST()

b.insert(40)
b.insert(20)
b.insert(60)
b.insert(10)
b.insert(30)
b.insert(50)
b.insert(70)

print("Inorder:", b.inorder())
print("Preorder:", b.preorder())
print("Postorder:", b.postorder())

result = b.search(30)

if result:
    print("Found:", result.item)
else:
    print("Not Found")

print("Minimum:", b.min_value(b.root))
print("Maximum:", b.max_value(b.root))
print("Size:", b.size())

b.delete(10)

print("After delete:", b.inorder())

 


         




    
            


    

                   

        
    
    