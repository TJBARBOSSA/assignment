def longest_path(graph: list) -> int:
    topo_order = topological_sort(graph)
    return calculate_longest_path(graph, topo_order)

def topological_sort(graph):
    from collections import deque
    
    indegree = [0] * len(graph)
    for u in range(len(graph)):
        for v, _ in graph[u]:
            indegree[v] += 1
    
    queue = deque([i for i in range(len(graph)) if indegree[i] == 0])
    topo_order = []
    
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v, _ in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    
    return topo_order

def calculate_longest_path(graph, topo_order):
    dist = [-float('inf')] * len(graph)
    
    dist[topo_order[0]] = 0
    
    for node in topo_order:
        if dist[node] != -float('inf'):  
            for neighbor, weight in graph[node]:
                if dist[neighbor] < dist[node] + weight:
                    dist[neighbor] = dist[node] + weight
    
    return max(dist)