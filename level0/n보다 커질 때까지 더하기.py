def solution(numbers, n):
    answer = 0
    count = 0
    while answer <= n:
        answer += numbers[count]
        count += 1
    return answer
