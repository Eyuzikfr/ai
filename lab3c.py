graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

def DLS(graph, node, goal, limit, depth=0, path=None):
    if path is None:
        path = []

    path.append(node)   

    if node == goal:
        return path  
    if depth == limit:
        return None   

    for neighbor in graph[node]:
        result = DLS(graph, neighbor, goal, limit, depth + 1, path)
        if result is not None:
            return result

    return None   
limit = 2
goal = 'F'
start = 'A'
path = DLS(graph, start, goal, limit)

if path:
    print("Path to goal:", path)
else:
    print("No path found")