'''def dfs(graph,vertex,visited):
    visited.add(vertex)
    print(vertex,end=" ")

    for neighbour in graph[vertex]:
        if neighbour  not in visited:
         dfs(graph,neighbour,visited)

graph={
"A":["B","C"],
'B':['D','E'],
'C':[],
'D':[],
'E':[]
}            
visited=set()
dfs(graph,'A',visited)'''

#impleted by class
class graph:
    def __init__(self): # store the graph connection
        self.adjlist={}

    # add the edge of graph
    def add_edge(self,u,v):
        if u not in self.adjlist:
            self.adjlist[u]=[]
        if v not in self.adjlist:
            self.adjlist[v]=[]
        self.adjlist[u].append(v)
        self.adjlist[v].append(u)

    def dfs_util(self,vertex,visited):
        print(vertex,end=" ")
        visited.add(vertex)

        if vertex in self.adjlist:
            for neighbour in self.adjlist[vertex]:
                if neighbour not in visited:
                    self.dfs_util(neighbour,visited)

    def dfs(self,start):
        visited=set()
        print("DFS traversal",end='')
        self.dfs_util(start,visited)
        print()


g=graph()
g.add_edge("A","B")
g.add_edge("A","C")
g.add_edge("B","D")
g.add_edge("C","E")

g.dfs("A")
