#Program 1:

import heapq

class Graph:
    def __init__(self):
        self.graph = {}         # adjacency list: node -> list of (neighbor, cost)
        self.heuristic = {}     # node -> heuristic value

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def set_heuristic(self, node, h_value):
        self.heuristic[node] = h_value

    def greedy_best_first_search(self, start, goal):
        visited = set()
        priority_queue = []
        heapq.heappush(priority_queue, (self.heuristic[start], start))
        came_from = {start: None}

        while priority_queue:
            _, current = heapq.heappop(priority_queue)

            if current == goal:
                return self.reconstruct_path(came_from, goal)

            if current in visited:
                continue

            visited.add(current)
            
            if current in self.graph:
                for neighbor in self.graph[current]:
                    if neighbor not in visited:
                        heapq.heappush(priority_queue, (self.heuristic[neighbor], neighbor))
                        if neighbor not in came_from:
                            came_from[neighbor] = current

        return None  # No path found

    def reconstruct_path(self, came_from, goal):
        path = []
        while goal is not None:
            path.append(goal)
            goal = came_from[goal]
        return path[::-1]

# -----------------------------
# Example usage:

g = Graph()

# Graph structure (directed)
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.add_edge('C', 'E')
g.add_edge('E', 'F')
g.add_edge('D', 'F')

# Heuristic values (straight-line distance to goal 'F')
g.set_heuristic('A', 7)
g.set_heuristic('B', 6)
g.set_heuristic('C', 4)
g.set_heuristic('D', 3)
g.set_heuristic('E', 2)
g.set_heuristic('F', 0)

path = g.greedy_best_first_search('A', 'F')
print("Path found:", path)

#Program 2:

import heapq

def astar(graph, heuristics, start, goal):
    open_list = [(heuristics[start], 0, start, [])]  # (f, g, node, path)
    closed_list = set()

    while open_list:
        f, g, node, path = heapq.heappop(open_list)

        if node in closed_list:
            continue
        path = path + [node]

        if node == goal:
            return path

        closed_list.add(node)

        for neighbor, cost in graph[node].items():
            if neighbor not in closed_list:
                g_new = g + cost
                f_new = g_new + heuristics[neighbor]
                heapq.heappush(open_list, (f_new, g_new, neighbor, path))

    return None


# Example graph
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'D': 5, 'E': 12},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 5, 'G': 7},
    'E': {'B': 12, 'G': 3, 'H': 6},
    'F': {'C': 3, 'H': 8},
    'G': {'D': 7, 'E': 3, 'I': 2},
    'H': {'E': 6, 'F': 8, 'I': 4},
    'I': {'G': 2, 'H': 4}
}

# Heuristic values
heuristics = {
    'A': 14, 'B': 12, 'C': 11,
    'D': 9, 'E': 7, 'F': 6,
    'G': 4, 'H': 4, 'I': 0
}

# Run search
result = astar(graph, heuristics, 'A', 'I')
print("Path found:", result)


#Example 3:
import heapq

# Heuristic: number of misplaced tiles
def misplaced_tiles(state, goal):
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])

# Get neighbors (possible moves of the blank)
def get_neighbors(state):
    neighbors = []
    index = state.index(0)  # blank position
    row, col = divmod(index, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_state = state[:]
            swap = r * 3 + c
            new_state[index], new_state[swap] = new_state[swap], new_state[index]
            neighbors.append(new_state)
    return neighbors

# A* search
def astar(start, goal):
    open_list = [(misplaced_tiles(start, goal), 0, start, [])]  # (f, g, state, path)
    closed = set()

    while open_list:
        f, g, state, path = heapq.heappop(open_list)

        if state == goal:
            return path + [state]

        closed.add(tuple(state))

        for neighbor in get_neighbors(state):
            if tuple(neighbor) not in closed:
                g_new = g + 1
                f_new = g_new + misplaced_tiles(neighbor, goal)
                heapq.heappush(open_list, (f_new, g_new, neighbor, path + [state]))

    return None

# Example
start = [1, 2, 3,
         5, 6, 0,
         7, 8, 4]

goal = [1, 2, 3,
        5, 8, 6,
        0, 7, 4]

solution = astar(start, goal)

if solution:
    print("Steps to solve:")
    for s in solution:
        print( "" ,s[0:3], "\n", s[3:6], "\n", s[6:9], "\n")
else:
    print("No solution found.")
