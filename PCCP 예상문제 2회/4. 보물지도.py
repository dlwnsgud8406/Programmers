from collections import deque

def bfs(graph, visited, si, sj, ei, ej):
    answer = 1
    q = deque()
    q.append((si, sj, 0))
    visited[si][sj][0] = 1
    while q:
        for _ in range(len(q)):
            i, j, available = q.popleft()
            for (di, dj) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < len(graph) and 0 <= nj < len(graph[0]) and graph[ni][nj] == 0 and not visited[ni][nj][available]:
                    if (ni, nj) == (ei, ej):
                        return answer
                    visited[ni][nj][available] = 1
                    q.append((ni, nj, available))
                if not available:
                    ni, nj = ni + di, nj + dj
                    if 0 <= ni < len(graph) and 0 <= nj < len(graph[0]) and graph[ni][nj] == 0 and not visited[ni][nj][available]:
                        if (ni, nj) == (ei, ej):
                            return answer
                        visited[ni][nj][1] = 1
                        q.append((ni, nj, 1))
        answer += 1
    return -1

def solution(n, m, hole):
    graph = [[0 for _ in range(n)] for _ in range(m)]
    visited = [[[0] * 2 for _ in range(n)]for _ in range(m)]
    for i, j in hole:
        graph[j-1][i-1] = 1

    return bfs(graph, visited, 0, 0, len(graph)-1, len(graph[0]) - 1)
