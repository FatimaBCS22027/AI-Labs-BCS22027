#Program 1:

class Graph:
    def __init__(self):
        self.adj = {}

    def addEdge(self, v, w):
        if v not in self.adj:
            self.adj[v] = []
        self.adj[v].append(w)


    def DFSUtil(self, node, visited):
        visited.add(node)
        print(node, end=" ")
        if node in self.adj:
            for neighbour in self.adj[node]:
                if neighbour not in visited:
                    self.DFSUtil(neighbour, visited)

    def DFS(self, start):
        visited = set()
        self.DFSUtil(start, visited)

# Driver code
g = Graph()
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(2, 1)
g.addEdge(3, 1)
g.DFS(2)
print()

#Program 2:



class Graph:

    def __init__(self):
        self.adj={}
    def addedge(self,v,w):
        if v not in self.adj:
            self.adj[v]=[]
        self.adj[v].append(w)
        
        

    def dfs_stack(self,start, goal):
      stack = [start]
      visited = [start]

      while stack:
          s=stack.pop()
          print(s,end=" ")
          if(s==goal):
              print ("Goal found")
              return
          if s in self.adj:
            for neighbours in self.adj[s]:
                if neighbours not in visited:
                    stack.append(neighbours)
                    visited.append(neighbours)
      print("Goal not found") 


g=Graph()
g.addedge("A", "E")
g.addedge("A", "D")
g.addedge("A", "F")
g.addedge("A", "B")
g.addedge("B", "J")
g.addedge("B", "K")
g.addedge("D", "C")
g.addedge("D", "G")
g.addedge("E", "H")
g.addedge("E", "C")
g.addedge("E", "I")
g.addedge("K", "M")
g.addedge("K", "N")
g.addedge("I", "L")
g.dfs_stack("A","G")

