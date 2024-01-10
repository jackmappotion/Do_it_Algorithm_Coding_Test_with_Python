# imports
from collections import deque

# input
def get_n_m():
    n, m = map(int, input().split())
    return n, m


def get_maps(n):
    maps = list()
    for _ in range(n):
        row = list(input())
        maps.append(row)
    return maps


n, m = get_n_m()
maps = get_maps(n)

## bfs
def bfs(maps, start, end):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    n, m = len(maps), len(maps[0])
    #
    visited = [[False] * m for _ in range(n)]
    
    queue = deque([(start[0], start[1], 1)])
    visited[start[0]][start[1]] = True
    while queue:
        c_r, c_c, dist = queue.popleft()

        if (c_r, c_c) == end:
            return dist

        for d_r, d_c in directions:
            n_r, n_c = (c_r + d_r, c_c + d_c)
            if (0 <= n_r < n) and (0 <= n_c < m) and (maps[n_r][n_c] == "1") and (not visited[n_r][n_c]):
                visited[n_r][n_c] = True
                queue.append((n_r, n_c, dist + 1))
    return -1

print(bfs(maps, (0, 0), (n-1, m-1)))
