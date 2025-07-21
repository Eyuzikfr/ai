def minmax(node, isMaximizing):
  if node not in graph or len(graph[node]) == 0:
    return scores[node]
  
  if isMaximizing:
    best_value = -float('inf')
    for child in graph[node]:
      val = minmax(child, False)
      best_value = max(best_value, val)
    return best_value
  else:
    best_value = float('inf')
    for child in graph[node]:
      val = minmax(child, True)
      best_value = min(best_value, val)
    return best_value

def alphaBetaPruning(node, isMaximizing, alpha, beta):
  if node not in graph or len(graph[node]) == 0:
    return scores[node]
  
  if isMaximizing:
    max_eval = -float('inf')
    for child in graph[node]:
      eval = alphaBetaPruning(child, False, alpha, beta)
      max_eval = max(max_eval, eval)
      alpha = max(alpha, eval)
      if beta <= alpha:
        print(f"Pruned at node '{node}' (MAX): beta <= alpha ({beta} <= {alpha})")
        break
    return max_eval
  else:
    min_eval = float('inf')
    for child in graph[node]:
      eval = alphaBetaPruning(child, True, alpha, beta)
      min_eval = min(min_eval, eval)
      beta = min(beta, eval)
      if beta <= alpha:
        print(f"Pruned at node '{node}' (MIN): beta <= alpha ({beta} <= {alpha})")
        break
    return min_eval

graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F', 'G'],
  'D': ['H', 'I'],
  'E': ['J', 'K'],
  'F': ['L', 'N'],
  'G': ['R', 'S'],
  'H': [],
  'I': [],
  'J': [],
  'K': [],
  'L': [],
  'N': [],
  'R': [],
  'S': []
}

scores = {
  'H': 5,
  'I': 6,
  'J': 7,
  'K': 4,
  'L': 3,
  'N': 2,
  'R': 8,
  'S': 1
}

result = minmax('A', True)
print("Best value for maximizing player: ", result)

result = alphaBetaPruning('A', True, -float('inf'), float('inf'))
print("Best value with alpha-beta pruning: ", result)