# imports
from collections import deque

# input
def get_graph_info():
    n,m,v = map(int,input().split())
    return n,m,v


def get_graph(n,m):
    graph = {_:[] for _ in range(1,n+1)} 
    for _ in range(m):
        i,j = map(int,input().split())
        graph[i].append(j)
        graph[j].append(i)
    return graph

n,m,v = get_graph_info()
graph = get_graph(n,m)

# sort_graph
def get_sorted_graph(graph):
    sorted_graph = {key:sorted(val) for key,val in graph.items()}
    return sorted_graph

sorted_graph=get_sorted_graph(graph)


# search
## dfs
def dfs(graph,v):
    visited = list()
    to_visit = deque([v])
    while to_visit:
        current_visit = to_visit.popleft()
        if current_visit not in visited:
            visited.append(current_visit)
            to_visit.extendleft(graph[current_visit][::-1])
    return visited

## bfs
def bfs(graph,v):
    visited = list()
    to_visit = deque([v])
    while to_visit:
        current_visit = to_visit.popleft()
        if current_visit not in visited:
            visited.append(current_visit)
            to_visit.extend(graph[current_visit])
    return visited

dfs_result = dfs(sorted_graph,v)
bfs_result = bfs(sorted_graph,v)

## print
print(' '.join(map(str,dfs_result)))
print(' '.join(map(str,bfs_result)))