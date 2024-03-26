def solution(n):
    answer = 0
    a = 0
    b = 1
    for i in range(n-1):
        answer =  a + b
        a = b
        b = answer
    return int(answer)

print(solution(6))