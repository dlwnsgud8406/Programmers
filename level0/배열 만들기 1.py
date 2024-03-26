def solution(n, k):
    answer = [i * k for i in range(1, n//k + 1)]
    return answer
