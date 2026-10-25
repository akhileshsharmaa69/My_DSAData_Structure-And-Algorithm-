from collections import deque# using deque creating to easily remove front element
'''def bfs(graph,start):
    queue=deque([start])
    visited={start}

    while queue: # jab tak queue emty nahi hota loop run karta rahega
        vertex=queue.popleft()
        print(vertex,end=" ")

        for neighbour in graph[vertex]: #each neighbour we are cheking 
            if neighbour not in visited: # check neighbour visited or not
                visited.add(neighbour)# mark the visited neighbour
                queue.append(neighbour)# add the neighbour rear of queue

graph={
    "A":['B','C'],
    'B':['D'],
    'C':['E'],
    'D':[],
    'E':[]
}         
bfs(graph,'A') '''

#implemented by  class
class graph:
    def __init__(self):
        self.adjlist={}

    def add_edge(self,u,v):
        #add the edge 
        if u not in self.adjlist:
            self.adjlist[u]=[]
        if v not in self.adjlist:
            self.adjlist[v]=[]
        self.adjlist[u].append(v)
        self.adjlist[v].append(u)

    def bfs(self,start):
        queue=deque([start])
        visited={start}

        while queue:
            vertex=queue.popleft()
            print(vertex,end=" ")

            for neighbour in self.adjlist[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
                    
                    

g=graph()
g.add_edge("A","B")
g.add_edge("A","C")
g.add_edge("B","D")
g.add_edge("C","E")

g.bfs("A")


