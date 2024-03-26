def solution(a, b, n):
    answer = 0
    while n > a:
        bottle = 0
        while n > a:
            bottle = (n // a) * b
            n = n % a
        n += bottle
        answer += bottle
    answer += (n // a) * b
    return answer

print(solution(2, 1, 20))
