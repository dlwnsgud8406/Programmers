def solution(board1, date2):
    answer = 0
    if board1[0] > date2[0]:
        return 0
    elif board1[0] < date2[0]:
        return 1
    else:
        if board1[1] > date2[1]:
            return 0
        elif board1[1] < date2[1]:
            return 1
        else:
            if board1[2] > date2[2]:
                return 0
            elif board1[2] < date2[2]:
                return 1
            else:
                return 0
