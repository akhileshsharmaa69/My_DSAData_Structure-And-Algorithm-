#manually implemented
'''vertex=['A','B','C','D']
n=len(vertex)
matrix=[[0]*n for _ in range(n)]
edges=[
('A','B'),
('A','C'),
('B','C'),
('B','D')     
]
for u,v in edges:
    i = vertex.index(u)
    j = vertex.index(v)
    matrix[i][j] = 1
    matrix[i][j] = 1
    
print('adejancy matrix')

for i in range(n):
    print(matrix[i])'''


#class implemented

class graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_matrix=[[0]*vno for e in range (vno)]

    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=weight
            self.adj_matrix[v][u]=weight
        else:
            print('inavlid graph:')

    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=0
            self.adj_matrix[v][u]=0
        else:
            print("invalid graph:")   

    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v]!=0
        else:
            print('invalid graph')

    def print_adj_matrix(self):
        for row_list in self.adj_matrix:
            print(" " .join(map(str,row_list)))     

g=graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)

g.remove_edge(3,4)
g.has_edge(0,1)

g.print_adj_matrix()





