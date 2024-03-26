from collections import deque

def make_graph(wires, n):
    graph = []
    for i in range(n+1):
        node = []
        graph.append(node)
    for i in range(len(wires)):
        graph[wires[i][0]].append(wires[i][1])
        graph[wires[i][1]].append(wires[i][0])
    return graph

def bfs(graph, visited, start):
    visited[start] = True
    arr = []
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        arr.append(vertex)
        for i in graph[vertex]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return arr

def solution(n, wires):
    answer = 101
    wires = sorted(wires, key = lambda x:(x[0], x[1]))

    for i in range(len(wires)):
        wire = wires[:i] + wires[i+1:]
        graph = make_graph(wire, n)
        node = set(node)
        for j in range(1, n+1):
            visited = [False] * (n+1)
            bfs(graph, visited, j)
            node.add(visited.count(True))

        if max(node) - min(node) < answer:
            answer = max(node) - min(node)
    return answer

