from collections import deque


def bfs(land, visited, i, j):
    cnt = 0
    m = len(land[0])
    n = len(land)
    q = deque()
    visited.add((i, j))
    q.append((i, j))
    while q:
        ci, cj = q.popleft()
        for (di, dj) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in visited and land[ni][nj] == 1:
                visited.add((ni, nj))
                q.append((ni, nj))
                cnt += 1
    return cnt + 1


def solution(land):
    n = len(land)
    m = len(land[0])
    answer = 0
    for i in range(m):
        total_oil = 0
        visited = set()
        for j in range(n):
            if land[j][i] == 1 and (j, i) not in visited:
                total_oil += bfs(land, visited, j, i)
        answer = max(answer, total_oil)

    return answer
