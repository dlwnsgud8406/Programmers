from collections import deque
def solution(maps):
    x = y = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    def bfs(x, y):
        deq = deque()
        deq.append((x, y))
        while deq:
            x, y = deq.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue
                if not maps[nx][ny]:
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    deq.append((nx, ny))

        return maps[-1][-1]
    answer = bfs(x, y)
    return -1 if answer == 1 else answer
