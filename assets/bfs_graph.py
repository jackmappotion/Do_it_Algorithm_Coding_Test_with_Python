from collections import deque

def bfs_graph(graph,start):
    visited = list()
    to_visit = deque([start])
    while to_visit:
        current_visit = to_visit.popleft()
        if current_visit not in visited:
            visited.append(current_visit)
            to_visit.extend(graph[current_visit])
    return visited
