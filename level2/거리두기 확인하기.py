from collections import deque


def bfs(place):
    start = []

    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                start.append([i, j])
    for s in start:
        q = deque([s])
        graph = [[0] * 5 for i in range(5)]
        visited = [[0] * 5 for i in range(5)]
        visited[s[0]][s[1]] = 1
        while q:
            ci, cj = q.popleft()
            for (di, dj) in ((1, 0), (-1, 0), (0, -1), (0, 1)):
                ni, nj = ci + di, cj + dj
                if 0 <= ni < 5 and 0 <= nj < 5 and not visited[ni][nj]:
                    if place[ni][nj] == 'O':
                        q.append([ni, nj])
                        visited[ni][nj] = 1
                        graph[ni][nj] = graph[ci][cj] + 1
                    if place[ni][nj] == 'P' and graph[ci][cj] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []

    for place in places:
        answer.append(bfs(place))
    return answer
