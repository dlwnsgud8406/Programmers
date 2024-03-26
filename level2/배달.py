import heapq

def dijkstra(distance, graph):
    heap = []
    heapq.heappush(heap, [0, 1])
    while heap:
        cost, node = heapq.heappop(heap)
        for c, n in graph[node]:
            if cost + c < distance[n]:
                distance[n] = cost + c
                heapq.heappush(heap, [cost+c, n])
    

def solution(N, road, K):
    distance = [float('inf')] * (N+1)
    distance[1] = 0
    graph = [[] for _ in range(N+1)]
    for r in road:
        graph[r[0]].append([r[2], r[1]])
        graph[r[1]].append([r[2], r[0]])
    dijkstra(distance, graph)
    
    return len([i for i in distance if i <= K])