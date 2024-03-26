def solution(board, moves):
    answer = 0
    new_board = list(map(list, zip(*board)))
    arr = []
    for idx in moves:
        if max(new_board[idx-1]) == 0:
            pass
        else:
            for i in range(len(new_board[idx-1])):
                if new_board[idx-1][i] != 0:
                    arr.append(new_board[idx-1][i])
                    new_board[idx-1][i] = 0
                    break
            if arr[len(arr)-1] == arr[len(arr)-2] and len(arr) > 1:
                arr.pop()
                arr.pop()
                answer += 2
    return answer
