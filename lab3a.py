from collections import deque

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

graph = {
    'A': ['B', 'C'],    # A is connected to B and C
    'B': ['D', 'E'],    # B is connected to D and E
    'C': ['F'],         # C is connected to F
    'D': ['G'],         # D is connected to G
    'E': ['H'],         # E is connected to H
    'F': [],            # F is not connected to any node
    'G': [],            # G is not connected to any node
    'H': [],            # H is not connected to any node
}

print("Graph:\n", graph)
print()
print("BFS: ", end=' ')
bfs(graph, 'A', 'H')
print()
print("DFS: ", end=' ')
dfs(graph, 'A', 'H')
print()