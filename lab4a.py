import heapq

def a_star_search(graph, start, goal, heuristic):
  visited = set()
  # priority queue: (heuristic, cumulative cost, node, path)
  pq = [(heuristic[start], 0, start, [start])]

  while pq:
    f, g, current, path = heapq.heappop(pq)

    if current == goal:
      return path, g
    
    if current in visited:
      continue
    visited.add(current)

    for neighbor, cost in graph.get(current, {}).items():
      if neighbor not in visited:
        new_g = g + cost
        new_f = new_g + heuristic[neighbor]
        heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

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

result, total_cost = a_star_search(graph, 'A', 'H', heuristic)

if result:
  print("Path found: ", result)
  print("Total Cost: ", total_cost)
else:
  print("Path not found")