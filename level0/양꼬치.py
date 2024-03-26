def solution(n, k):
    answer = 0
    answer -= (n // 10) * 2000
    return answer + 12000 * n + 2000 * k
