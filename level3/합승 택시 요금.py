import sys
import heapq

INF = sys.maxsize


def dijkstra(graph, start, n):
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = [(0, start)]
    while q:
        c_dist, c_node = heapq.heappop(q)
        if distance[c_node] < c_dist:
            continue
        for n_node, n_dist in graph[c_node]:
            if distance[n_node] > c_dist + n_dist:
                distance[n_node] = c_dist + n_dist
                heapq.heappush(q, (c_dist + n_dist, n_node))
    return distance


def solution(n, s, a, b, fares):
    answer = INF
    graph = [[] for _ in range(n + 1)]
    for v, u, c in fares:
        graph[v].append((u, c))
        graph[u].append((v, c))
    D = [0] + [dijkstra(graph, i, n) for i in range(1, n + 1)]

    for i in range(1, n + 1):
        answer = min(answer, D[s][i] + D[i][a] + D[i][b])
    return answer
