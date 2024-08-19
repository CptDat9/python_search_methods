def dfs(graph, start, vistied None):
    if vistied is None:
        vistied = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]
       if neighbor not in visited:
           dfs(graph, neighbor, vistied)
           
