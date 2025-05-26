# Program 1:

from collections import deque
class Graph:
    def __init__(self):
        self.adj={}

    def addEdge(self,v,w):
        if v not in self.adj:
            self.adj[v]=[]
        self.adj[v].append(w)

    def BFS(self,start):
        visited=set()
        queue=deque()
        visited.add(start)
        queue.append(start)

        while queue:
            node=queue.popleft()
            print(node,end=" ")
            if node in self.adj:
                for neighbour in self.adj[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print("BFS Traversal of the Graph is:")
g.BFS(2)

#Program 2:

from collections import deque
class Graph:
    def __init__(self):
        self.adj={}

    def add_edge(self,v,w):
        if v not in self.adj:
            self.adj[v]=[]
        self.adj[v].append(w)

    def BFS(self,start,goal):
        visited=set()
        queue=deque()
        visited.add(start)
        queue.append(start)

        while queue:
            node=queue.popleft()
            print(node,end=" ")
            if node==goal:
                print("\nGoal Node found")
                return

            if node in self.adj:
                for neighbour in self.adj[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
                    
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'F')
g.add_edge('A', 'D')
g.add_edge('A', 'E')
g.add_edge('B', 'K')
g.add_edge('B', 'J')
g.add_edge('B', 'A')
g.add_edge('F', 'A')
g.add_edge('D', 'G')
g.add_edge('D', 'A')
g.add_edge('E', 'C')
g.add_edge('E', 'H')
g.add_edge('E', 'I')
g.add_edge('E', 'A')
g.add_edge('K', 'N')
g.add_edge('K', 'M')
g.add_edge('K', 'B')
g.add_edge('J', 'B')
g.add_edge('G', 'D')
g.add_edge('C', 'I')
g.add_edge('H', 'I')
g.add_edge('I', 'I')
g.add_edge('I', 'E')
g.add_edge('I', 'L')
g.add_edge('N', 'K')
g.add_edge('M', 'K')
g.add_edge('L', 'I')

print("\nBFS Traversal of the Graph is:")
g.BFS('A', 'G')

#Program 3:

class PQueue:
  def __init__(self):
    self.adj=[]

  def enqueue(self,priority,element):
      self.adj.append((priority,element))
      self.adj.sort(key=lambda item:item[0])

  def size(self):
      return len(self.adj)
  
  def dequeue(self):
      if len(self.adj)==0:
          print("Queue is empty")
          return
      return self.adj.pop(0)[1]
  
 
  def __str__(self):
        return str([element for priority, element in self.adj])
  
q = PQueue()
q.enqueue(4, 10)
q.enqueue(5, 20)
q.enqueue(2, 30)
q.enqueue(1, 40)
print(q)
print(q.dequeue())
print(q)
print(q.size())
q.enqueue(3, 50)
print(q)
print(q.dequeue())
print(q.dequeue())
print(q)