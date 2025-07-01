import heapq

def ucs(graph, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    costs = {start: 0}
    parents = {start: None}

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parents[current_node]
            return path[::-1], current_cost

        for neighbor, edge_cost in graph[current_node].items():
            new_cost = current_cost + edge_cost
            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = current_node
                heapq.heappush(priority_queue, (new_cost, neighbor))
    return [], float('inf') #can't reach goal node

graph = {
    'S': {'A': 1, 'G': 12},
    'A': {'B': 3, 'C': 1},
    'B': {'D': 3},
    'C': {'D': 1, 'G': 2},
    'D': {'G': 3},
    'G': {}
}

path, total_cost = ucs(graph, 'S', 'G')

print(graph)
print()
print("Path: ", path)
print("Total Cost: ", total_cost)