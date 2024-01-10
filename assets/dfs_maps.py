from collections import deque

def dfs_maps(maps, start, end):
    #
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    n, m = len(maps), len(maps[0])
    #
    visited = [[False] * m for _ in range(n)]
    to_visit = deque([(start[0], start[1], 1)])
    #
    visited[start[0]][start[1]] = True
    while to_visit:
        c_r, c_c, dist = to_visit.popleft()
        if (c_r, c_c) == end:
            return dist

        for d_r, d_c in directions:
            n_r, n_c = c_r + d_r, c_c + d_c
            if (0 <= n_r < n) and (0 <= n_c < m) and (maps[n_r][n_c] == 1) and (not visited[n_r][n_c]):
                visited[n_r][n_c] = True
                to_visit.appendleft((n_r, n_c, dist + 1))
    return -1

