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

# graph = {
#     'A': ['B', 'C'],         # A is connected to B and C
#     'B': ['A', 'D', 'E'],    # B is connected to D and E
#     'C': ['A', 'F'],         # C is connected to F
#     'D': ['B', 'G'],         # D is connected to G
#     'E': ['B', 'H'],         # E is connected to H
#     'F': ['C'],              # F is connected to C
#     'G': ['D'],              # G is connected to D
#     'H': ['E']
# }

# graph = {
#   'A': ['B', 'F'],
#   'B': ['A', 'C', 'D'],
#   'C': ['B', 'E'],
#   'D': ['B'],
#   'E': ['C'],
#   'F': ['A', 'G'],
#   'G': ['F']
# }

graph = {
  'A': ['B', 'C', 'D'],
  'B': ['A', 'C', 'E'],
  'C': ['A', 'B', 'F'],
  'D': ['A', 'G'],
  'E': ['B', 'I'],
  'F': ['C', 'G', 'I'],
  'G': ['D', 'F', 'I'],
  'I': ['E', 'F', 'K'],
  'J': ['G', 'K'],
  'K': ['I', 'J']
}

start_node = 'A'
goal_node = 'G'
depth_limit = 2

result = dls(graph, start_node, goal_node, depth_limit)

if result:
  print("Path found: ", result)
else:
  print("Path not found")