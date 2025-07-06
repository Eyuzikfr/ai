import heapq

def greedy_bfs(graph, start, goal, heuristic):
  visited = set()
  queue = [(heuristic[start], start, [start])]  # priority, node, path

  while queue:
    _, current, path = heapq.heappop(queue)

    if current == goal:
      return path

    if current in visited:
      continue

    visited.add(current)

    for neighbor in graph.get(current, []):
      if neighbor not in visited:
        heapq.heappush(queue, (heuristic[neighbor], neighbor, path + [neighbor])) # maintains a minheap

  return None

graph = {
    'A': {'B': 22, 'D': 30, 'E': 25},
    'B': {'A': 22, 'C': 20, 'D': 11},
    'C': {'B': 20},
    'D': {'A': 30, 'B': 11, 'F': 10},
    'E': {'A': 25, 'F': 25, 'G': 40},
    'F': {'D': 10, 'E': 25, 'G': 12},
    'G': {'E': 40, 'F': 12, 'H': 6},
    'H': {'G': 6}
}

heuristic = {
  'A': 46,
  'B': 39,
  'C': 41,
  'D': 29,
  'E': 38,
  'F': 17,
  'G': 6,
  'H': 0
}

result = greedy_bfs(graph, 'A', 'H', heuristic)

if result:
  print ("Path found: ", result)
else:
  print("Path not found")