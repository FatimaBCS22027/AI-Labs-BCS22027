#Program 1:

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def DLSS(self, src, target, limit,visited):
        if limit < 0:
            return False
        print (src,end=" ")
        if src == target:
            print(f"\nGoal {target} found\n")
            return True
        visited.add(src)
        if src not in self.graph:
            return False
        for neighbour in self.graph[src]: 
            if neighbour not in visited:
                if self.DLSS(neighbour, target, limit - 1,visited):
                    return True
        return False
    
    def DLS(self,src,target,limit):
        visited=set()
        if self.DLSS(src,target,limit,visited):
            return True
        else:
            print ("Goal not found")
            return False


# Build graph from image
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'F')
g.add_edge('A', 'D')
g.add_edge('A', 'E')
g.add_edge('B', 'K')
g.add_edge('B', 'J')
g.add_edge('K', 'N')
g.add_edge('K', 'M')
g.add_edge('D', 'G')
g.add_edge('D', 'C')
g.add_edge('E', 'C')
g.add_edge('E', 'H')
g.add_edge('E', 'I')
g.add_edge('I', 'L')

# Apply DLS
print("DLS path to G:")
g.DLS('A', 'L', 2)


#Program 2:
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def DLSS(self, src, target, limit,visited):
        if limit < 0:
            return False
        print (src,end=" ")
        if src == target:
            print(f"\nGoal {target} found\n")
            return True
        visited.add(src)
        if src not in self.graph:
            return False
        for neighbour in self.graph[src]: 
            if neighbour not in visited:
                if self.DLSS(neighbour, target, limit - 1,visited):
                    return True
        return False
    
    def DLS(self,src,target,limit):
        visited=set()
        if self.DLSS(src,target,limit,visited):
            return True
        else:
            return False

    # IDDFS main logic
    def IDDFS(self, src, target, max_depth):
        for depth in range(max_depth + 1):
            print(f"\nTrying depth limit: {depth}")
            if self.DLS(src, target, depth):
                return True
        print("\nGoal not found within max depth")
        return False


# Build the graph (same tree structure)
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'F')
g.add_edge('A', 'D')
g.add_edge('A', 'E')
g.add_edge('B', 'K')
g.add_edge('B', 'J')
g.add_edge('K', 'N')
g.add_edge('K', 'M')
g.add_edge('D', 'G')
g.add_edge('D', 'C')
g.add_edge('E', 'C')
g.add_edge('E', 'H')
g.add_edge('E', 'I')
g.add_edge('I', 'L')

# Apply IDDFS
print("IDDFS path to G:")
g.IDDFS('A', 'G', max_depth=5)


'''

In the above situation, we applied Depth Limited Search (DLS) with a depth limit of 3 and also used
Iterative Deepening Depth First Search (IDDFS or IDS) to find the goal node G in a tree starting from node A.
Both search methods successfully found the path A → D → G, but their behavior and efficiency differ:
DLS explored many nodes before reaching G, including unnecessary paths like B → K → N, K → M, and J, even though the goal was closer.
IDS, on the other hand, started from depth 0 and increased the limit step-by-step. It explored fewer nodes at the depth where the goal
actually existed (depth 2) and found the goal in a more optimal and structured way.

Conclusion:
Iterative Deepening Search (IDS) gave the best path in this situation because it found the goal node G at 
the shallowest depth (2) with minimal and structured exploration, ensuring both completeness and optimality.
While DLS also found the goal, it explored deeper and unnecessary branches first, making IDS the more efficient 
and reliable search in this scenario.


'''







