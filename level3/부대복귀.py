from collections import deque


# def bfs(c, e, graph):
#     q = deque()
#     q.append((c, 0))

#     visited = [False] * (len(graph))
#     visited[c] = True

#     while q:
#         n, distance = q.popleft()
#         if n == e:
#             return distance
#         for i in graph[n]:
#             if not visited[i]:
#                 q.append((i, distance + 1))
#                 visited[i] = True
#     return -1


# def solution(n, roads, sources, destination):
#     answer = []
#     graph = [[] for _ in range(n+1)]

#     for road in roads:
#         graph[road[0]].append(road[1])
#         graph[road[1]].append(road[0])

#     for source in sources:
#         distance = bfs(source, destination, graph)
#         answer.append(distance)

#     return answer

def bfs(dest, graph, costs):
    q = deque([dest])
    costs[dest] = 0  # 자기 자신으로 가는 비용: 0

    while q:
        x = q.popleft()
        for node in graph[x]:
            if costs[node] == -1:  # 방문하지 않았다면
                q.append(node)
                costs[node] = costs[x] + 1

    return costs


def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]
    for s, e in roads:
        graph[s].append(e)
        graph[e].append(s)
    costs = [-1] * (n + 1)
    costs = bfs(destination, graph, costs)  # costs[i]: destination에서 지역 i로 갈 때 소모되는 비용

    return [costs[s] for s in sources]
