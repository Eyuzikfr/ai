import heapq

def ucs(graph, start, goal):
    visited = set()
    pq = [(0, start, [start])]  # (cost, current_node, path)

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, {}).items():
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))

    return None, float('inf')


graph = {
    'S': {'A': 1, 'G': 12},
    'A': {'B': 3, 'C': 1},
    'B': {'D': 3},
    'C': {'D': 1, 'G': 2},
    'D': {'G': 3},
    'G': {}
}

path, total_cost = ucs(graph, 'S', 'G')

print("Path: ", path)
print("Total Cost: ", total_cost)