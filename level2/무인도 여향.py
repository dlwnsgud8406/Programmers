from sys import setrecursionlimit
setrecursionlimit(10000)

def solution(maps):
    answer = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    height = len(maps)
    width = len(maps[0])
    vis = [[False for i in range(width)] for j in range(height)]

    def dfs(x, y) -> int:
        temp = 0
        if x < 0 or y < 0 or x >= height or y >= width:
            return temp
        if maps[x][y] != 'X' and vis[x][y] is False:
            vis[x][y] = True
            for i in range(4):
                temp += dfs(x + dx[i], y + dy[i])
            return int(maps[x][y]) + temp
        return temp
    for i in range(height):
        for j in range(width):
            if maps[i][j] != 'X' and vis[i][j] is False:
                answer.append(dfs(i, j))
    if len(answer) == 0:
        return [-1]
    return sorted(answer)
