def solution(board):
    answer = 0
    arr = []
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, 1, -1, 1, -1, 0]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                arr.append((i, j))

    for x, y in arr:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(board) and 0 <= ny < len(board):
                board[nx][ny] = 1

    for line in board:
        answer += line.count(0)
    return answer
