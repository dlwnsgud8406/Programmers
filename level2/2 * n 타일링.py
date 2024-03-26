def solution(n):
    first = 2
    second = 3
    if n == 1 or n == 2:
        return first
    elif n == 3:
        return second
    else:
        for i in range(3, n):
            answer = first + second
            first = second
            second = answer
        return answer % 1000000007
print(solution(60000))
