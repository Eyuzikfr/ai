def dls(graph, start, goal, limit):
  def recursive_dls(node, goal, limit, path):
    path.append(node)

    if node == goal:
      return path
  
    if limit <= 0:
      path.pop()
      return None
    
    for neighbor in graph.get(node, []):
      if neighbor not in path:
        result = recursive_dls(neighbor, goal, limit - 1, path)
        if result is not None:
          return result
    
    path.pop()
    return None
  
  return recursive_dls(start, goal, limit, [])

graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['A', 'B', 'F'],
    'E': ['A', 'F', 'G'],
    'F': ['D', 'E', 'G'],
    'G': ['E', 'F', 'H'],
    'H': ['G']
}

start_node = 'A'
goal_node = 'F'
depth_limit = 2

result = dls(graph, start_node, goal_node, depth_limit)

if result:
  print("Path found: ", result)
else:
  print("Path not found")