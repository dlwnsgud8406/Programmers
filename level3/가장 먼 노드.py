from collections import deque


def bfs(graph, visited, s):
    q = deque()
    q.append(s)
    visited[s] = 1
    while q:
        n = q.popleft()
        for i in graph[n]:
            if not visited[i[0]]:
                visited[i[0]] = visited[n] + 1
                q.append(i[0])
    return max(visited)


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    for s, e in edge:
        graph[s].append((e, 1))
        graph[e].append((s, 1))
    for i in range(0, n + 1):
        graph[i].sort()

    m = bfs(graph, visited, 1)

    return visited.count(m)
