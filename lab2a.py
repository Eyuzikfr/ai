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

print(graph)