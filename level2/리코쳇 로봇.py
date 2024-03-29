from collections import deque


def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    q = deque()
    graph = [[100 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                q.append((i, j, 0))
                graph[i][j] = 0
        if q:
            break
    while q:
        i, j, answer = q.popleft()
        if board[i][j] == 'G':
            return answer
        for (di, dj) in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            ni = i
            nj = j
            while 0 <= ni + di < n and 0 <= nj + dj < m and board[ni + di][nj + dj] != 'D':
                ni += di
                nj += dj
            if graph[ni][nj] > answer + 1:
                graph[ni][nj] = answer + 1
                q.append((ni, nj, answer + 1))

    return -1
