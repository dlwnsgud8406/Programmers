from collections import deque


def bfs(start, end, maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    q = deque([])
    flag = False

    for i in range(n):
        for j in range(m):
            if maps[i][j] == start:
                q.append((i, j, 0))
                visited[i][j] = True
                flag = True
                break
        if flag:
            break
    while q:
        si, sj, cost = q.popleft()
        if maps[si][sj] == end:
            return cost
        for (di, dj) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni = si + di
            nj = sj + dj
            if 0 <= ni < n and 0 <= nj < m and maps[ni][nj] != 'X' and not visited[ni][nj]:
                q.append((ni, nj, cost + 1))
                visited[ni][nj] = True
    return -1


def solution(maps):
    from_start_to_lever_path = bfs('S', 'L', maps)
    from_lever_to_exit_path = bfs('L', 'E', maps)

    if from_start_to_lever_path != -1 and from_lever_to_exit_path != -1:
        return from_start_to_lever_path + from_lever_to_exit_path

    return -1
