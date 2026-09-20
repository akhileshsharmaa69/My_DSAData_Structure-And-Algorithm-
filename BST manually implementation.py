class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Node(40)
root.left=Node(20)
root.right=Node(60)
root.left.left=Node(10)
root.left.right=Node(30)
root.right.right=Node(70)
root.right.left=Node(50)
def preorder(root):
    if root is None:
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)
print("traversal of a preorder of a tree",preorder(root)) 

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
print("trsversal of a inorder of a tree",inorder(root))

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")
print("traversal of a postorder of tree",postorder(root))

def count_nodes(root):
    if root is None:
        return 0
    return 1+ count_nodes(root.left)+count_nodes(root.right)
print("node of tree",count_nodes(root))    

def count_leaf_node(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaf_node(root.left)+count_leaf_node(root.right)
print("leaf node of tree",count_leaf_node(root))

def height(root):
    if root is None:
        return-1
    left_height=height(root.left)
    right_height=height(root.right)
    return 1+max(left_height,right_height)
print("height of tree",height(root))


def search(root,value):
    if root is None:
        print("item not found:")
        return False
    if root.data==value:
        print("item found:",value)
        return True
    if value<root.data:
        return search(root.left,value)
    else:
        return search(root.right,value)
print(search(root,60))
print(search(root,40))
print(search(root,25))

def insertion(root,value):
    if root is None:
        return Node(value)
    if value < root.data:
        root.left=insertion(root.left,value)
    else:
        root.right=insertion(root.right,value)
    return root
insertion(root,25)
print("node inserted successfully") 
inorder(root) 
print(search(root,25))

def delete(root,value):
    if root is None:
        return None
    # Node find 
    if value<root.data:
        root.left=delete(root.left,value)
    elif value>root.data:
        root.right=delete(root.right,value)
    else:
        #case 1 and 2
        if root.left is None:
             return root.right
        if root.right is None:
            return root.left
        #case 3
        temp=root.right
        while temp.left is not None:
            temp=temp.left
        root.data=temp.data
        root.right=delete(root.right,temp.data)
    return root        
delete(root,40)
print("node deleted successefully") 
inorder(root) 

def find_min(root):
    if root is None:
        return None
    while root.left is not None:
        root=root.left
    return root.data
print('min node find:',find_min(root))
inorder(root)

def find_max(root):
    if root is None:
        return None
    while root.right is not None:
        root=root.right
    return root.data
print('find max node',find_max(root))

def find_successor(root,value):
    successor=None
    while root is not None:
        #case 2
        if value<root.data:
            successor=root
            root=root.left

        elif value>root.data:
            root=root.right
        else:
            #case 1 
            if root.right is not None:
             temp=root.right
             while temp.left is not None:
                temp=temp.left
            successor=temp
            break 
        # case 3
    if successor is None:
        return None
    return successor.data
print("succsessor",find_successor(root,50))
inorder(root)

def find_predessor(root,value):
    predessor=None
    while root is not None:
        if value<root.data:
            root =root.left
        elif value>root.data:
            predessor=root
            root=root.right
        else:
            if root.left is not None:
                temp=root.left
                while temp.right is not None:
                    temp=temp.right
                predessor=temp
                break
    if predessor is None:
        return None
    return predessor.data

print("predessor",find_predessor(root,40))   

def valid_BST(root,lowerlimit,upperlimit):
    if root is None:
        return True
    if root.data<=lowerlimit or root.data>=upperlimit:
        return False
    return (valid_BST(root.left,lowerlimit,root.data) and valid_BST(root.right,root.data,upperlimit))

print('valid BST',valid_BST(root,float('-inf'),float('inf')))   

        





       
