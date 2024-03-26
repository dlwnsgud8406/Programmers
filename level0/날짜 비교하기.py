def solution(data1, date2):
    answer = 0
    if data1[0] > date2[0]:
        return 0
    elif data1[0] < date2[0]:
        return 1
    else:
        if data1[1] > date2[1]:
            return 0
        elif data1[1] < date2[1]:
            return 1
        else:
            if data1[2] > date2[2]:
                return 0
            elif data1[2] < date2[2]:
                return 1
            else:
                return 0
