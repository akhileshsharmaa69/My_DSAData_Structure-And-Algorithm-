# manually created 
'''vertices=['A','B','C','D']
graph={}
for vertex in vertices:
    graph[vertex]=[]

edge=[
('A','B'),
('A','C'),
('B','C'),
('B','D')   
]   
for u,v in edge:
    graph[u].append(v)
    graph[v].append(u)
print('Adjancency list:')
for vertex in graph:
    print(vertex,"->" ,graph[vertex])'''
#class implemented
class graph:
    def __init__(self):
        self .adjlist={}

    def add_vertex(self,vertex):
        if vertex not in self.adjlist:
            self.adjlist[vertex] = []

    def addEdge(self,src,dest):
        self.add_vertex(src)
        self.add_vertex(dest)

        self.adjlist[src].append(dest)
        self.adjlist[dest].append(src)


            # Remove vertex function
    def remove_vertex(self, vertex):
        if vertex in self.adjlist:
            for neighbour in self.adjlist[vertex]:
                self.adjlist[neighbour].remove(vertex)

            del self.adjlist[vertex]
            print(vertex, "removed successfully")
        else:
            print(vertex, "not found")

    # Hash function
    def hash_function(self, key):
        return hash(key)

    def printgraph(self):
         print('adjancency list:')
         for  vertex in self.adjlist:
             print(vertex,"->",self.adjlist[vertex],end='\n')

                
g=graph()
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(1,4)
g.addEdge(4,3)
g.addEdge(2,4)
g.addEdge(4,5)
g.addEdge(3,5)
g.remove_vertex(2)
g.hash_function(1)
g.printgraph()
