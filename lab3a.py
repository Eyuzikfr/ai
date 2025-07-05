from collections import deque

def dfs(graph, start, goal):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex == goal:
            print(vertex)
            return
        
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)

            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        if vertex == goal:
            print(vertex)
            return

        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

graph = {
    'A': ['B', 'C'],         # A is connected to B and C
    'B': ['A', 'D', 'E'],    # B is connected to D and E
    'C': ['A', 'F'],         # C is connected to F
    'D': ['B', 'G'],         # D is connected to G
    'E': ['B', 'H'],         # E is connected to H
    'F': ['C'],              # F is connected to C
    'G': ['D'],              # G is connected to D
    'H': ['E']

}

print("DFS: ", end=' ')
dfs(graph, 'A', 'H')
print()
print("BFS: ", end=' ')
bfs(graph, 'A', 'H')
print()