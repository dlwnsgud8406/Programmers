def solution(a, b):
    answer = 0
    a, b = min(a,b), max(a,b)
    if a == b:
        answer = a
    else:
        for i in range(a, b+1):
            answer += i
    return answer
