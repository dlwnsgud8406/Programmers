from collections import deque

def bfs(graph, visited, si, sj, ei, ej):
    answer = 0
    q = deque()
    visited[0][0][0] = 1
    q.append((si, sj, 0))
    while q:
        for _ in range(len(q)):
            i, j, used = q.popleft()
            for (di, dj) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < len(graph) and 0 <= nj < len(graph[0]) and not visited[ni][nj][used] and graph[ni][nj] == 1:
                    if (ni, nj) == (ei, ej):
                        return answer + 1
                    visited[ni][nj][used] = 1
                    q.append((ni, nj, used))
                if not used:
                    ni, nj = ni + di, nj + dj
                    if 0 <= ni < len(graph) and 0 <= nj < len(graph[0]) and not visited[ni][nj][True] and graph[ni][nj] == 1:
                        if (ni, nj) == (ei, ej):
                            return answer + 1
                        visited[ni][nj][1] = 1
                        q.append((ni, nj, 1))
        answer += 1
    return -1


def solution(n, m, hole):
    graph = [[1] * n for _ in range(m)]
    visited = [[[0] * 2 for _ in range(n)] for _ in range(m)]
    for i, j in hole:
        graph[j-1][i-1] = 0
    return(bfs(graph, visited, 0, 0, len(graph)-1, len(graph[0])-1 ))
