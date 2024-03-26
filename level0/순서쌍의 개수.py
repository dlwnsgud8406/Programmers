def solution(n):
    answer = []
    for i in range(1, n+1):
        if n / i == int(n / i):
            answer.append(i)
    return len(answer)
