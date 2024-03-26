def solution(a, b):
    answer = 0
    if len(str(a/b)) >= 16:
        return 2
    else:
        return 1
    return answer
